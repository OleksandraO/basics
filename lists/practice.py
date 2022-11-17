pizzas = ['margherita', 'peperoni', 'veggie', 'sicilian', 'hawaiian']
for pizza in pizzas:
    print(f'I like {pizza.title()} pizza.')
print('I really love pizza!')

print('------------------------------------------------')

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_food = my_foods[:]

my_foods.append('canoli')
friend_food.append('ice cream')

print('My favorite foods are:')
print(my_foods)

print('My friends favorite foods are:')
print(friend_food)

print('------------------------------------------------')

pizzas = ['chicken', 'cheese', 'mushroom']
print(pizzas)
print(f'List of my favorite pizzas: {pizzas}')
pizzas.append('sicilian')
print(f'Updated list of pizzas: {pizzas}')

new_pizza = pizzas
friends_pizza = pizzas[:]
new_pizza.append('steak')
print(f'New list of pizzas: ')
for new_pizza in pizzas:
    print(new_pizza)

friends_pizza.append('peperoni')
print(f'Friends pizza list is: ')
for friend_pizza in friends_pizza:
    print(friend_pizza)

# tuples
dimensions = (200, 50)
print(dimensions[1])
print(dimensions[0])
#dimensions[0] = 250
#print(dimensions[0])

print('======================================')

dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)


dimensions = (200, 50)
print('Original dimensions:')
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print('\n Modified dimensions:')
for dimension in dimensions:
    print(dimension)
