from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from airflow.providers.mysql.hooks.mysql import MySqlHook
from ingestion import ingestion, preparation
from config import configs

config_file = configs

def create_sql(data, table):
    data['load_date'] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    lst = []
    data.fillna("NaN")
    for i in range(len(data)):
        val = tuple(list(tuple(data.values))[i])
        lst.append(val)
    cols = '('+(' , '.join(data.columns.tolist()))+')'
    sql = f"INSERT INTO {table} {cols} VALUES {str(lst)[1:-1]};"
    return sql

def _t0(ti):
    df = ingestion()
    sql = create_sql(df, "cadastro_raw")
    MySqlHook(mysql_conn_id='mysql_con', schema = 'db').run(sql)

def _t1(ti):
    df = preparation()
    sql = create_sql(df, "cadastro")
    MySqlHook(mysql_conn_id='mysql_con', schema = 'db').run(sql)

with DAG(
    "dataops-treinamento",
    start_date=datetime(2023, 10, 10), 
    schedule_interval=timedelta(minutes=2),
    catchup=False) as dag:

    t0 = PythonOperator(
        task_id='t0',
        python_callable=_t0
    )

    t1 = PythonOperator(
        task_id='t1',
        python_callable=_t1
    )

    t0 >> t1