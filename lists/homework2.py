#4-10 Slices

pets = ['dog', 'cat', 'hamster', 'rabbit', 'parakeet', 'guinea pig']
for pet in pets:
    print(f'A {pet} would make a great pet.')
print('Any of these animals would make a great pet!')

# first message
print(f'The first three items in the list are:')
for pet in pets[0:3]:
    print(pet)

# second message
print(f'Three items from the middle of the list are:')
for pet in pets[2:5]:
    print(pet)

# third message
print(f'The last three items in the list are:')
for pet in pets[3:]:
    print(pet)

print('-------------------------------------------------')


# 4-11 My Pizzas, Your Pizzas

pizzas = ['margherita', 'peperoni', 'veggie', 'sicilian', 'hawaiian']
for pizza in pizzas:
    print(f'I like {pizza.title()} pizza.')
print('I really love pizza!')

print('---------------------------------------------------')

new_pizza = pizzas
friends_pizza = pizzas[:]

pizzas.append('chicken')
new_pizza.append('mushroom')
friends_pizza.append('everything')

print(f'My favorite pizzas are:')
for new_pizza in pizzas:
    print(f'{new_pizza.title()} ')

print('---------------------------------------------------')

print(f'My friend\'s favorite pizzas are:')
for friend_pizza in friends_pizza:
    print(f'{friend_pizza.title()}')

print('---------------------------------------------------')




