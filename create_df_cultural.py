import pandas as pd
import logging

## Logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('logs.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

# create df_cultural
def create_df_cultural(df_museos, df_cines, df_bibliotecas):
    
    # rename df_museos columns
    df_museos = df_museos.drop(['Observaciones', 'subcategoria', 'piso', 
        'cod_area', 'Latitud', 'Longitud', 'TipoLatitudLongitud',
        'Info_adicional', 'jurisdiccion', 'año_inauguracion',
        'IDSInCA'], axis=1)

    df_museos.columns = ['Cod_Loc', 'Id_Provincia', 'Id_Departamento', 'Categoria', 
        'Provincia', 'Localidad', 'Nombre', 'Domicilio', 'Cod_Postal', 'Telefono', 'Mail', 'Web', 'Fuente']

    # rename df_cines columns
    df_cines = df_cines.drop(['Observaciones', 'Piso', "Departamento",
        'cod_area', 'Latitud', 'Longitud', 'TipoLatitudLongitud',
        'Información adicional', 'Latitud', 'Longitud', 'TipoLatitudLongitud',
        'tipo_gestion', 'Pantallas', 'Butacas', 'espacio_INCAA',
        'año_actualizacion'], axis=1)

    df_cines.columns = ['Cod_Loc', 'Id_Provincia', 'Id_Departamento', 'Categoria', 
        'Provincia', 'Localidad', 'Nombre', 'Domicilio', 'Cod_Postal', 'Telefono', 'Mail', 'Web', 'Fuente']

    # rename df_bibliotecas columns
    df_bibliotecas = df_bibliotecas.drop(['Observacion', 'Subcategoria', 'Piso', "Departamento",
        'Información adicional', 'Latitud', 'Longitud', 'TipoLatitudLongitud', 'Cod_tel',
        'Tipo_gestion', 'año_inicio',
        'Año_actualizacion'], axis=1)

    df_bibliotecas.columns = ['Cod_Loc', 'Id_Provincia', 'Id_Departamento', 'Categoria', 
        'Provincia', 'Localidad', 'Nombre', 'Domicilio', 'Cod_Postal', 'Telefono', 'Mail', 'Web', 'Fuente']

    ## concat dataframes in 1 dataframe (table)
    df_cultural = pd.concat([df_museos, df_cines, df_bibliotecas])
    #df_cultural.to_csv('cultural.csv')

    logger.info('DataFrame Cultural was created!')

    return df_cultural