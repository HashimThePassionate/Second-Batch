# name : str = "Muhammad Butt"
# name : str = 'Muhammad Butt'
# name : str = '''
# My name is Muhammad Butt
# i am studying python
# Programming
# '''
# print(len(name))
# print(name.len())
# name : str = """
# My name is Muhammad Butt
# i am studying python
# Programming"""
# name : str = """
# My name is Muhammad Butt
# i am studying python
# ProgramminG
# """
# len : int = name.__len__()
# print(len)
# # name[-1] = 'G'
# print(dir(name))
# print() 
#Help
# * help(object)
# * object?
# * object?? 
# * ?object
# * ?? 
# print(help(name.rfind))
# ch : int = name.rfind("G")
# print(ch)
# check : bool = name.endswith('ProgramminG',0,58)
# print(check)

# print('C:\some\name')
# print(r'C:\Users\aaaa\Desktop\Batches\Python Full Stack Journey\PythonBatch2\PythonBatch2\Day 31 - Python\Class04.py')
# print(10 * 'un' + 'ium')

# student : list[str,int] = ["Umer",800,"Butt",850,"Mowahid",950]
# # print(type(student))
# # print(id(student))
# # # print(dir(student))
# # # help(student.__reversed__)
# # print(student)
# # student.reverse()
# # print(student[0])
# # a : int = 2
# # b : int = 2
# # print(id(a))
# # print(id(b))
# # print(a is b)
# a : list[int,str,float] = [1,2,"Peter",4.50,"Ricky",5,6]  
# b : list[int,str,float] = [1,2,"Peter",4.50,"Ricky",5,7]  
# print(a is b)
# print(id(a))
# print(id(b))
# print(a == b)
# print("-------------------------")
# b = a
# print(a is b)
# print(id(a))
# print(id(b))
# square : list[int] = [1,2,9,16,25]
# print(square)
# square += [36,49,64,81,100]
# print(square)
# square[1]=4
# print(square)
a : list[str] = ['a', 'b', 'c']
n : list[int] = [1, 2, 3]
x : list[list[str],list[int]] = [a, n]
# x = [ ['a', 'b', 'c'], [1, 2, 3] ]
print(x)
x[0][2]='C'
print(x[0][2])
print(x[1][1])
print(x)
