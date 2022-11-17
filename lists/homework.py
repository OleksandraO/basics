# 3-4

guests = ['jake', 'nicholas', 'sophia', 'michael']
print(f'Hello {guests[0].title()}, I would like to invite you to dinner!')
print(f'Hello {guests[1].title()}, I would like to invite you to dinner!')
print(f'Hello {guests[2].title()}, I would like to invite you to dinner!')
print(f'Hello {guests[3].title()}, I would like to invite you to dinner!')



print('================================================================================================')



# 3-6
guests = ['jake', 'nicholas', 'sophia', 'michael']
print(f'Hello {guests[0].title()}, I found a bigger dinner table to more people will be coming')
print(f'Hello {guests[1].title()}, I found a bigger dinner table to more people will be coming')
print(f'Hello {guests[2].title()}, I found a bigger dinner table to more people will be coming')
print(f'Hello {guests[3].title()}, I found a bigger dinner table to more people will be coming')

guests.insert(0, 'lisa')
print(guests)

guests.insert(3, 'chistopher')
print(guests)

guests.append('emma')
print(guests)

for new_guest_list in guests:
    print(f'Hello {new_guest_list.title()}, I am having a dinner party this Saturday and cannot wait to see you there!')




print('================================================================================================')




#3-7

for new_guest_list in guests:
      print(f'Hello {new_guest_list.title()}, just found out that new dinner table wont arrive in time for the dinner '
            f'and there is space for two people only.')

print(guests)
# removed_guest = guests.pop(0)
print(f'Dear {guests.pop(0).title()}, I am sorry but lets reschedule the dinner for next time')
print(guests)


print(f'Dear {guests.pop(1).title()}, I am sorry but lets reschedule the dinner for next time')
print(guests)

print(f'Dear {guests.pop(2).title()}, I am sorry but lets reschedule the dinner for next time')
print(guests)

print(f'Dear {guests.pop(3).title()}, I am sorry but lets reschedule the dinner for next time')
print(guests)

print(f'Dear {guests.pop(0).title()}, I am sorry but lets reschedule the dinner for next time')
print(guests)

for updated_guest_list in guests:
    print(f'Hello {updated_guest_list.title()}, I am still waiting for you at the dinner!')


# del guests[0]
# del guests[1]

# print(guests)



print('================================================================================================')



#3-8

locs = ['milan', 'lisboa', 'monte carlo', 'sydney', 'galapagos']
print(locs)

# sorting in ascending order (sorted())
sorted_locs = sorted(locs)
print(sorted_locs)
print(locs)

# sorting in descending order (sorted())
sorted_reverse_locs = sorted(locs, reverse=True)
print(sorted_reverse_locs)
print(locs)

# changing order with reverse())
locs.reverse()
print(locs)

# reverse back to original list
locs.reverse()
print(locs)

#sorting to change list in ascending order

locs.sort()
print(locs)

#sorting to change list in descending order

locs.sort(reverse=True)
print(locs)



print('================================================================================================')


#3-9

len(guests)
print(guests)


print('================================================================================================')


#3-10


states = ['alabama', 'wisconsin', 'kentucky', 'texas', 'illinois']
print(states)

# list each state by index
print(states[0])
print(states[1])
print(states[-1])
print(states[2])
print(states[3])

# add more states using append()
states.append('new mexico')
print(states)

#add more states using insert()
states.insert(0, 'montana')
print(states)
states.insert(2, 'georgia')
print(states)

# using f- string to print a message

print(f'{states[1].title()} is one of North America\'s states.')
print(f'{states[-1].title()} is one of North America\'s states.')

# remove states by remove()
removed_state = states.remove('wisconsin')
removed_state = states.remove('montana')
print(states)

# remove states by pop()
removed_state = states.pop(0)
print(states)
removed_state = states.pop(2)
print(states)

# sorting states with sort() in ascending order
states.sort()
print(states)


# sorting states with sort() in descending order
#states.sort(reverse=True)
print(states)

# sorting states with sorted() temporarily in ascending order
sorted_states_asc = sorted(states)
print(sorted_states_asc)
print(states)

# sorting states with sorted() temporarily in descending order

sorted_states_desc = sorted(states, reverse=True)
print(sorted_states_desc)
print(states)

# reversing states list without sorting
states.reverse()
print(states)

# finding how many states in the list
len(states)
print(len(states))




print('===============================================================================')


# 4-1 Pizzas

pizzas = ['margherita', 'peperoni', 'veggie', 'sicilian', 'hawaiian']
for types in pizzas:
    print(f'I like {types} pizza.')
print('I really love pizza!')


print('===============================================================================')


# 4-2 Animals

pets = ['dog', 'cat', 'hamster', 'rabbit']
for animals in pets:
    print(f'A {animals} would make a great pet.')
print('Any of these animals would make a great pet!')




print('===============================================================================')




# 4-3 Counting to Twenty:

for num in range(1, 21):
    print(num)

print('===============================================================================')



# 4-4 One million:

#for num in range(1, 1001):
  # print(num)

print('===============================================================================')




# 4-5 Summing a Million:

nums = range(1, 1000001)
print(min(nums))
print(max(nums))
print(sum(nums))


print('===============================================================================')



# 4-6 Odd numbers:

for num in range(1, 21, 1):
    # checking condition
    if num % 2 == 1:
        print(num)

print('===============================================================================')


# 4-7 Threes:

for num in range(3, 31):
    print(num*3)


print('===============================================================================')


# 4-8 Cubes:

for num in range(1, 11):
    print(num**3)


print('===============================================================================')


# 4-9 Cube comprehension

cubes = [num**3 for num in range(1, 11)]
print(cubes)





# 4-11 My Pizzas, Your Pizzas

pizzas = ['margherita', 'peperoni', 'veggie', 'sicilian', 'hawaiian']
for pizza in pizzas:
    print(f'I like {pizza.title()} pizza.')
print('I really love pizza!')

new_pizzas = pizzas
friends_pizzas = pizzas[:]

new_pizzas.append('chicken')
friends_pizzas.append('mushroom')

print(f'My favorite pizzas are:')
for new_pizzas in pizzas:
    print(f'{new_pizzas.title()} ')

print(f'My friend\'s favorite pizza are:')
for friend_pizzas in friends_pizzas:
    print(f'{friend_pizzas.title()}')
