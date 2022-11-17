# 6-1 Person:

person = {'first_name': 'sophia',
          'last_name': 'smith',
          'age': 30,
          'city': 'athens'}

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])
# print(person['sophia'])
# print(person['smith'])
# print(person[30])
# print(person['athens'])


# print('=========================================================')

# 6-2 Favourite Numbers
fav_numbers = {'emma': 13,
               'sophia': 25,
               'mike': 21,
               'max': 100,
               'alice': 18}
print(fav_numbers)
print(fav_numbers['emma'])
print(fav_numbers['mike'])
print(fav_numbers[25])
# 6-3 Glossary


glossary = {'modulo': 'reminder',
            'loops': 'executing code repeatedly',
            'tuples': 'immutable data structure',
            'append': 'adding new value to the end',
            'indentation': 'tab/space at the beginning of line code'}
for key, value in glossary.items():
    print(key.title() + ' is ' + value + '.')


# print('=========================================================')

glossary = {'modulo': 'reminder',
            'loops': 'executing code repeatedly',
            'tuples': 'immutable data structure',
            'append': 'adding new value to the end',
            'indentation': 'tab/space at the beginning of line code'}

print(glossary, '\n \t')


# 6-6 Polling
favorite_languages = {'jen': 'python',
                      'sarah': 'c',
                      'edward': 'ruby',
                      'phil': 'python'}
names = ['john', 'sarah', 'anna', 'phil']
for name in names:
    if name in favorite_languages:
        print(f'{name.title()}, thank you for taking the poll.')
    else:
        print(f'{name.title()}, please take poll!')

