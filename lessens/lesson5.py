from random import randint as generate_number

import calculator
import emoji
from decouple import config
from person import Person
from termcolor import cprint

print(generate_number(2, 5))
print(calculator.multiplication(2, 5))

my_friend = Person('Jim', 20)
print(my_friend)
cprint("Hello, World!", "green", "on_red")
print(emoji.emojize('Python is :thumbs_up:'))

print(config('DATABASE_URL'))
commented = config('COMMENTED', default=0, cast=int)
print(commented * 2)
print('END')
