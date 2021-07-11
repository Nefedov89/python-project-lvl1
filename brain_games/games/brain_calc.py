import random

OPERATORS = ['+', '-', '*']


def show_game_conditions():
    print('What is the result of the expression?')


def get_correct_answer(expression):
    res = eval(expression)

    return str(res)


def get_question_value():
    num_1 = random.randint(1, 100)
    num_2 = random.randint(1, 100)
    operator = OPERATORS[random.randint(0, len(OPERATORS) - 1)]

    return '{} {} {}'.format(num_1, operator, num_2)
