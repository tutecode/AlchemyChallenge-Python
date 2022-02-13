import pathlib
import requests
import csv
from datetime import datetime

def download_data(category, url):
    url = url
    response = requests.get(url)

    # current date
    now = datetime.now() 
    year_month = now.strftime("%Y-%b") # year-month    
    date = now.strftime("%m-%d-%Y") # month-day-year
    
    # make directory
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