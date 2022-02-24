import pandas as pd
import logging

## Logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('logs.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

def create_df_registros(df_cultural):

    # Categoria
    df_categoria = df_cultural.groupby(['Categoria']).size().reset_index(name='Total')      
    logger.info(f"Cantidad de registros totales por 'Categoria': \n\n{df_categoria}\n")
    
    # Fuentes
    df_fuentes = df_cultural.groupby(['Fuente']).size().reset_index(name='Total')
    logger.info(f"Cantidad de registros totales por 'Fuente': \n\n{df_fuentes}\n")
    
    # Provincia y Categorias
    df_prov_categ = df_cultural.groupby(['Provincia', 'Categoria']).size().reset_index(name='Total')
    logger.info(f"Cantidad de registros totales por 'Provincia' y 'Categoria': \n\n{df_prov_categ}\n")
    
    # Total Registros
    df_registros = pd.concat([df_categoria, df_fuentes, df_prov_categ], axis = 1)
    logger.info(f"Cantidad de registros totales: \n\n{df_registros}\n")

    return df_registros