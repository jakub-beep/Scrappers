# this program generates passwords
import random

small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u']
big_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def password_generator(characters):
    password = ''
    try:
        characters_int = int(characters)
        list_of_elements = random.sample(small_letters, characters_int - 4) + random.sample(big_letters, 2) + \
                           random.sample(numbers, 2)

        for element in list_of_elements:
            password += element
        return password

    except:
        print('You need to enter a number bigger or equal than 4')
