from typing import Any 
# name : list[Any] = ['Ahmed Raheem','Ishaque Sahb','Abdullah Bro','Nadia COAS','Maaz Taxila Wala','Annie CDN']
# print(name)
# name[2] = 'Soobedar Abdullah'
# name[0]=' Ahmed Notes'
# print(name)
# name[1]= 'Ishaque Galib Qalandry'
# print(name)
# name[4] = 'Maaz Music wala'
# print(name)

# numbers = [3, 5, 1, 7, 3, 9]  
# num = []  
# for n in numbers:  
#     num.append(n+6)  
# print(numbers)
# print(num)  
# print('----------------------------------------------------')
# a = [n+6 for n in numbers]
# print(a)

# # tuple : tuple[int] = (1,2,3,4,5)
# l: list[Any] = ["Ishaque",(1,2,3,4,5),10]
# print(l)

# t : tuple = 1,2
# print(type(t))
# t1 : tuple = ()
# print(type(t1))
# name : tuple = ('MyName',)
# print(type(name))
# print(t[0])
# t[0] = 3
# # print(t)

tuple1 = tuple(input("Enter the tuple elements ..."))  
print(tuple1)    
count = 0    
for i in tuple1:    
    print("tuple1[%d] = %s"%(count, i))   
    count = count+1  

    