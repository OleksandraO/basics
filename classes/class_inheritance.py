# class inheritance:
from classes.working_with_classes import Car

print('-----------------------------')
# class A is parent of class B
# class B inherits of class A
# class B is a child has access to everything that A has
class A:
    name = 'I am from class A'

    def greet(self):
        print('hello')


class B(A):
    age = 25

    def get_age(self):
        print(f'My age is: {self.age}')


item1 = B() #when class inherits class A
print(item1.name)
print(item1.age)
item1.greet()
item1.get_age()

# parent class does not have access to child class attr and method of class A and B
item2 = A()
print(item2.name)
item2.greet()


print('----Inplementing the concepts with Car Class------')

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.batter_size = 80

    def fill_tank(self):
        print('Sorry this car does not have a tank, please go to charging')

    def get_description(self):
        super().get_description()
        print(f'Battery size: {self.batter_size}')


ecar1 = ElectricCar('tesla', 'model x', 2022)
ecar1.get_description()
ecar1.fill_tank()
ecar1.get_description()
print('-----------------------------------')
car1 = Car('bmw', 'x5', '2022')
car1.fill_tank()
car1.get_description()


