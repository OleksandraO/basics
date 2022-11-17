# Homework 8-1
#
# 8-1. Message: Write a function called display_message() that prints one sentence
# telling everyone what you are learning about in this chapter. Call the
# function, and make sure the message displays correctly.

def display_message():
    print('In this chapter you\'ll learn to write functions, which are named blocks of code that are '
          'designed to do one specific job.')


display_message()


# 8-2. Favorite Book: Write a function called favorite_book() that accepts one
# parameter, title. The function should print a message, such as One of my
# favorite books is Alice in Wonderland. Call the function, making sure to
# include a book title as an argument in the function call.

def favourite_book(title):
    print(f'One of my favourite books is {title}.')


favourite_book('Alice in Wonderland')


# 8-4 Large Shirts
def make_shirt(size="Large", message='I love Python'):
    print(f'I have {size} size shirt with the message printed "{message}"!')


make_shirt()


def make_shirt(size="Medium", message='I love Python'):
    print(f'I have {size} size shirt with the message printed "{message}"!')


make_shirt()

make_shirt('Small', 'Hello World')


#8-5 Cities

def describe_city(city_name, country_name='Spain'):
    print(f'{city_name.title()} is in {country_name.title()}. ')


describe_city('reykjavik', 'iceland')
describe_city(city_name='madrid')
describe_city(city_name='barcelona')
describe_city(city_name='malaga')
describe_city('santorini', 'greece')


#8-7 Album

def make_album(artist_name, album_name, num_of_tracks=0):
    album = {'name': artist_name.title(), 'album': album_name.title()}
    if num_of_tracks:
        album['num_of_tracks'] = num_of_tracks
    return album

# print(f'{} is presenting his new album {album_name}')
print(make_album('david bowie', 'magic dance'))
#another option
musician1 = make_album('amy winehouse', 'back to black', 23)
musician2 = make_album('depeche mode', 'enjoy the silence', 12)

print(musician1)
print(musician2)



