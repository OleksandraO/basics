#Chapter 7: Functions (methods)


#built-in functions: print(arg1,arg2), input(), sorted(), list.append()
#User defined functions, funcxtions that user created
#def greet_user(): #- name of function,
#def - is a key, we are defining function - declaring the function name,
# python, register my function!
# all lower case, no upper case, use underscore
#() - shows it is a function
#: - will be indented
# #registering in the python executable system
#
# def greet_user():
#     print('Hello class!')
#     print('Wonderful sunny day today!')
#
#
# #function overriding - resetting the content with the same name
#
# def greet_user():
#     print('Hello class!')
#     print('Wonderful sunny day today!')
#
# # how to execute? call the function
# # how to call? mention the name
#
# greet_user()
# print('logged in the system')
# greet_user()
# greet_user()
#
# #Docstring - gives description of what needs to be done

#functions with arguments:positional argument, required argument)
#def greet_user_by_name(name,day_of_week):
#def greet_user_by_name_with_def(name,day_of_week ='monday'):
# #function with default value:name is required, day of week is not required
#     print(f'Hello, {name.title()}!')
#     print(f'Wonderful sunny {day_of_week} today!')
# greet_user_by_name('jane', 'saturday')
# greet_user_by_name('sophia', 'sunday')
# greet_user_by_name('mike', 'monday')
#
# #need to mention when changing positions (executing functions
# #with parameters and arguements mentioned, positions does not matter)
# print('#Keyword arguments------------------------')
# greet_user_by_name(name ='mike', day_of_week='monday')
#
#
#
# print('#Default values-----------------------')
# greet_user_by_name_with_def('kamran', 'sunday')
# greet_user_by_name_with_def('nadia')
# greet_user_by_name_with_def('jamshid',day_of_week='wednesday')
# greet_user_by_name_with_def(day_of_week='monday', name ='nina')
#



#8-3 exercise

def make_shirt(size, text_to_print):
    '''
    Prints message and size of the shirt
    :return:
    '''
    pass
    print(f'The size of you shirt is {size}.')
    print(f"The message to be printed on your shirt is: \n\t\t '{text_to_print}'")

make_shirt(size='medium', text_to_print='Level Up Group')