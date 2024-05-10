"Script de ingestão treinamento DPH"

import pandas as pd
import requests
import utils
import os
from dotenv import load_dotenv
from config import configs
import logging

load_dotenv()
config_file = configs
logging.basicConfig(level=logging.INFO)


def ingestion():
    """
    Função de ingestão dos dados
    Outputs: Salva base raw em local específico e retorna o nome do arquivo
    """

    logging.info("Iniciando a ingestão")
    api_url = os.getenv('URL')
    try:
        response = requests.get(api_url, timeout=10).json()
        data = response['results']
    except Exception as exception_error:
        utils.error_handler(exception_error, 'read_api', configs['path']['logs'])
    df = pd.json_normalize(data)
    utils.save_folder(df, configs['path']['raw'])
    

def preparation():
    """
    Função de preparação dos dados: renomeia, tipagem, normaliza strings
    Arguments: file -> nome do arquivo raw
    Outputs: Salva base limpa em local específico
    """

    logging.info("Iniciando o saneamento")
    file = f"{configs['path']['raw']}"
    df = pd.read_csv(file, sep=";")
    san = utils.Saneamento(df, config_file)
    san.select_rename()
    logging.info("Seleção de dados")
    df = san.tipagem()
    logging.info("Tipagem dos dados")
    utils.save_folder(df, configs['path']['work'])
    logging.info("Dados salvos na work")
    

if __name__ == '__main__':
    ingestion()
    preparation()