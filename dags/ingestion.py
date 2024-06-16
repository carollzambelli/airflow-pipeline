"Script de ingestão treinamento DPH"

import pandas as pd
import requests
import utils as utils
from dotenv import load_dotenv
from config import configs

config_file = configs

def ingestion():
    """
    Função de ingestão dos dados
    Outputs: Salva base raw em local específico e retorna o nome do arquivo
    """
    api_url = configs["URL"]
    try:
        response = requests.get(api_url, timeout=10).json()
        data = response['results']
    except Exception as exception_error:
        utils.error_handler(exception_error, 'read_api', configs['path']['logs'])
    df = pd.json_normalize(data)
    cols = [s.replace('.', '_') for s in df.columns]
    df.columns = cols
    return df
    

def preparation():
    """
    Função de preparação dos dados: renomeia, tipagem, normaliza strings
    Arguments: file -> nome do arquivo raw
    Outputs: Salva base limpa em local específico
    """

    df = utils.read_mysql("mysql", "cadastro_raw")
    san = utils.Saneamento(df, config_file)
    san.select_rename()
    df = san.tipagem()
    return df
    

if __name__ == '__main__':
    ingestion()
    preparation()