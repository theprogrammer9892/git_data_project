import pandas as pd


def limpiar_ventas(df):
    df = df.dropna()
    df.columns = df.columns.str.lower().str.strip()
    return df
