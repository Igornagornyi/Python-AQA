import os


path = '/home/igor/Desktop/Python-AQA/'


def os_walk(path: str) -> tuple[dir]:
    """Show all folders and files of the path"""
    tree = os.walk(path)
    for i in tree:
        print(i)


hh = os_walk(path)
print(hh)
