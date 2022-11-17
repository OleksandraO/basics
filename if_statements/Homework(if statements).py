# 4-13 Buffet

buffet = ('fish', 'falafel', 'pasta', 'pizza', 'sushi')
print(f'This restaurant offers following dishes: ')
for food in buffet:
    print(food.title())

# buffet[0] = 'steak'

buffet = ('steak', 'lasagna', 'pasta', 'pizza', 'sushi')
print(f'\nThis is the updated menu: ')
for food in buffet:
    print(food.title())

# 5-1 Conditional tests:

# 1
names = ['james', 'ana', 'mark', 'sophia', 'nicholas']
if 'maria' in names:
    print('Sorry, you are not in the list')
else:
    print('Welcome to the club')

print('==================================================')

# 2
food = 'pizza'
if food != 'pasta':
    print('I don\'t like pasta!')

print('==================================================')

# 3
name = 'sophia'
if name == 'sophia':
    print('Hello my friend!')
else:
    print('Hello stranger!')

# 4
city = 'Paris'
if city != 'Milan':
    print('This is my dream vacation!')
else:
    print('I visited it last year!')

# 5
# grades = input('Please enter your grade')
# grades = int(grades)
#
# if 90 < grades < 100:
#     print('Great job, you work was very impressive')
# elif 70 < grades <= 90:
#     print('Well done, keep it up with good work')
# elif 60 < grades <= 70:
#     print('You need to practice more')
# elif 50 < grades <= 60:
#     print('You did not pass, please come back when you ready')
# else:
#     print('Your work was not found, please address the issue at the main office')
#
#
# print('==================================================')


# 5-2 More conditional Tests

# 1 Tests for equality and inequality with strings
# flower = 'lily'
# flower == 'lily'
# True

# city = 'paris'
# city == 'milan'
# False

# name = 'jane'
# name == 'sophia'
# False

# 2 Tests using lower() functions

# city = 'athens'
# city == 'Athens'
# False

# country = 'Greece'
# country.lower() =='greece'
# True

# country = 'spain'
# country.upper() == 'Spain'
# False

# country = 'france'
# country.title() == 'France'
# True


# 3 Numerical tests

# num = 13
# num == 13
# True


# num = 13
# num == 13
# False

age = 32
if age != 32:
    print('Wrong answer! try again')
else:
    print('You are correct!')

# num =20
# num < 34
# True
# num >=55
# False
# num !=20
# False
# num < 3
# False
# num <=20
# True

# 4 Tests using keyword AND/OR
# age = 33
# 15 < age <=35
# True
# age > 23 and age <50
# True
# age > 34 or age <35
# True

# 5 Test whether item in the list
names = ['maria', 'james', 'sophia']
if 'sophia' in names:
    print('Hello there!')
else:
    print('Welcome friends')

# 5 Test whether item is not in the list
names = ['maria', 'james', 'sophia']
if 'ana' in names:
    print('Hello there!')
else:
    print('Welcome friends')

# print('==================================================')


# 5-3 Aliens Colors #1

alien_color = 'green'
if alien_color == 'green':
    print('Congratulations!! You just won 5 points')
else:
    print('Game over')

alien_color = 'green'
if alien_color == 'yellow':
    print('Congratulations!! You just won 5 points')
else:
    print('Game over')

# print('==================================================')


# 5-4 Aliens colors #2

alien_color = 'yellow'
if alien_color == 'green':
    print('Congratulations!! You just won 5 points')
else:
    print('You just won 10 points!!!')

alien_color = 'yellow'
if alien_color != 'green':
    print('Congratulations!! You just won 5 points')

# print('==================================================')


# 5-5 Aliens colors #3

alien_color = 'red'
if alien_color == 'green':
    print('Congratulations!! You just won 5 points')
elif alien_color == 'yellow':
    print('You just won 10 points!!!')
elif alien_color == 'red':
    print('You just won 15 points!!!')
else:
    print('Game over')

# print('==================================================')


# 5-6 Stages of Life:
#age = int(input('Please enter your age'))
if age < 2:
    print('The person is a baby')
elif 2 <= age < 4:
    print(' The person is a toddler')
elif 4 <= age < 13:
    print('The person is a kid')
elif 13 <= age < 20:
    print('The person is a teenager')
elif 20 <= age < 65:
    print('The person is a adult')
else:
    print('The person is elder')

# print('==================================================')


# 5-7 Favorite fruit

favourite_fruits = ['banana', 'blueberry', 'apricot']
if 'banana' in favourite_fruits:
    print('You really like bananas!')
if 'apricot' in favourite_fruits:
    print('I really love apricots')
if 'melon' in favourite_fruits:
    print('Love melon!')
else:
    print('I hate melons')
if 'blueberry' in favourite_fruits:
    print('I eat them every day!!')
if 'strawberry' in favourite_fruits:
    print('These are my favourite!!')
else:
    print('NEVER LIKED THEM!')

# print('==================================================')


# 5-8 HELLO ADMIN

user_name = ['admin', 'guest', 'manager', 'supervisor', 'user']
for user in user_name:
    if user == 'admin':
        print(f'Hello {user.title()}, would you like to see a status report?')
    else:
        print(f'Hello {user.title()}, thank you for loging in again!')

# print('==================================================')


# 5-9 No Users
user_name = ['sophia', 'mike', 'ana']
if user_name:
    for user in user_name:
        print(f'Welcome {user.title()}!!')
else:
    print('We need to find some users!!!')



user_name = []
if user_name:
    for user in user_name:
        print(f'Welcome {user.title()}!!')
else:
    print('We need to find some users!!!')


# print('==================================================')


#5-10 Checking Usernames

current_users = ['guest', 'user', 'admin', 'supervisor', 'tech']
new_users = ['mike', 'john', 'guest', 'sophia', 'ADMIN']
for new_user in new_users:
    if new_user.lower() in current_users:
        print(f'{new_user.title()}, Enter a new username!')
    else:
        print(f'{new_user.title()}, Username is available!')


#5-11 Ordinal Numbers

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in nums:
    if num == 1:
        print(f'{num}st')
    elif num == 2:
        print(f'{num}nd')
    elif num == 3:
        print(f'{num}rd')
    else:
        print(f'{num}th')










# Interview questions:
# Problem 1:

#num = int(input('Please enter a number'))
if num % 3 == 0 and num % 5 == 0:
    print('FuzzBuzz')
elif num % 3 == 0:
    print('Fuzz')
elif num % 5 == 0:
    print('Buzz')
else:
    print('This is not dividable by 3 or 5')

# Problem 2:

# nums = int(input('Please enter a number'))
# nums = [4, 6, 9, 7, 65, 678, 8, 5, 31, 24, 22, 55, 778, 990]
# for num in nums:
#     if num == 5:
#         print('Hoooraa')
#     else:
#         print('Try again')
