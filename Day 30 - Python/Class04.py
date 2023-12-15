# number : int = int(input("Please Enter Your Number: "))
# if number == 2:
#     print(f"You Enter {number}")
#     print("Number Two")
# else:
#     print(f"Number is not 2 it is {number}")
# print("It is a normal statement")



# age : int = int (input("Enter your age? "))  
# if age>=18:  
#     print("You are eligible to vote !!");  
# else:  
#     print("Sorry! you have to wait !!")

 
# def http_error(status):
#     match status:
#         case 400:
#             return "Bad request"
#         case 404:
#             return "Not found"
#         case 418:
#             return "I'm a teapot"
#         case _:
#             return "Something's wrong with the internet"


# print(http_error(600))

# print(range(15))    
# print(list(range(15)))    
# print(list(range(4, 9)))    
# print(list(range(5, 25, 3 ))) 

# name : str = "Muhammad Hashim"
# # print(name[7])
# # name[7] = "D"
# # print(name[7])
# for i in name:
#     print(i,end="")


# names : list[str] = ['Hashim', 'Farooq', 'Hamza', 'Usman', 'Madiha']
# print(type(names))
# print(dir(names))


# for i in range(len(names)):
#     print(i,names[i],len(names[i]))


# rows = int(input("Enter number of rows: "))
# for i in range(rows):
#     for j in range(i+1): 
#         print("* ", end="")
#     print("\n")

# n=5
# s=1
# summation=0
# while s<=n:
#     summation = summation + s**2
#     s+=1
# print("The sum of squares is", summation)  

# num = 5        
# counter = 1      
# # we will use a while loop for iterating 10 times for the 
# # multiplication table        
# print("The Multiplication Table of: ", num)      
# while counter <= 10: # specifying the condition  
#     ans = num * counter      
#     print (f"{num} x {counter} = {ans}")      
#     counter += 1 # expression to increment the counter


n=2  
while 1:  
    i=1;  
    while i<=10:  
        print("%d X %d = %d\n"%(n,i,n*i))  
        i = i+1;  
    choice = int(input("Do you want to continue printing the table, press 0 for no?"))  
    if choice == 0:  
        break    
    n=n+1 