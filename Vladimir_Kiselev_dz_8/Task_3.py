# Task_3 
from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(args):
        val_type = type(args)
        return f'{calc_cube.__name__} ({args}: {val_type})'
    return wrapper


@ type_logger
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
print(a)