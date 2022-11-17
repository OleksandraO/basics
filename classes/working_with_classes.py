# 9 Chapter 9: Working with Clases and Instances
import self as self


class Car:
    # attribute - required, optional (default)
    # behaviour - CRUD - set, get, other
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = int(year)
        self.__mileage = 0  # hiding from the object, child classes - encapsulation

    def get_description(self):
        """ gets details about the car"""

        print(f'Car details: \nManufacturer: {self.make}\nModel:{self.model}\nYear: {self.year}')
        print(f'Current Mileage: {self.__mileage}')

    def set_mileage(self, new_mileage):
        if new_mileage > self.__mileage:
            print('setting the new value a mileage')
            self.__mileage = new_mileage
        else:
            print('mileage was less than current mileage, cannot be done')

    def add_to_mileage(self, miles):
        if miles >0:
            """increments the mileafe with given miles"""
            self.__mileage = self.__mileage + miles
            print(f'{miles}miles were added to your car mileage')
        else:
            print('you can not give negative number to increment mileage, cheating ha')

car1 = Car('bmw', 'x5', '2022')
print(car1.make, car1.year + 1)
print('#GETTER functions')
car1.get_description()
print('#SETTERs - updating the values of attributes')
car1.model = 'x5 M'
# car1.__mileage = 50 #setting a value
car1.set_mileage(50)
car1.get_description()
# car1.__mileage = 10
car1.set_mileage(50)
car1.get_description()
car1.add_to_mileage(-15)
car1.get_description()

#input,