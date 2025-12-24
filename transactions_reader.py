import pandas as pd
import os


def read_csv_file(filepath: str) -> pd.DataFrame:
    """Читает данные из CSV файла"""
    if filepath is None:
        filepath = r"C:\Users\User\PycharmProjects\ProjectBank\transactions.csv"
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File {filepath} not found")

    return pd.read_csv(filepath)


def read_excel_file(filepath: str) -> pd.DataFrame:
    """Читает данные из Excel файла"""
    if filepath is None:
        filepath = r"C:\Users\User\PycharmProjects\ProjectBank\transactions_excel.xlsx"
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File {filepath} not found")

    return pd.read_excel(filepath)
