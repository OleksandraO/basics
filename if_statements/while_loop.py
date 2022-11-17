#Chapter 7: user input and while loop

name = 'john'
# while expression: - checks expression true or false
#     code to repeatedly execute with each iteration
#     code to repeatedly execute with each iteration
#     code to repeatedly execute with each iteration
#     code to repeatedly execute with each iteration

# be cautious of infinite loop to avoid make sure the
#condition is changing with each iteration


print('While loop when we are setting upper limit '
      'in the condition, we need to increment')
current_number = 1
while current_number <= 5:
    print('current number:', current_number)
    current_number += 1


print('While loop when we are setting lower limit '
      'in the condition, we need to decrement')
current_number = 1
while current_number > -10:
    print('current number:', current_number)
    current_number -= 1



print('Fuzz Buzz example with while loop....')
answer = ''
while answer.lower() != 'n':
    #num = int(input('Please enter a number'))
    num = 3
    if num != 0:
        if num % 3 == 0 and num % 5 == 0:
            print('FuzzBuzz')
        elif num % 3 == 0:
            print('Fuzz')
        elif num % 5 == 0:
            print('Buzz')
        else:
            print('This is not dividable by 3 or 5')
    else:
        print('please enter different number than 0')
    answer = input("Do you want to continue? yes/no")



prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)