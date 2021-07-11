import prompt
import random

QUESTION_TRIES_NUMBER = 3
NUMBER_IS_EVEN_CORRECT_ANSWER = 'yes'
NUMBER_IS_NOT_EVEN_CORRECT_ANSWER = 'no'


def show_game_conditions():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def get_correct_answer(number):
    return NUMBER_IS_EVEN_CORRECT_ANSWER \
        if number % 2 == 0 \
        else NUMBER_IS_NOT_EVEN_CORRECT_ANSWER


def show_and_handle_questions(user_name=''):
    is_user_gave_wrong_answer = False

    for x in range(QUESTION_TRIES_NUMBER):
        random_int_number = random.randint(1, 100)
        print('Question: {}'.format(random_int_number))
        user_answer = prompt.string('Your answer: ')
        correct_answer = get_correct_answer(random_int_number)

        if correct_answer == user_answer:
            print('Correct!')
        else:
            is_user_gave_wrong_answer = True
            print(
                "'{}' is wrong answer ;(. Correct answer was '{}'.".format(
                    user_answer,
                    correct_answer
                )
            )
            print('Let\'s try again, {}!'.format(user_name))
            break

    if not is_user_gave_wrong_answer:
        print('Congratulations, {}!'.format(user_name))
