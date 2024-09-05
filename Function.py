def read_data(ruta_archivo):
    """ 
    lee la data
    parametros=a ruta de archivos
    return= df que contiene esos archivos
    """
    import pandas as pd 
    df = pd.read_excel(ruta_archivo)
    return df

def isna(df):
    """
    Nos devuelve el porcentaje
    return = df_nan la variable
    """
    df_nan = df.isna().sum()
    percent = df_nan * 100 / len(df)
    missing_values = pd.DataFrame({'Missing values': df_nan, 'Missing %': percent})
    return missing_values
