import pytest
import os

from src.decorators import function_with_exception, my_function, logged_to_file_function


def test_successful_execution_output(capsys):
    """Тест вывода в консоль при успешном выполнении"""
    result = my_function(5, 3)
    assert result == 8
    captured = capsys.readouterr()
    output = captured.out

    assert "my_function ok" in output


def test_exception_execution_output(capsys):
    """Тест вывода в консоль при возникновении исключения"""
    with pytest.raises(ValueError):
        function_with_exception(5, 3)

    captured = capsys.readouterr()
    output = captured.out

    assert "[function_with_exception] error: ValueError" in output
    assert "Inputs: (5, 3), {}" in output or "Inputs: (5, 3)," in output


def test_file_output():
    """Тест сохранения логов в файл"""
    if os.path.exists("test_log.txt"):
        os.remove("test_log.txt")

    result = logged_to_file_function(5)
    assert result == 10

    assert os.path.exists("test_log.txt")

    with open("test_log.txt", "r", encoding="utf-8") as f:
        content = f.read()

    assert "logged_to_file_function started" in content
    assert "Time for work:" in content
    assert "logged_to_file_function ok" in content

    os.remove("test_log.txt")
