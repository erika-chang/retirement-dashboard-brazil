import os
import requests
from datetime import datetime

DATA_FILES = [("https://www.bcb.gov.br/conteudo/depes/ArquivosAposentados/Aposentadorias_BCB_RJU.csv", "aposentados.csv"),
              ("https://www.bcb.gov.br/conteudo/depes/ArquivosAposentados/Aposentadorias_BCB_RJU_Fundamenta%C3%A7%C3%B5es.csv", "fundamentacao.csv"),
              ("https://www.bcb.gov.br/conteudo/depes/ArquivosAposentados/Aposentadorias_BCB_RJU_Classes.csv", "classes.csv")]
SAVE_DIR = "data/raw"

def download_data(url, save_path):
    print(f'Downloading data from {url}...')
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f'Data downloaded and saved to {save_path}')
    else:
        print(f'Failed to download data. Status code: {response.status_code}')

def check_date_file(file_path, days_valid=30): # Check if the file is less than 30 days old
    if os.path.exists(file_path):
        file_mod_time = os.path.getmtime(file_path)
        file_age = (datetime.now().timestamp() - file_mod_time) / (24 * 3600)
        return file_age < days_valid
    return False

def main():
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)

for url, filename in DATA_FILES:
        save_path = os.path.join(SAVE_DIR, filename)
        if check_date_file(save_path):
            print(f"{filename} is already fresh. Skipping.")
            print(f"Last modified: {datetime.fromtimestamp(os.path.getmtime(save_path))}")
        else:
            download_data(url, save_path)

if __name__ == "__main__":
    main()
