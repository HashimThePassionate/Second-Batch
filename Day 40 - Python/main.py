# https://github.com/HashimThePassionate/Python-For-Absolute-Beginners/blob/main/23-Classes.py

# class Parent():
#     def __init__(self) -> None:
#         self.color = "Brown"
#         self.eyeColor = "Green"

#     def speak(self, words: str)->None:
#         print(f"Parent method speak: {words}")

#     def watching(self, object_name : str)->None:
#         print(f"You are looking {object_name}!")


# class child(Parent):
#     pass

# obj1 : Parent = Parent()
# print(obj1.eyeColor)
# print(obj1.color)
# obj1.speak("Pakistan zinda bad!")
# obj1.watching("TV")

# print("======Child object=======")
# ### Child object 

# obj2 : child = child()
# obj2.watching("Cenima")
# obj2.speak("Hello World")
# print(obj2.eyeColor)
# print(obj2.color)


# class ACI:
#     institute : str = "Azad Chaiwala Institute"
#     working_hours : str = "8 ' Clock "
#     dress_code : str = "Formal Dress"
#     courses :  str = "Technical"
#     working_days : str = "5 days"

#     def __init__(self, name : str, salary: str, education : str, post : str) -> None:
#         self.employee_name : str  = name
#         self.employee_salary : str  = salary
#         self.employee_education : str = education
#         self.employee_post : str = post


#     def __str__(self) -> str:
#         return f"""
#                 ------------------------------------------------
#                 Employee Institute is : {ACI.institute}
#                 Employee Working Hours is : {ACI.working_hours}
#                 Employee Dress Code is : {ACI.dress_code}
#                 Employee Courses is : {ACI.courses}
#                 Employee Working days is : {ACI.working_days}
#                 Employee Name is : {self.employee_name}
#                 Employee Salary is : {self.employee_salary} pkr
#                 Employee Education is : {self.employee_education}
#                 Employee post is : {self.employee_post}
               
# """


# class Employee(ACI):
#     def __init__(self, name: str, salary: str, education: str, post: str,bonus: str) -> None:
#         super().__init__(name, salary, education, post)
#         self.bonus = bonus
    
#     def __str__(self) -> str:
#         return super().__str__() + f"""Bonus is {self.bonus}
    
#          ---------------------------------------------
# """

# employee1 : Employee = Employee("Muhammad Hashim","150000","BSCS","Junior Python Trainer","25000")
# employee2 : Employee = Employee("Abdullah Khokhar","1500000","BSCS","Senior Full Python Trainer","15000")

# print(employee1)
# print(employee2)

# employee1 : Employee = Employee()


# from typing import Union, overload

# class Adder:
#     @overload
#     def add(self, x: int, y: int) -> int:
#         ...
        
#     @overload
#     def add(self, x: float, y: float) -> float:
#         ...
        
#     @overload
#     def add(self, x: str, y: str) -> str:
#         ...
        
    
#     def add(self, x: Union[int, float, str], y: Union[int, float, str]) -> Union[int, float, str]:
#         if isinstance(x, int) and isinstance(y, int):
#             return x + y
#         elif isinstance(x, float) and isinstance(y, float):
#             return x + y
#         elif isinstance(x, str) and isinstance(y, str):
#             return x + y
#         else:
#             raise TypeError("Invalid argument types!")

# # Usage examples
# adder = Adder()
# result1 = adder.add(1, 2)  # Should return 3
# result4 = adder.add(1, 2.3)  # return Error
# result2 = adder.add(1.5, 2.5)  # Should return 4.0
# result3 = adder.add("Hello, ", "world!")  # Should return "Hello, world!"
# result5 = adder.add(1, "world!")  # Error

# print(result1)
# print(result2)
# print(result3)
# print(result4)
# print(result5)


class Animal():
    def eating(self,food : str )->None: #same method 
        print(f"Animal is eating {food}")


class Bird(Animal):
    def eating(self, food: str) -> None:
        # super().eating("Bread")
        print(f"Bird is eating {food}")


# bird : Bird = Bird()
# bird.eating("bread")
# # print(type(bird))

# animal : Animal = Animal()
# animal.eating("grass")
# # print(type(animal))

# parrot : Bird = Animal()
# print(type(parrot))
# parrot.eating("grass")
        
# animal : Animal = Bird()# run time it will decide which object method it will be run
# animal.eating("grass")
        

class MathOperations:

    counter : int = 100
    organization : str = "PIAIC"

    @staticmethod
    def add(x: int, y: int) -> int:
        """Add two numbers."""
        return x + y

    @staticmethod
    def multiply(x: int, y: int) -> int:
        """Multiply two numbers."""
        return x * y

# Using the static methods

print("Addition:", MathOperations.add(10, 20))
print("Multiplication:", MathOperations.multiply(10, 20))

print("Static variable or Class variable",MathOperations.organization)