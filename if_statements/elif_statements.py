# #chapter 5 : ELIF statements
#
# #else if - elif
#
# # if expression1:
# #     code to execute when expression1 is True
# # elif expression2:
# #     code to execute when expression2 is True
# # elif expression3:
# #     code to execute when expression3 is True
# # elif expression4:
# #     code to execute when expression4 is True
# # else:
# #     code to exe
# cute when none of above expressions are True
# #
#
# #input (prompt_message) - this asks the user to input and return a string(always)
# # age = input('Please enter your age: ')
# # age = int(age)
# print('Hello ')
# for i in range(5):
#     print(f'Iteration #: {i}')
# #can do in 1 line
#     age = int(input('Please enter your age: '))
#
#     #if age is less than 17 then you can get DL, from 17-25 pay more to insurance, older than 25 print dont drink and drive
#
#     if age < 17:
#         print(f'You can not get DL')
#     elif 17 <= age < 25:
#         print(f'Good you are eligible to get DL, but you have to pay more insurance')
#     elif 25 <= age < 120:
#         print(f'Don\'t drink and drive')
#     else:
#         print(f'Hello')
#
# # h/w: if number dividable by 3, print 'Fuzz',
# if number dividable by 5 then print 'Buzz',
# if number dividable by 3 and 5 then print 'FuzzBuzz"

n = 10
#10 = 3*n+1

if n % 3 == 0:
    print('this is dividable by 3')
else:
    print('this is not dividable')

# how can you loop through the list of number
# and check that number 5 is in the list
# when you find 5 then stop the loop print 'Hooraa'

#use 'break' keyword to stop the loop