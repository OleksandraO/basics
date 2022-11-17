# Chapter 9: classes and objects

# pep8: guidelines
# use lowercase letters and underscore for:
# packages, folders, file, variable (object of class)
# functions names

# use combination of tittle case for:
# classes
# self keyword -

msg = 'Wouf Wouf'
breed = 'General'


class Dog():
    """
    Model of dogs, template for dogs.
    """
    # attribute(description) - variables
    # name = 'a'
    # breed = 'chow chow'
    # color = ''
    size = 'medium'
    age = '2'

    # CONSTRUCTOR of the class when you instantiate
    # default function to make required arguments
    # executed automatically everytime when you create an object(instance)

    def __init__(self, nm, brd, clr):
        self.name = nm
        self.breed = brd
        self.color = clr

    # behaviour(actions) - functions
    def eat(self):
        breed = ''
        print(f'{self.name} is eating ...')
        print(f'{self.name} wants more ...')
        print(f'{self.name} done eating .')
        print(f'{self.breed} {msg}')
        print(f'{self.breed} {breed}')

    def run(self):
        print('dog is running')

    def get_description(self):
        # run() #outside the class
        # self.run() #within the class
        print(f'Name of the dog: {self.name}')
        print(f'Bread of the dog: {self.breed}')
        print(f'Color of the dog: {self.color}')
        print(f'Size of the dog: {self.size}')
        print(f'Age of the dog: {self.age}')


# instantiation  - creating instance of the class - creating object
# dog1,dog2 are the object
dog1 = Dog('chubby', 'chow chow', 'brown')  # copying everything from the model to new object
print('name of the dog before:', dog1.name)
dog1.name = 'trex'  # assigning value to attributes
print('name of the dog, after assigning:', dog1.name)
dog1.eat()
dog1.breed = 'poodle'
print('dog1 breed', dog1.breed)

print("---------Dog2--------------")
dog2 = Dog('max', 'german sheppard', 'black')
print(dog2.name)  #
print(dog2.breed)
dog2.get_description()
