# Chapter 4: Slicing the list

pizzas = ['chicken', 'cheese', 'capriciosa', 'funghi', 'sicilian']

for pizza in pizzas[0:3]:
    print(f'we have {pizza} pizza today')
for pizza in pizzas[2:5]:  # - includes index 2, 3, 4
    print(f'we have {pizza} pizza today')

    print('---------COPY THE LIST-----------')
for pizza in pizzas[3:-1]:  # - from 3rd to the end
    print(f'we have {pizza} pizza today')

    print('---------COPY THE LIST-----------')
for pizza in pizzas[3:]:  # - means from 3 index to the end
    print(f'we have {pizza} pizza today')

    print('---------COPY THE LIST-----------')

for pizza in pizzas[:3]:  # - from beginning to the 3rd element
    print(f'we have {pizza} pizza today')

    print('---------COPY THE LIST-----------')
    new_pizzas = pizzas  # creates the new reference list to the same list
    copy_pizzas = pizzas[:]  # creates the totally independent list(copy_pizzas)

pizzas.append('cheese steak')
new_pizzas.append('mushroom')
copy_pizzas.append('veggie')
copy_pizzas.append('grandma')
print(f'Lists before updating {pizzas}\n{new_pizzas}\n{copy_pizzas}')

# Tuples - immutable data structure
animals = ('dog', 'cat', 'horse')
dog_index = animals.index('dog')
print(f'index of the dog element in the tuple: {dog_index}')
sorted_animals = sorted(animals)
print(f'sorted animals: {sorted_animals}')

# H-W 4-10, 4-11, 4-12

list_animals = list(animals)
print(list_animals)
