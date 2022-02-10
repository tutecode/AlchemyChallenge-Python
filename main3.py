import pathlib
import requests
import csv
from datetime import datetime
import os

var = 'museos'
pathlib.Path(f'data/{var}').mkdir(parents=True, exist_ok=True) 

def download_data(category, url):
    url = url
    response = requests.get(url)

    # current date
    now = datetime.now() 
    year_month = now.strftime("%Y-%b") # year-month    
    date = now.strftime("%m-%d-%Y") # month-day-year
    
    pathlib.Path(f"data/{category}/{year_month}").mkdir(parents=True, exist_ok=True) 

    if(category == 'museos'):
        with open(f'data/{category}/{year_month}/{category}-{date}.csv', 'w') as f:
            writer = csv.writer(f)
            for line in response.iter_lines():
                writer.writerow(line.decode('utf-8').split(','))

    if(category == 'cines'):
        with open(f'data/{category}/{year_month}/{category}-{date}.csv', 'w') as f:
            writer = csv.writer(f)
            for line in response.iter_lines():
                writer.writerow(line.decode('utf-8').split(','))

    if(category == 'bibliotecas'):
        with open(f'data/{category}/{year_month}/{category}-{date}.csv', 'w') as f:
            writer = csv.writer(f)
            for line in response.iter_lines():
                writer.writerow(line.decode('utf-8').split(','))


download_data('museos', 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museo.csv')
download_data('cines', 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv')
download_data('bibliotecas', 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv')
