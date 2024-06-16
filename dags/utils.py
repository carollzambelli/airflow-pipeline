import os
import pandas as pd
from datetime import datetime
import mysql.connector
from sqlalchemy import create_engine   

class Saneamento:
    
    def __init__(self, data, configs):
        self.data = data
        self.colunas = configs["metadados"]['nome_original']
        self.colunas_new = configs["metadados"]['nome']
        self.tipos = configs["metadados"]['tipos']  

    def select_rename(self):
        self.data = self.data.loc[:, self.colunas] 
        for i in range(len(self.colunas)):
            self.data.rename(columns={self.colunas[i]:self.colunas_new[i]}, inplace = True)

    def tipagem(self):
        for col in self.colunas_new:
            tipo = self.tipos[col]
            if tipo == "int":
                tipo = self.data[col].astype(int)
            elif tipo == "float":
                self.data[col].replace(",", ".", regex=True, inplace = True)
                self.data[col] = self.data[col].astype(float)
            elif tipo == "date":
                self.data[col] = pd.to_datetime(self.data[col]).dt.strftime('%Y-%m-%d')
        return self.data
    
def save_folder(data, path):
    data['load_date'] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    if not os.path.exists(path):
        data.to_csv(path, index=False, sep = ";")
    else:
        data.to_csv(path, index=False, mode='a', header=False, sep = ";")


def save_mysql(data, myhost, table):
    data['load_date'] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    con = mysql.connector.connect(
        user='root', password='root', host=myhost, port="3306", database='db')
    
    print("DB connected")
    
    engine  = create_engine(f"mysql+mysqlconnector://root:root@{myhost}/db")
    data.to_sql(table, con=engine, if_exists='append', index=False)
    con.close()


def read_mysql(myhost, table):

    con = mysql.connector.connect(
        user='root', password='root', host=myhost, port="3306", database='db')
    
    cursor = con.cursor()
    cursor.execute(f'Select * FROM {table}')
    cadastro_raw = cursor.fetchall()
    df = pd.DataFrame(cadastro_raw)

    cursor.execute('describe cadastro_raw')
    cols = cursor.fetchall()
    colunas = []
    for i in range(len(cols)):
        colunas.append(cols[i][0])

    df.columns = colunas
    con.close()
    return df

def error_handler(exception_error, stage, path):
    
    log = [stage, type(exception_error).__name__, exception_error,datetime.now()]
    logdf = pd.DataFrame(log).T
    
    if not os.path.exists(path):
        logdf.columns = ['stage', 'type', 'error', 'datetime']
        logdf.to_csv(path, index=False,sep = ";")
    else:
        logdf.to_csv(path, index=False, mode='a', header=False, sep = ";")
