# Functions with Return Statement

def build_full_name(firstname, lastname):
    """returns beautiful full name."""
    print('starting to build full name')
    full_name = f"{firstname} {lastname}"
    return full_name.title()


print('Result of the function: ', build_full_name('john', 'doe'))
build_full_name('jane', 'doe')
person2 = build_full_name('jane', 'doe')
print('Person2:', person2)


# 8-6

def city_country(city: str, country: str):  # int, list, float
    """returns name of the city with country"""
    return f"{city.title()}, {country.title()}"


print(city_country('paris', 'france'))
print(city_country('london', 'united kingdom'))
print(city_country('new york', 'united states'))
