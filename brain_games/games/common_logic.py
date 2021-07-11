import prompt

QUESTION_TRIES_NUMBER = 3


def welcome_user():
    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')

    print('Hello, {}!'.format(name))

    return name


def show_and_handle_questions(
        get_correct_answer_func,
        get_question_value_func,
        user_name=''
):
    is_user_gave_wrong_answer = False

    for x in range(QUESTION_TRIES_NUMBER):
        question_value = get_question_value_func()
        correct_answer = get_correct_answer_func(question_value)

        print('Question: {}'.format(question_value))

        user_answer = prompt.string('Your answer: ')

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
