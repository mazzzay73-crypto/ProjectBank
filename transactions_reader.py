import pandas as pd
import os


def get_project_root() -> str:
    """Возвращает корневую директорию проекта"""

    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    return project_root


def read_csv_file(filepath: str = None) -> pd.DataFrame:
    """Читает данные из CSV файла"""

    if filepath is None:
        project_root = get_project_root()
        filepath = os.path.join(project_root, "data", "transactions.csv")

    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File {filepath} not found")

    return pd.read_csv(filepath)


def read_excel_file(filepath: str = None) -> pd.DataFrame:
    """Читает данные из Excel файла"""

    if filepath is None:
        project_root = get_project_root()
        filepath = os.path.join(project_root, "data", "transactions_excel.xlsx")

    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File {filepath} not found")

    return pd.read_excel(filepath)
