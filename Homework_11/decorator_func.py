def print_file_name_func(function) -> str:
    """Print name of the callable file plus ariphm operation"""
    def decoratee(a, b):
        return function.__name__, function(a, b)

    return decoratee


@print_file_name_func
def sum_elements(a: int, b: int) -> int:
    """Summarize two elements"""
    return a + b


@print_file_name_func
def mult_elements(a: int, b: int) -> int:
    """Multiply two elements"""
    return a * b


print(sum_elements(3, 9))
print(mult_elements(3, 10))
