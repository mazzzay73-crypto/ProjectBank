from time import time


def log(filename: Optional[str] = None, print_time: bool = True):
    """Декоратор для логирования функций"""
    def decorator(func):
        """Обертка для функции"""
        def wrapper(*args, **kwargs):
            """"Функция с логированием"""
            func_name = func.__name__

            if filename:
                with open(filename, 'a', encoding='utf-8') as f:
                    f.write(f"{func_name} started\n")
            else:
                print(f"{func_name} started")

            try:
                start_time = time()
                result = func(*args, **kwargs)
                end_time = time()
                duration = end_time - start_time

                success_msg = f"{func_name} ok"

                if print_time:
                    time_msg = f"Time for work: {duration:.4f}"
                    if filename:
                        with open(filename, 'a', encoding='utf-8') as f:
                            f.write(time_msg + '\n')
                    else:
                        print(time_msg)

                if filename:
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.write(success_msg + '\n')
                else:
                    print(success_msg)

                return result

            except Exception as e:
                """Обработка ошибок"""
                error_msg = f"[{func_name}] error: {type(e).__name__}. Inputs: {args}, {kwargs}"

                if filename:
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.write(error_msg + '\n')
                else:
                    print(error_msg)

                raise

        return wrapper

    return decorator


@log()
def function_with_exception(x, y=0):
    """Функция, которая вызывает исключение"""
    raise ValueError("Test error")


@log()
def my_function(x, y):
    """Функция суммирует два числа"""
    return x + y


@log(filename="test_log.txt")
def logged_to_file_function(x):
    """Функция с логированием в файл"""
    return x * 2
