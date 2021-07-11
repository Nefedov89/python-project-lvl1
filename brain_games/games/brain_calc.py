import random

OPERATORS = ['+', '-', '*']
RANDOM_INTEGER_NUMBER_MIN = 1
RANDOM_INTEGER_NUMBER_MAX = 1000


def show_game_conditions():
    print('What is the result of the expression?')


def get_correct_answer(expression):
    res = eval(expression)

    return str(res)


def get_question_value():
    num_1 = random.randint(
        RANDOM_INTEGER_NUMBER_MIN,
        RANDOM_INTEGER_NUMBER_MAX
    )
    num_2 = random.randint(
        RANDOM_INTEGER_NUMBER_MIN,
        RANDOM_INTEGER_NUMBER_MAX
    )
    operator = OPERATORS[random.randint(0, len(OPERATORS) - 1)]

    return '{} {} {}'.format(num_1, operator, num_2)
