# import pandas as pad
#
# d = {'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}
#
# df = pad.DataFrame(data=d)
#
# print(df)
#
# count_column = df.shape[1]
# print(f'Number of columns={count_column}')
#
# count_row = df.shape[0]
# print(f'Number of rows={count_row}')

from  dataclasses import dataclass

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

@dataclass
class Person:
    name:str
    age:int = 20

obj = Person('rajeev', 25)

a= None
print(type(a))

def fun(p1,p2,/,*,k1,k2):
    print(f'name is {p1} and job is {p2} and education is {k1} and hobby is {k2}')

fun('rajeev', 'software developer', k1='mca', k2='coding and gaming')

f'frffwffvf'



