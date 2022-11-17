print('---------------10-3 Guest-----------------------')
#
# with open('guest.txt', 'a') as userName:
#     name = input("Please enter your name")
#     userName.write(f'{name}\n')
#     # check file content


# print('-----------------10-4 Guest Book-----------------')
#
# with open('guest_book.txt', 'a') as userName:
#     name = input('Please enter your name')
#     while 2 == 2:
#         print(userName.write(f'Hello {name}!\nThank you for logging in!\n'))
#

print('-----------------10-5 Programming Poll -----------------')


with open('guest_book.txt', 'a') as responses:
    answer = input('Why do you like programming')
    while answer != '':
        print(responses.write(f'{answer}\n'))


