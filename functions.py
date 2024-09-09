# functions.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def load_data(url):
    """Carga los datos desde una URL."""
    return pd.read_excel(url)

def explore_data(df):
    """Explora el DataFrame mostrando la forma y las columnas."""
    print(f"Shape of DataFrame: {df.shape}")
    print(f"Columns in DataFrame: {df.columns}")

def analyze_missing_values(df):
    """Analiza valores faltantes en el DataFrame."""
    df_nan = df.isna().sum()
    percent = df_nan * 100 / len(df)
    missing_values = pd.DataFrame({'Missing values': df_nan, 'Missing %': percent})
    print(missing_values)
    return missing_values

def preprocess_data(df):
    """Preprocesa los datos del DataFrame."""
    df.columns = df.columns.str.strip().str.lower()
    
    # Imprimir las columnas para verificar
    print("Columnas disponibles en el DataFrame:")
    print(df.columns.tolist())
    
    # Seleccionar las columnas existentes
    columns_to_select = ['date', 'year', 'type', 'country', 'state', 'location', 'activity', 'name', 'sex', 'age', 'injury', 'unnamed: 11', 'source', 'pdf', 'href formula', 'href', 'case number', 'case number.1', 'original order']
    columns_to_select = [col for col in columns_to_select if col in df.columns]
    df = df[columns_to_select]
    
    # Eliminar columnas no relevantes
    columns_to_drop = ["state", "location", "activity", "name", "age", "injury", "source", "pdf", "href formula", "href", "case number", "case number.1", "original order", "unnamed: 21", "unnamed: 22", "time", "species"]
    columns_to_drop = [col for col in columns_to_drop if col in df.columns]
    df.drop(columns=columns_to_drop, axis=1, inplace=True)
    
    # Cambiar nombre de la columna
    df.rename(columns={'unnamed: 11': 'fatal attack: yes/no'}, inplace=True)
    
    return df

def filter_data(df):
    """Filtra y limpia los datos del DataFrame según los requisitos establecidos."""
    
    # 1. Contar el número de filas vacías en la columna 'Year'
    num_filas_vacias = df['year'].isna().sum()
    print(f"Número de filas vacías en la columna 'Year': {num_filas_vacias}")

    # 2. Eliminar filas con valores vacíos en la columna 'Year' en el DataFrame original
    df.dropna(subset=['year'], inplace=True)
    
    # Verificar el número de filas después de eliminar las vacías
    print(f"Número de filas después de eliminar las vacías: {len(df)}")

    # 3. Filtrar el DataFrame original para mantener solo los años en el rango de 1993 a 2023
    df = df[(df['year'] >= 1993) & (df['year'] <= 2023)]
    
    # Verifica el número de filas después del filtrado
    print(f"Número de filas después de filtrar: {len(df)}")

    # 4. Convertir a lista y ordenar los elementos únicos
    years_unique_sorted = sorted(df['year'].unique().tolist())
    print(years_unique_sorted)
    
    return df


def clean_sex_column(df):
    """Limpia la columna 'sex' en el DataFrame."""
    df['sex'] = df['sex'].str.strip().replace('lli', np.nan)
    df = df.dropna(subset=['sex'])
    value_counts = df['sex'].value_counts()
    print("Conteo de cada valor en la columna 'sex':")
    print(value_counts)
    return df

def analyze_attacks_by_sex(df):
    """Analiza y visualiza ataques por sexo."""
    valid_attacks = df[df['type'].isin(['Unprovoked', 'Provoked'])]
    attack_counts_by_sex = valid_attacks['sex'].value_counts()
    print("Número total de ataques por genero:")
    print(attack_counts_by_sex)
    
    total_attacks = attack_counts_by_sex.sum()
    attack_proportions = attack_counts_by_sex / total_attacks
    print("\nProporción de ataques por genero:")
    print(attack_proportions)
    
    attack_counts_df = attack_counts_by_sex.reset_index()
    attack_counts_df.columns = ['sex', 'count']
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x='sex', y='count', data=attack_counts_df, palette='coolwarm', hue='sex', dodge=False)
    plt.title('Número total de ataques por genero')
    plt.xlabel('Genero')
    plt.ylabel('Número de ataques')
    plt.show()
    
    plt.figure(figsize=(8, 8))
    plt.pie(attack_proportions, labels=attack_proportions.index, autopct='%1.1f%%', colors=sns.color_palette('coolwarm', n_colors=len(attack_proportions)))
    plt.title('Proporción de ataques por genero')
    plt.show()


def analyze_fatal_attacks(df):
    """Analiza y visualiza ataques fatales por sexo."""
    df['fatal attack: yes/no'] = df['fatal attack: yes/no'].str.upper().map({'Y': 'Yes', 'N': 'No'})
    fatal_attacks = df[df['fatal attack: yes/no'] == 'Yes']
    fatal_attacks_by_sex = fatal_attacks['sex'].value_counts()
    
    fatal_attacks_by_sex_df = fatal_attacks_by_sex.reset_index()
    fatal_attacks_by_sex_df.columns = ['sex', 'count']
    
    print("Número de ataques fatales por genero:")
    print(fatal_attacks_by_sex)
    
    total_fatal_attacks = fatal_attacks_by_sex.sum()
    fatal_attack_proportions = fatal_attacks_by_sex / total_fatal_attacks
    print("\nProporción de ataques fatales por genero:")
    print(fatal_attack_proportions)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x='sex', y='count', data=fatal_attacks_by_sex_df, palette='coolwarm', errorbar=None)
    plt.title('Número de ataques fatales por genero')
    plt.xlabel('Genero')
    plt.ylabel('Número de ataques fatales')
    plt.show()
    
    plt.figure(figsize=(8, 8))
    plt.pie(fatal_attack_proportions, labels=fatal_attack_proportions.index, autopct='%1.1f%%', colors=sns.color_palette('coolwarm', n_colors=len(fatal_attack_proportions)))
    plt.title('Proporción de ataques fatales por genero')
    plt.show()

def analyze_attacks_by_year(df):
    """Analiza y visualiza ataques por año."""
    attacks_by_year = df['year'].value_counts().sort_index()
    print("Número de ataques por año:")
    print(attacks_by_year)
    
    attacks_by_year_df = attacks_by_year.reset_index()
    attacks_by_year_df.columns = ['Year', 'Count']
    
    attacks_1994 = attacks_by_year_df[attacks_by_year_df['Year'] == 1994]['Count'].sum()
    attacks_2023 = attacks_by_year_df[attacks_by_year_df['Year'] == 2023]['Count'].sum()
    
    if attacks_1994 > 0:
        aumento_percent = ((attacks_2023 - attacks_1994) / attacks_1994) * 100
        print(f"El porcentaje de aumento en ataques de tiburones entre 1994 y 2023 es: {aumento_percent:.2f}%")
    else:
        print("No hay datos suficientes para el año 1994.")
    
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='Year', y='Count', data=attacks_by_year_df, marker='o')
    plt.title('Número de ataques por año')
    plt.xlabel('Año')
    plt.ylabel('Número de ataques')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()