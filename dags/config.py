import os
from datetime import datetime

configs = {
    "URL": "https://randomuser.me/api/?results=3",
    "metadados":{
        "nome_original": [
            "gender",
            "name_title",
            "name_first",
            "name_last",
            "location_city",
            "location_state",
            "location_country",
            "email",
            "dob_date"
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