import pytest
import pandas as pd
import tempfile
import os

from transactions_reader import read_csv_file, read_excel_file


def test_csv_basic():
    """Базовый тест чтения CSV"""

    content = "name,age\nAlice,30\nBob,25"

    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
        f.write(content)
        filepath = f.name

    try:
        result = read_csv_file(filepath)
        assert isinstance(result, pd.DataFrame)
        assert len(result) == 2
        assert list(result.columns) == ["name", "age"]
    finally:
        os.unlink(filepath)


def test_excel_basic():
    """Базовый тест чтения Excel"""

    df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})

    with tempfile.NamedTemporaryFile(mode="w", suffix=".xlsx", delete=False) as f:
        df.to_excel(f.name, index=False)
        filepath = f.name

    try:
        result = read_excel_file(filepath)
        assert isinstance(result, pd.DataFrame)
        assert len(result) == 2
    finally:
        os.unlink(filepath)


def test_file_not_found():
    """Тест ошибки для несуществующего файла"""

    with pytest.raises(FileNotFoundError):
        read_csv_file("/fake/path/file.csv")

    with pytest.raises(FileNotFoundError):
        read_excel_file("/fake/path/file.xlsx")
