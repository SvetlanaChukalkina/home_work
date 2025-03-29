def log(filename=None):
    """Автоматически логирует начало и конец выполнения функции, ее результаты или возникшие ошибки"""
    def wrapper(func):
        def inner(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                message = f'{func.__name__} ok'
                if filename != None:
                    with open(filename, "a") as file:
                        file.write(message + "\n")
                else:
                    print(message)
                return result

            except Exception as error:
                result = None
                message = f'{func.__name__} error: {error}. Inputs: {args}, {kwargs}'
                if filename != None:
                    with open(filename, "a") as file:
                        file.write(message + "\n")
                else:
                    print(message)
                return result
        return inner
    return wrapper


@log(filename="logs.txt")
def my_function(x, y):
    return x / y
my_function(2,1.5)