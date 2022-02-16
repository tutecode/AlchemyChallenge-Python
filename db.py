# db.py
# provides a connect() function that returns a SQLAlchemy connection to the database passed to config(); sample uses config() defaults. 

from sqlalchemy import create_engine
from config import config
import logging


def connect():
    """ Connect to the PostgreSQL database server """

    try:
        # read connection params
        params = config()

        conn_string = f"postgresql://{params['username']}:{params['password']}@{params['hostname']}:{params['port']}/{params['database']}"

        # connect to PostgreSQL server
        print('Connecting...')
        engine = create_engine(conn_string)

        connection = engine.connect()
        
        ## for debug
        # result = connection.execute("select version();")
        # for row in result:
        #    print(row)
        #connection.close()

        #print('"Connected to database!"')
        logging.info('"Connected to database!"')
        return connection
    except:
        return print("Connection failed.")



# CAMBIAR ESTO????
# for debug
#if __name__ == '__main__':
#    connection = connect()
#    result = connection.execute("select version();")
#    for row in result:
#        print(row)
#    connection.close()