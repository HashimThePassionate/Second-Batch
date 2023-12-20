from typing import Callable , Tuple, Dict
# def display(a : int, b : int) -> int:
#     return a + b

# a = display(10,20)
# print(a)

# l : list[str] = ['Abdullah','Ahmed','Afaq']
# print(l)
# s = l.append('Mowahid')
# print(s)
# print(l)

# a : str = print("Pakistan") 
# # print(a)

# def re() -> str:
#     return str(22)+'Pakistan'

# z = re()
# print(z)
# print(type(z))

# a : int = len("Pakistan") # a = 8 Return

# # print(len("Pakistan"))#
# help(len)

# def add_two_numbers(num1 : int , num2 : int)->int:
#     print(f"num1 value {num1} and num 2 value {num2}")
#     return num1 + num2

# x : int = add_two_numbers(7,20)
# print(f"The sum is {x}")

# a = lambda num1, num2 : num1 + num2
# sum : Callable[[int,int],int] = lambda no1, no2 : no1 + no2 
# print(sum(2,5))
# a(7,8)

# square = lambda no : 2 * no + str(2)
# print(square('Name'))
# data : list[int] = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# d1= list(map(lambda x:x**2 , data))
# even :list[int] = list(filter(lambda x:x%2==0 ,data))
# odd :list[int] = list(filter(lambda x:x%2==1 ,data))


# print(data)
# print('--------------------')
# print(d1)
# print(even)
# print(odd)

## Generator Function
# def my_range(start:int , end:int , step: int=1):
#     for i in range(start,end+1,step):
#         yield i # Generator fucntion
# a = my_range(1,10)
# print(next(a))
# print(next(a))
# print(next(a))
# print("Hello World")
# print(next(a))
# print(next(a))
# print(next(a))
# print(10)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print("Helloe World")


# def my_range(start:int , end:int , step: int=1):
#     for i in range(start,end+1,step):
#         yield i # Generator fucntion
# a = my_range(1,10) 

# from collections.abc import Iterator

# def my_range(start:int , end:int , step: int=1)->Iterator[int]:
#     for i in range(start,end+1,step):
#         yield i # Generator fucntion


# iterator_variable = my_range(1,10)
# print(type(iterator_variable))
# print(dir(iterator_variable))
# # print(next(iterator_variable))

# def abc(*nums):
#     print(nums, type(nums))
#     total = 0
#     for n in nums:
#         total += n
#     return total


# a = abc(1,2,3,3,5,6)
# print(a)
# print('------------------------------------------------')

# def abc(*names : Tuple[str, ...]) -> None:
#     """
#     This function greets all persons in the names tuple.
#     """  
#     for name in names:
#         print("Hello", name)


# a = abc('Muhammad Mowahid','Abdullah Sobadar','Ahmed NotesWala','Ishaque Londonwala','Butt Khamoshi Wala')
# print(abc.__doc__)
# print(a)


# def greet(**greeting: Dict[str,str]) -> None:
#     print(f'Hey {greeting}')

# greet(a="Mowahid", b='Sobadar')


def my_decorator(func: Callable[[], None])-> Callable[[], None]:
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()