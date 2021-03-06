
def arithmetic(value1: int, value2: int, operation: str) -> int | float | str:
    """Summerize, subtract, multiply, divide values"""
    if operation == '+':
        result = value1 + value2
    elif operation == '-':
        result = value1 - value2
    elif operation == '*':
        result = value1*value2
    elif operation == '/':
        result = value1/value2
    else:
        result = f"Not known operation {operation}"

    return result


if __name__ == '__main__':
    print(arithmetic(3, 4, '+'))
