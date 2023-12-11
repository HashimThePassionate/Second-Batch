name ="Muhammad Hashim" #Beginner level code
name : str = "Muhammad hashim" # Professional Code
print("In python Everything is Object")
print("Every Object contain Attributes and Methods")
print(name)
print(id(name))
print(dir(name))
print(name.upper())
print(name.title())

age : int = 24
print(age)
print(id(age))
print(type(age))
print(dir(age))

#Naming Convention
#Single letter lowercase
a : int = 10
print("Single letter lowercase")
print(a)
#Single letter Uppercase
A : int = 20
print("Single letter Uppercase")
print(A)

#lowercase
percentage : float = 88.7
print("lowercase")
print(percentage)
#Uppercase
PERCENTAGE : float = 90.99
print("Uppercase")
print(PERCENTAGE) 

#lower_case_with_underscores
my_age_is : int = 24
print("lower_case_with_underscores")
print(my_age_is)
#UPPER_CASE_WITH_UNDERSCORES
MY_AGE_IS : int = 24
print("UPPER_CASE_WITH_UNDERSCORES")
print(MY_AGE_IS)


#CapWords, or CamelCase
myAgeIs : int = 24
print("Camel Case")
print(myAgeIs)
MyAgeIs : int = 24
print("CapWords")
print(MyAgeIs)

deximal : float = 25.2358784848468484
print(deximal)
print(round(deximal,10))


nickName : str = "Muhammad Hashim"
#Comma Operator
print("My name is :",nickName)
#plus Operator Concetenation 
print("My name is : "+nickName)
print(f"My Nickname is {nickName}")
print(f'My Nickname is "{nickName}"')
print(f"My Nickname is \"{nickName}\"")

print("My name is %s and my age is %d"%(nickName,age))
print("My age is {} and my name is {}".format(age,name.title()))


pi: float = 3.14159
print(pi)
print(f"Value of pi to 2 decimal places: {pi:.2f}")