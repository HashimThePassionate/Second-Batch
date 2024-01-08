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
from math import radians, sin, cos, sqrt, atan2

def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371.0
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance

city1 = {'name': 'City A', 'latitude': 40.7128, 'longitude': -74.0060}
city2 = {'name': 'City B', 'latitude': 34.0522, 'longitude': -118.2437}

distance = haversine_distance(city1['latitude'], city1['longitude'], city2['latitude'], city2['longitude'])
print(f"The distance between {city1['name']} and {city2['name']} is approximately {distance:.2f} kilometers.")

import random

def generate_random_quote():
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "In the end, we will remember not the words of our enemies, but the silence of our friends. - Martin Luther King Jr.",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
        "Do not wait to strike till the iron is hot, but make it hot by striking. - William Butler Yeats"
    ]

    return random.choice(quotes)

# Example usage
random_quote = generate_random_quote()
print(random_quote)


    
