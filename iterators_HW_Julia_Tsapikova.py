"""
Home work for lesson "Iterators_2".
Performed by Julia Tsapikova

# Task_1. FizzBuzz

for i in range(1, 101):
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz", end = " ")
    elif i%3 == 0:
        print("Fizz", end = " ")
    elif i%5 == 0:
        print("Buzz", end = " ")
    else:
        print(i, end = " ")

# Task_2. Key - value.


d = {'key1': 'value1', 'key2': 'value2'}
print(dict([(y,x) for (x,y) in d.items()]))


# Task_3. Duplikates

from itertools import groupby
x = [1, 1, 2, 3, 5, 4, 5, 6]
new_x = [el for el, _ in groupby(x)]
print(new_x)

"""







        
    
