from msg import message as M,  line as L
from cal import square as s, add as a, info as i
from error import zeroError as e
print(L)
print(M)
print(L)
lt : list = s([1,2,3,4,5,6])
add : int = a(10,5)
dt : dict = i(name="Umer", age = 16)
print(lt)
print(L)
print(dt)
print(L)
print(add)
print(L)
print(e(0))
print(L)

