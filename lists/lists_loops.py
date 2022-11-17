#chapter 4: Looping through the list

places = ['hawai', 'paris', 'bahamas', 'iceland', 'canada']
#loops - executing the code repetitively (what ti loop through, how many times,)

print('Looping through entire list: ')
print(f'I want to visit {places[0]} next summer')

#for var_each_element in list_name:
    #print('lines of code to be repeated')


for place in places:
    #print(place)
    print(f'I want to visit {place} next summer')
    print('ohhh I need to convince my husband')
    print(f'How far is the {place.title()} from New York?')


nums =[5, 7, 100, 99]
for num in nums:
    print(num)
    num = num + 5


# working with list of numbers, range()
# range(5) -> 0, 1, 2, 3, 4, 5
# range(2,6) -> 2, 3, 4, 5
# range(4, 16, 3) -> 3, 7, 10, 13
print(range(5))
print(list(range(5)))

for num in range(5):
    print(f'Each number: {num}')
    print('==================================')

for num in range(2, 6):
    print(f'Each number: {num}')
    print('==================================')

for num in range(4,16,3):
    print(f'Each number: {num}')


# problem solving: list all numbers between 21 and 36 that can be divided by 4
for num in range (24, 37, 4):
    print(f'each number: {num}')

# list of squares of numbers between 25 and 30

for num in range(25,31):
    print(f'num ={num} and square is: {num**2}')


range(5, 10, -2)

for num in range(5, 10, -2):
    print({num})


nums =[4, 2, 9, 10]
print(f'sum of the nums: {sum(nums)}')
