from typing import Any


def log(filename: Any = None) -> Any:
    """Автоматически логирует начало и конец выполнения функции, ее результаты или возникшие ошибки"""

    def wrapper(func: Any) -> Any:
        def inner(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
                if filename is not None:
                    with open(filename, "a") as file:
                        file.write(message + "\n")
                else:
                    print(message)
                return result

            except Exception as error:
                result = None
                message = f"{func.__name__} error: {error}. Inputs: {args}, {kwargs}"
                if filename is not None:
                    with open(filename, "a") as file:
                        file.write(message + "\n")
                else:
                    print(message)
                return result

        return inner

    return wrapper
