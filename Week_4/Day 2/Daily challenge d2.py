birthday= input('When is your birthday?')

# import datetime
# x = datetime.datetime(2020, 6, 26)
# print(x)

year = int(birthday.split("/")[-1])
age = str(2020-year)
candels = int(age[-1])
cake = f'''
    ___{"i"*candels}___
    | :H:a:p:p:y|
    |           |
 ___________________
|^^^^^^^^^^^^^^^^^^^|
| :B:i:r:t:h:d:a:y  |
|                   |
~~~~~~~~~~~~~~~~~~~~~



print(cake.format("i"*cypher))
'''
print(cake)