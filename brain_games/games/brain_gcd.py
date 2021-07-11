import random
import math


def show_game_conditions():
    print('Find the greatest common divisor of given numbers.')


def get_correct_answer(expression):
    nums_arr = expression.split(' ')
    num_1 = int(nums_arr[0])
    num_2 = int(nums_arr[1])

    return str(math.gcd(num_1, num_2))


def get_question_value():
    num_1 = random.randint(1, 100)
    num_2 = random.randint(1, 100)

    return '{} {}'.format(num_1, num_2)
