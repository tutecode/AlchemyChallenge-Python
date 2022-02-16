from download_data import download_data
from db import connect


## 1. Download data
download_data('museos', 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museo.csv')
download_data('cines', 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv')
download_data('bibliotecas', 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv')

## 2. Connect to database
connect()











# 2. Create tables
#import psycopg2

#conn = psycopg2.connect("dbname=gov_db user=postgres password=postgres")

#conn = psycopg2.connect(
#    host="localhost",
#    database="gov_db",
#    user="postgres",
#    password="password")

#import psycopg2
#from config.config import config
## Import libraries
#
##import pandas as pd
#import psycopg2
#from config.config import config
## Connect to PostgreSQL
#params = config(config_db = 'database.ini')
#engine = psycopg2.connect(**params)
#print('Python connected to PostgreSQL!')
#
#
#
#def connect():
#    """ Connect to the PostgreSQL database server """
#    conn = None
#    try:
#        # read connection parameters
#        params = config()
#
#        # connect to the PostgreSQL server
#        print('Connecting to the PostgreSQL database...')
#        conn = psycopg2.connect(**params)
#		
#        # create a cursor
#        cur = conn.cursor()
#        
#	# execute a statement
#        print('PostgreSQL database version:')
#        cur.execute('SELECT version()')
#
#        # display the PostgreSQL database server version
#        db_version = cur.fetchone()
#        print(db_version)
#       
#	# close the communication with the PostgreSQL
#        cur.close()
#    except (Exception, psycopg2.DatabaseError) as error:
#        print(error)
#    finally:
#        if conn is not None:
#            conn.close()
#            print('Database connection closed.')
#
#
#if __name__ == '__main__':
#    connect()
#
#
#