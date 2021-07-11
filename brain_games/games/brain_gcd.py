import random
import math

RANDOM_INTEGER_NUMBER_MIN = 1
RANDOM_INTEGER_NUMBER_MAX = 1000


def show_game_conditions():
    print('Find the greatest common divisor of given numbers.')


def get_correct_answer(expression):
    nums_arr = expression.split(' ')
    num_1 = int(nums_arr[0])
    num_2 = int(nums_arr[1])

    return str(math.gcd(num_1, num_2))


def get_question_value():
    num_1 = random.randint(
        RANDOM_INTEGER_NUMBER_MIN,
        RANDOM_INTEGER_NUMBER_MAX
    )
    num_2 = random.randint(
        RANDOM_INTEGER_NUMBER_MIN,
        RANDOM_INTEGER_NUMBER_MAX
    )

    return '{} {}'.format(num_1, num_2)
