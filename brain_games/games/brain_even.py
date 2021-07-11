import random

NUMBER_IS_EVEN_CORRECT_ANSWER = 'yes'
NUMBER_IS_NOT_EVEN_CORRECT_ANSWER = 'no'
RANDOM_INTEGER_NUMBER_MIN = 1
RANDOM_INTEGER_NUMBER_MAX = 1000


def show_game_conditions():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def get_correct_answer(number):
    return NUMBER_IS_EVEN_CORRECT_ANSWER \
        if number % 2 == 0 \
        else NUMBER_IS_NOT_EVEN_CORRECT_ANSWER


def get_question_value():
    return random.randint(RANDOM_INTEGER_NUMBER_MIN, RANDOM_INTEGER_NUMBER_MAX)
