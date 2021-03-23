# -*- coding: utf-8 -*-
'''
Welcome to the 6-sided dice roller simuator!

This simple Python2 terminal-based application allows you to simulate the rolling
of a 6-sided dice.

Ana Teresa Queiroga (anatqueiroga), March 2021

--
Adapted from Udemy's course 'Python Bootcamp 2021 Build 15 working Applications
and Games '

see here: https://www.udemy.com/course/python-complete-bootcamp-2019-learn-by-applying-knowledge/
--

'''

import random

rolling_letter = 'y'
user_input     = 'y'

# 2 - Defining the dice

while user_input == rolling_letter:
    print('-- Rolling the dice! --')
    random_dice_num = random.randint(1,6) #generating the random number

    if random_dice_num == 1:
        print('----------')
        print('|        |')
        print('|    O   |')
        print('|        |')
        print('----------')

    elif random_dice_num == 2:
        print('----------')
        print('|        |')
        print('|  O  O  |')
        print('|        |')
        print('----------')

    elif random_dice_num == 3:
        print('----------')
        print('|      O |')
        print('|    O   |')
        print('|  O     |')
        print('----------')

    elif random_dice_num == 4:
        print('----------')
        print('|  O   O |')
        print('|        |')
        print('|  O   O |')
        print('----------')

    elif random_dice_num == 5:
        print('----------')
        print('|  O   O |')
        print('|    O   |')
        print('|  O   O |')
        print('----------')

    elif random_dice_num == 6:
        print('----------')
        print('|  O   O |')
        print('|  O   O |')
        print('|  O   O |')
        print('----------')

    user_input = raw_input('Press y to roll the dice again!' + '\n' + 'Press x to exit the simulator. ')

    if user_input == 'y':
        continue
    elif user_input == 'x':
        print('-- See you next time! --')
        exit()
    else:
        print('\n' + '                ¯\_( ͡❛ ⏥ ͡❛)_/¯' + '\n' +
         '-- Invalid character. Please enter a valid one. --' + '\n')

        user_input = raw_input('Press y to roll the dice again!' + '\n'
        + 'Press x to exit the simulator. ')
