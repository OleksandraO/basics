# 9-1

class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'Name of the restaurant is: {self.restaurant_name}')
        print(f'This is {self.cuisine_type} restaurant.')

    def open_restaurant(self):
        print("Welcome everyone! we are now open")


restaurant1 = Restaurant('Brooklyn Pizza', 'Italian')

print(restaurant1.restaurant_name)
print(restaurant1.cuisine_type)

restaurant1.describe_restaurant()
restaurant1.open_restaurant()

# print('------------------2nd Restaurant---------------------')
#
# restaurant2 = Restaurant('Lou Lou', 'French')
#
# print(restaurant2.restaurant_name)
# print(restaurant2.cuisine_type)
#
# restaurant2.describe_restaurant()
# restaurant2.open_restaurant()
#
# print('------------------3rd Restaurant--------------------')
# restaurant3 = Restaurant('Chama Mama', 'Georgian')
#
# print(restaurant3.restaurant_name)
# print(restaurant3.cuisine_type)
#
# restaurant3.describe_restaurant()
# restaurant3.open_restaurant()
#
# print('------------------4th Restaurant--------------------')
#
# restaurant4 = Restaurant('Nagoya', 'Japanese')
#
# print(restaurant4.restaurant_name)
# print(restaurant4.cuisine_type)
#
# restaurant4.describe_restaurant()
# restaurant4.open_restaurant()

print('---------------------9-3-----------------------')


class User:

    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city

    def describe_user(self):
        print(
            f'User first name is: {self.first_name}, last name is {self.last_name}.User is {self.age} years old and '
            f'lives is {self.city}.')

    def greet_user(self):
        print(f'Welcome {self.first_name} {self.last_name}')


user1 = User('sophia', 'smith', 23, 'brooklyn')
user1.describe_user()
user1.greet_user()

print(user1.first_name)
print(user1.last_name)
print(user1.age)
print(user1.city)

print('------------------User 2------------------------')

user2 = User('james', 'oliver', 30, 'manhattan')
user2.describe_user()
user2.greet_user()

print(user2.first_name)
print(user2.last_name)
print(user2.age)
print(user2.city)

print('------------------User 3------------------------')

user3 = User('maria', 'diaz', 35, 'miami')
user3.describe_user()
user3.greet_user()

print(user3.first_name)
print(user3.last_name)
print(user3.age)
print(user3.city)

print('----------------------9-4--------------------')


class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f'Name of the restaurant is: {self.restaurant_name}')
        print(f'This is {self.cuisine_type} restaurant.')

    def open_restaurant(self):
        print("Welcome everyone! we are now open")

    def set_number_served(self, new_num_served):
        self.number_served = new_num_served

    def increment_number_served(self, num_served):
        """
        add a method called increment_numbe_served()that lets
        you increment the number of customers

        :param num_served: number that number_served to be incremented by
        :return:
        """
        self.number_served += num_served


restaurant1 = Restaurant('Brooklyn Pizza', 'Italian')

# Print number of customers restaurant served
print(f'Number of customers restaurant served: {restaurant1.number_served}')

# and then change the and print again
restaurant1.number_served = 15
print(f'Number of customers restaurant served: {restaurant1.number_served}')

# Call this method with a new number and print the value again
restaurant1.set_number_served(20)
print(f'Number of customers restaurant served: {restaurant1.number_served}')

# Call this method with any number you like that could represent how many customers were served in,say,
# a day of business
restaurant1.increment_number_served(7)
print(f'Number of customers restaurant served: {restaurant1.number_served}')

print("--------------------------9-5---------------------------------")
#
#
# class User:
#
#     def __init__(self, first_name, last_name, age, city, login_attempts):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.city = city
#         self.login_attempts = int(login_attempts)
#
#     def describe_user(self):
#         print(
#             f'User first name is: {self.first_name}, last name is {self.last_name}.User is {self.age} years old and lives is {self.city}.')
#
#     def greet_user(self):
#         print(f'Welcome {self.first_name} {self.last_name}')
#
#     def increment_login_attempts(self, new_login_attempts):
#         self.login_attempts += 1
#
#     def reset_login_attempts(self):
#         self.login_attempts = 0
#
#
# user1 = User('sophia', 'smith', 23, 'brooklyn', 5)
#
# user1.increment_login_attempts()
# print(f'Number of login attempts is: {user1.login_attempts}')
#
# user1.reset_login_attempts()
# print(f'Number of logins after resetting: {user1.login_attempts}')

print('---------------------------9-6---------------------------')


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'pistachio']

    def describe_restaurant(self):
        super().describe_restaurant()
        print(f'Ice Cream flavors at this restaurant are: {self.flavors}')


item1 = IceCreamStand('Lou Lou', 'French')
item1.describe_restaurant()

print('---------------------------9-7---------------------------')


class Admin(User):

    def __init__(self, first_name, last_name, age, city):
        super().__init__(first_name, last_name, age, city)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print(f'Admin has following privileges: {self.privileges}')


person1 = Admin('john', 'smith', 30, 'new york')
person1.privileges
person1.show_privileges()

print('---------------------------9-8---------------------------')


class Privileges(Admin):
    privileges = ['can add post', 'can delete post', 'can ban user']

    def __init__(self, first_name, last_name, age, city):
        super().__init__(first_name, last_name, age, city)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        super().show_privileges()
        print(f'The privileges are: {self.privileges}')


person2 = Privileges('john', 'smith', 30, 'new york')

print(person2.show_privileges())




