# #              0        1         2
# magicians = ['Sobadar', 'Chief', 'SamonsayWala','Chief']
# magician = ('Sobadar', 'Chief', 'SamonsayWala','Chief')

# for i, n in enumerate(magicians):
#     print(i, n)
#     print('-------------------------------')
# for i, n in enumerate(magician):
#     print(i, n)

# basket : set[str] = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# print(basket)
# print(dir(basket))

# Days : set[str] = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}    
# print(Days)    
# print(type(Days))    
# print("looping through the set elements ... ")    
# for i in Days:    
#     print(i)    


# set1 = {1,2,3, "JavaTpoint", 20.5, 14}  
# print(set1)

# set1 : set[tuple,str,int] = {("Javatpoint",4),"Mowahid",1,2,3}  
# print(set1)
# set1.add("Muhammad Affaq") 
# set1.add("Saad") 
# set2 = set1.copy()
# print(set1)
# print(set2)
# set2.add(3.19)
# print(set1)
# set1 = set2.copy()
# print(set2)
# print(set1)

# set = {}
# print(type(set))

# d : dict = {
#    'zain':{
#        'RollNo':1004,
#        'FullName':'Muhammad Zain',
#        'Percentage':90.4,
#        'Course':'Python programming Language'
#    },
#    'Ahmed':{
#        'RollNo':1005,
#        'FullName':'Ahmed Raheem',
#        'Percentage':98.9,
#        'Course':'Full Stack Python Developer'
#    }

# }
# for i in d:
#     print(d[i])
# # print(d['Ahmed'])
# # print(dir(d))
# a = [i for i in dir(d) if "__" not in i]
# print(a)

# for i in d:
#     for j in i:
#         print(j)
    
# Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}    
# for x in Employee.values():    
#     print(x) 


# people = {
#        "John":
#         {'Name': 'John', 
#          'Age': '27',
#          'Sex': 'Male'},
#         "Marie": 
#         {'Name': 'Marie', 
#          'Age': '22', 
#          'Sex': 'Female'}  
#           }

# for key, values in people.items():
#     print("\nPerson ID:", key)
#     print('-----------------------------')
#     for k in values:
#         print(k + ' = ', values[k])


# print(people['John']['Name'])
# course : dict[str] = {

#     'title':'Programming',
#     'instructor':{
#         'name':'Umer',
#         'mail':'umer@gmail.com'
#     },
#     'students':{
#         1:{'name':'peter'
#            ,'age':11},
#         2:{'name':'james'
#            ,'age':12},
#         3:{'name':'Emma'
#            ,'age':10},
#     },
#     'modality':'online'
# } 

# print(course)

# Example 1
# def dict_walk(d):
#     for k, v in d.items():
#         if type(v) == dict:   # option 1 with “type()”
#         #if isinstance(v, dict):   # option 2 with “isinstance()”
#             print(k)   # this line is for printing each nested key 
#             dict_walk(v)
#         else:
#             print(k, ': ', v)
  
# dict_walk(course)
#https://pythontutor.com/render.html#mode=edit