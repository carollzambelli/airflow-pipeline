import os
from datetime import datetime

local_path = os.path.abspath(os.getcwd())
data_path = os.path.dirname(os.path.dirname(local_path))

date_now = datetime.now().date()


configs = {
    "path":{
        "raw": f"{data_path}/data/raw/raw_cadastro_{date_now}.csv",
        "work": f"{data_path}/data/work/work_cadastro_{date_now}.csv",
        "logs": f"{data_path}/data/logs/logs_cadastro_{date_now}.csv"
    },
    "metadados":{
        "nome_original": [
            "gender",
            "name.title",
            "name.first",
            "name.last",
            "location.city",
            "location.state",
            "location.country",
            "email",
            "dob.date"
            ],
         "nome": [
            "sexo",
            "titulo",
            "nome",
            "sobrenome",
            "cidade",
            "estado",
            "pais",
            "email",
            "data_nascimento"
         ],
         "tipos":{
             "sexo": "string",
             "titulo": "string",
             "nome": "string",
             "sobrenome": "string",
             "cidade": "string",
             "estado": "string",
             "pais": "string",
             "email": "string",
             "data_nascimento": "date"
         }
    }
}