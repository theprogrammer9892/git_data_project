import pandas as pd


def limpiar_ventas(df):
    df.columns = df.columns.str.lower().str.strip()

    columnas_requeridas = ["producto", "cantidad", "precio", "fecha_venta"]

    columnas_faltantes = [col for col in columnas_requeridas if col not in df.columns]

    if columnas_faltantes:
        raise ValueError(f"Faltan columnas requeridas: {columnas_faltantes}")

    df = df.dropna()
    return df
