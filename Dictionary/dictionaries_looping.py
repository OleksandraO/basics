# CHAPTER 6: Looping through a dictionary
# dictionaries keys, only values, key and value

print('# default case - looping through keys only')
person1 = {'name': 'john doe',
           'age': 25,
           'location': 'ny'}
for i in person1:
    print(i)

print('#looping through keys only----------------------')
for key in person1.keys():
    print('key in this iteration: ', key)
    print('key in this iteration: ', person1[key])


print('#looping through values only --------------------')
for value in person1.values():
    print('value in this iteration is: ', value)

print('#looping through keys and values only (mostly used)-----------')
for key, value in person1.items():  # returns 2 variables
    print('key in this iteration: ', key)
    print('value in this iteration: ', value)

rivers_countries = {'nile': 'egypt',
                   'amazon': 'brazil',
                   'mississippi':'usa',
                   'themes':'uk'}

for river, country in rivers_countries.items():
    print(f'The {river.title()} runs through {country.title()}.')

for river in rivers_countries.keys():
    print(f' River: {river.title()}')

for country in rivers_countries.values():
    print(f' Countries: {country.title()}')