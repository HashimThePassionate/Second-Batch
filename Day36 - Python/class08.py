# Call by Value
# a : int = 5
# def abc(num : int ) -> None:
#     num = 6
#     print(id(num))
#     print(num)

# print(id(a))
# abc(a)
# print(a)

# Call by Reference
# l : list = [1,2,3,4,5]
# def myList(newList : list[int]) -> None:
#     print(newList)
#     print(id(newList))
#     newList.append(6)

# print(id(l))
# myList(l)
# print(l)


# a = int(input("Please Enter a Number\t"))
# b = int(input("Please Enter another Number\t"))

# res : int = (a/b)
# print(f"Value is {res}")


# a : int = 1
# while(True):
#     print(a)
#     a += a

# l: list[int] = [1,2,3]
# try:
#     # a = int(input("Please Enter a Number\t"))
#     # b = int(input("Please Enter another Number\t"))
#     # print(a/b)
#     print(k[3])
# except ZeroDivisionError:
#     print("You cannot Divide any number with zero")
# except IndexError:
#     print('List does not contain that index number')
# except NameError:
#     print('Variable name is not valid')
#     # pass


# Raising an Exception
# x : int = 10
# if x > 5:
#     raise Exception(f'x should not exceed 5. The value of x was: {x}')

# num = [3, 4, 5, 7]  
# if len(num) > 3:  
#     raise Exception( f"Length of the given list must be less than or equal to 3 but is {len(num)}" ) 

# Assertion Exception
def square_root( Number : int ) -> int:  
    assert ( Number < 0), "Give a positive number"
    return Number**(1/2)  
  
#Calling function and passing the values  
no1 : int = square_root(-36)
no2 : int = square_root(36)
print(no1)  
# print(no2) 


