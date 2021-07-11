import random

NUMBER_IS_PRIME_CORRECT_ANSWER = 'yes'
NUMBER_IS_NOT_PRIME_CORRECT_ANSWER = 'no'
RANDOM_INTEGER_NUMBER_MIN = 1
RANDOM_INTEGER_NUMBER_MAX = 1000


def show_game_conditions():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def get_correct_answer(number):
    return NUMBER_IS_PRIME_CORRECT_ANSWER \
        if is_prime(number) \
        else NUMBER_IS_NOT_PRIME_CORRECT_ANSWER


def get_question_value():
    return random.randint(RANDOM_INTEGER_NUMBER_MIN, RANDOM_INTEGER_NUMBER_MAX)


def is_prime(number):
    if number < 1:
        return False

    is_prime = True

    for i in range(2, int(number / 2) + 1):
        if (number % i) == 0:
            is_prime = False
            break

    return is_prime
