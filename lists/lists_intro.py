# Chapter 3: Data structure - structure that can hold more than 1 value, storage to hold multiple values,
# manage (create, add, update, remove)
# Python Data structures: Lists, Dictionary, Set, Tuple)
# [4, 10,6] ['john, 'mark', 'jane'] [True, False]

friends = []  # - empty list, assign empty value
players = list()  # - same empty list

nums = [4, 10, 6]
names = ['john', 'mark', 'jane']
bool_values = [True, False, True]
print(nums)
print(names)

# ctrl + alt + l - autoformat the file

# add elements, remove, update, read through values (access each value)

print('Hi, ', names[1].title())
print('Hi, ', names[0].title())
print('Hi, ', names[-1].title())
print('Hi, ', names[2].title())

# listname.append(new value) - adds new value to the end of the  list

names.append('alex')
print(names)

# listname.insert(index, value) - put the 'value' to the 'index'
# other vakues shifted left, all indexes will be updated
names.insert(2, 'araz')
print(names)
names[-1] = 'benny'  # - updating the last element of the list 'alex' -> 'benny'
print(names)

print('removing ther values from the list')
print("# remove element by index: del listname[index]. removing jane' ")
del names[3]
print(names)
print('#remove element by index: listname.pop() removing last in the list')
deleted_name = names.pop()  # - returns the value to the program after deleting
print(names)
names.pop()
print(names)
names.pop(0)
print(names)
print('we deleted following names: ', deleted_name)
print("#remove element by value: list.name.remove(value) ")

##names.remove('araz')
print(names)

#### 10/16/2022

## exercise 3-4

guests = ['akmal', 'said', 'lenur']
print(guests[0].title())
print(guests[1].title())
print(guests[-1].title())

print('Hello ' + guests[1].title() + ', I would like to invite you to my party!')

print('Good afternoon ' + guests[0].title() + ', I would like to invite you to the party')

print(f'Hello {guests[1].title()}, I would like to invite you to my party!')
print(f'Hello {guests[2].title()}, I would like to invite you to my party!')

removed_guest = guests.pop(1)
# removed_guest2 = guests.remove('akmal') - this will remove akmal but will not assign value to a variable
# a = 'said' - this is the same thing as line 60

print(guests)
# print(f'{guests.pop(1).title()} cannot make it to the party')
# print(f'{removed_guest2} cannot make it to the party')
print(guests)
guests.append('max')
print(guests)

print(f'Hello {guests[0].title()}, I would like to invite you to my party!')
print(f'Hello {guests[1].title()}, I would like to invite you to my party!')
print(f'Hello {guests[2].title()}, I would like to invite you to my party!')

# List sort

cars = ['tesla', 'bmw', 'lexus']
cars.sort()
print(cars)

# sorting is descending order

names = ['john', 'jane', 'mark']
names.sort(reverse=True)
print(names)

#sorting temporary - sorted()

car_models = ['model x', '550 xi', 'corolla', 'camry']
sorted_car_models_asc = sorted(car_models)

print(sorted_car_models_asc)

sorted_car_models_desc = sorted(car_models, reverse=True)
print(sorted_car_models_desc)
print(car_models)


# reversing without sorting

nums = [6, 3, 9, 7, 10]
#nums.reverse()
print(nums[0])
print(nums[-1])
print(nums[2])
print(nums[1])
print(nums[0])

# example
# unsorted list of number 10mln nums = [......]
# print largest and smallest number
# nums.sort()
# print('smallest number: ', nums[0])
# print('largest number: ', nums[-1])

print('number of elements in the nums list', len(nums))
print('number of elements in the names list', len(names))
print('number of elements in the cars list', len(cars))

print(len(cars))

nums = [3, 4, 5, 6]
#print(nums[4])
print(nums[3])

