# scenarios

from while_loop import fuzz_buzz as fb #this imports only one function
from while_loop_Akmals import *
from functions.functions_return import *


#import while_loop, we need to mention module name with each function use
#while_loop.fuzz_buzz()
print('#execution of function from while_loop.py')
fb() # executing fuzz_buzz() functions with alias name.

while_loop.increment()
while_loop.decrement()

print('#execution of functions from functions_returns.py')

print('Result of the function: ', build_full_name('john', 'doe'))
build_full_name('jane', 'doe')
person2 = build_full_name('jane', 'doe')
print('Person2:', person2)


print(city_country('paris', 'france'))
print(city_country('london', 'united kingdom'))
print(city_country('new york', 'united states'))
