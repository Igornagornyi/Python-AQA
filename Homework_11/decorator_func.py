def print_func(function):
    def decoratee(a, b):
        return f"{function.__name__} {function(a, b)}"

    return decoratee


@print_func
def sum_arg(a: int, b: int) -> int:
    return a + b


@print_func
def subtract_arg(a: int, b: int) -> int:
    return a - b


print(sum_arg(3, 9))
print(subtract_arg(3, 10))
