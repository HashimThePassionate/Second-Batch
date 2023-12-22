# def avg(scores):    
#     assert len(scores) != 0,"The List is empty."    
#     return sum(scores)/len(scores)    
# scores2 = [67,59,86,75,92]    
# print("The Average of scores2:",avg(scores2))    
# scores1 = []    
# print("The Average of scores1:",avg(scores1))   

# def square_root( Number ):  
#     assert ( Number < 0), "Give a positive integer"  
#     return Number**(1/2)  
  
# #Calling function and passing the values  
# print( square_root(-36))  
# print( square_root(36)) 

a : list[str] = ["A","B","C"]
# a  : list = "usman"
# print(a)
# a  : list = "USMAN"
# print(a)

# print(a[3])
# try:
#     print(a[3])
# except IndexError:
#     print("Index does not assign")

# a = ["Python", "Exceptions", "try and except"]  
# try:  
#     #looping through the elements of the array a, choosing a range that goes beyond the length of the array  
#      for i in range( 4 ):  
#         print( "The index and element from the array is", i, a[i] )  
# #if an error occurs in the try block, then except block will be executed by the Python interpreter       
# except:  
#     print ("Index out of range")  


# def reciprocal( num1 ):  
#     try:  
#         reci = 1 / num1  
#     except ZeroDivisionError:  
#         print( "We cannot divide by zero" )  
#     else:  
#         print ( reci )  
# Calling the function and passing values  
# reciprocal( 4 )  
# reciprocal( 0 )

# class SobadarError(Exception):
#     def __str__(self) -> str:
#         return "We cannot divide by zero"
    
# def rep(value : int ) -> int:
#     if value==0:
#         raise SobadarError()
#     return 1 / value 

# a : int = rep(10)
# b : int = rep(0)
# print(a)
# print(b)

# def dynamic_error_handling(value:int) -> int:
#     try:
#         return [i**2 for i in value]
#     except Exception as e:
#         print(f"An error occurred: str({e})")
#         return 0

class NotFound(Exception):
    def __str__(self) -> str:
        return "This username is not found in DB"
    
def check(value : str) -> str:
    # student : list = {'M': 'mowahid', 'A': 'abdullah', 'R': 'raheem', 'N': 'nadia', 'B': 'butt', 'M': 'maaz'}
    student : list = ['mowahid','ahmed','nadia','abdullah']
    for i in student:
        if i == value:
            return value
    raise NotFound() 
    
name : str = input("Please Enter Your Name!")
string : str = check(name)
print(f'Username {string} is found in Database')


# a : list = dynamic_error_handling([1,2,3,4,5,6,7,9])
# print(a)

