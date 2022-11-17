friend = {'name': 'john',
          'age': 25,
          'location': 'Brooklyn'}
print(friend['age'])


# Chapter 6: dictionary - data structure (key-value pair)
# CRUD  (create, read, update, delete)
print('########1. creating empty dictionary')
# person1 = {}
# person2 = dict()

languages_list = ['eng', 'ru', 'esp', 'marsian']
person1 = {'name': 'john doe',
           'age': 25,
           'location': 'ny',
           'cars': ['audi', 'bmw', 'subaru'], #independent value
           'languages': languages_list}  # two-way reference to the list (connected)
print('#########2.accessing the values (R)')
# person1['name']
print(f"getting name of person1 {person1['name']} ")
print(f"getting name of person1 {person1['age']} ")


print('#####3. adding/updating key value pair to the dictionary (U)')
print('Original dictionary: ', person1)
person1['phone'] = '(123) 456-7891'
# phone key does not exist so it adds new key-value pair (element)
print('Updated with new dictionary: ', person1)

print("Updating the value of 'age' in the person1 dictionary")
person1['age'] = 30  # pay attention that you are mentioning the existing key
print('Updated age in person1 dictionary:', person1)

print("Updating the list value inside the dictionary ..")
# cars[0] = 'merc'
person1['cars'][0] = 'merc'
print('Updated list (audi to merc) in person1 dictionary: ', person1)

# languages_list = ['eng', 'ru', 'esp', 'marsian']
# person1['languages'] = languages_list
# print(person1)
print('Updating the list language_list (marsian to ger) ... ')
languages_list[3] = 'ger'
print('updated list: ', languages_list)
print('dictionary: ', person1)


print('Updating the value of the list in the dictionary .. ')
languages_list[2] = 'french'
print('updated list: ', languages_list)
print('dictionary: ', person1)


# copying the list to a value of the dictionary (independent value)
# languages_list = ['eng', 'ru', 'esp' , 'marsian']
# person1['languages'] = languages_list[:]
# print(person1)


print('### 4. Delete key-value pair from dictionary (D)')
print('Deleting the location key-value pair from person1 ...')
del person1['location']
print('updated person1 dictionary: ', person1)
person1['age'] = None # no value(in Java too), like NULL in SQL
print('updated age in person1 dictionary: ', person1)


# exercise: 6-2 Favorite Numbers
fav_nums = {'nicole': 7, 'alex': 10, 'yulia': 5}
# print each person's name and their favorite number.
print(f"Nicole's favorite number is: {fav_nums['nicole']}")
print(f"Alex's favorite number is: {fav_nums['alex']}")
print(f"Yulia's favorite number is: {fav_nums['yulia']}")

