#chapter 5 : if statements


cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw' or 2 == 2 and ('hello'.upper() == 'HELLO'):
        print(f'car value was bmw so we are doing print differently: {car.upper()}')
    else:
        print(f'expression returned false so we are doing Title() : {car.title()}')


# expressions:

name = 'john'
num = 45.55
is_good = True
friends = []
#
# name == 'jane'  # checking if the value of the name var is equal
# name > 'abc' # A-Z (a,b, ..j..)
# num == 45  # False
# num > 45  # true
# num >= 45  # true
# num <= 45  # false
# num > 45  # false
# is_good == False #false
# name.lower() != 'jane' #- true Jane, jAne, JANE
# #

if friends:
    print('friends is not empty list')
else:
    print('friends expression returned false, this mean it is an empty list')
#friends expression returned false, this mean it is an empty list')


friends = ['jane']
if friends:
    print('friends is not empty list')
else:
    print('friends expression returned false, this mean it is an empty list')
#friends is not empty list


name == 'john' and num > 45 # true and true => true
name == 'john' and num < 45 # true and false => false


#cars = ['audi', 'bmw', 'subaru', 'toyota']
print('-----------------------------------------')
print(cars)
if 'tesla' in cars:
    print(f'cars list includes tesla')
else:
    print(f'tesla is not in the cars list')


#Exercise 5-1