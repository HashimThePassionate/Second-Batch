def square(myList:list) -> list:
    return [i**2 for i in myList]


def info(**what:dict):
    for key, value in what.items():
        print(f"{key} is {value}")

def add(a : int, b: int) ->int:
    return a+b




