print('Hello world')
# this is a comment line , CTRL + /

# variables - temporary storage, keeps the value of something while code runs,
# they should have names - a,b, name, number.
# IT CANNOT START WITH NUMBERS!!
# SHOULD START WITH LOWER CASE LETTER

# varname = value - meaning setting variable value. it can be number, string, etc.
a = 45  #- variable will hold value 45 - number, integer (data type)
b = 6.87 #- number, float, double (data type)
name = 'john doe' #- text, string (data type)
msg = 'hello, this is my first coding practice!!!!' # - string (data type)

print(a)
print(b)
print(name)
print(msg)

a = 90

a = 1000
print(a)
print(a)
print (a)
print(a)
print('I am printing the variables', a, b, name, msg)

# pep8 - python best practices (in coding) guidelines


print (a)
print(a + b)  # last version of a is being added
print(name + ': ' + msg)






# 10/9/2022
a = a + 1 #- right side of the equzion will be added first
print(a)

a += 1
print(a)

a -= 1
print(a)

# length_of_persons_name - snake case

#print(c)
# print(c) will give NameError since the name is not defined yet


# useful functions for strings

print(name)
print("# title(), upper(), lower(), isLower(), isUpper() ")
print('name before title', name)
print('name with title', name.title())
print('name after title', name)
print('using is lower:', name.islower())


# name = ada love


print('#concatenation')
print('my message:' + name + ', ' + msg)
print('my message:' + name.title() + ', ' + msg.upper())

print('Special Characters: /\t /\n"')
# t - tab
# n - new line
print('my message:' + name.title() + ', ' + msg.upper())
print('my message: \t\t\t\t' + name.title() + ', \n\t\t\t\t' + msg.upper())
print('Message to everyone:\n\t\t\t\t' + 'please have fun!!'.upper())


location = '   \thawaii\n\t'
print(location)


# strip() - remove white space from both sides, rstrip() - removes space from right side, lstrip() - removes space from left side, works with string values
print(location.strip())
print('my wedding venue: ' + location.strip().upper()+' islands')
#  print('my wedding venue: ' + a.strip().upper()+' islands') - expected error, can not be executed since a is integer, and the rest is string



print('  # working with numbers   ####  ')

num1 = 3
num2 = 8
print('addition: ', num1 + num2)
print('substraction: ', num1 - num2)
print('multiplication: ', num1 * num2)
print('division: ', num1 / num2)
print('exponent: ', num1 ** 2)
print('floor division: ', 20 // num1)
print('modulo: ', 20 % num1)

# find odd numbers 20-50 -> 21 (21=2*10 +1), 23 (23=2*11 +1)
# if n%2 return 1 then n is odd number - (pseudo code)
# if n%2 return 0 then n is even number - (pseudo code)


print('## str(expression), converts expression to a string')
print('addition: :' + str(num1 + num2))
num3 = '456' # - this is a string type
num4 = 45.4566 # - float data type, int(num4) will get only int part of it
print('addition with num3:', num1 + int(num3))
print('converted to int:', int(num4))

# summary
# variable(naming), values - string, int, float, double, boolean(true and false), primitive data type
status = True   # - this is a boolean value
newstat = False   # - always upper case
# string: concatenate, upper(), title(), str(), '\t', '\n'
# numbers: int, float/double, int(), +, -, *, /, **, //, %




