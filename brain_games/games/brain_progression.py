import random

MISSED_NUMBER_DELIMITER = '..'
MIN_NUMBERS_COUNT_IN_PROGRESSION = 3
PROGRESSION_LENGTH_MIN = 5
PROGRESSION_LENGTH_MAX = 15
PROGRESSION_NUMBER_MIN = 1
PROGRESSION_NUMBER_MAX = 50
PROGRESSION_STEP_MIN = 1
PROGRESSION_STEP_MAX = 10


def show_game_conditions():
    print('What number is missing in the progression?')


def get_correct_answer(expression):
    str_nums_arr = expression.split(' ')
    array_of_nums_len = len(str_nums_arr)
    array_of_nums = []

    if array_of_nums_len < MIN_NUMBERS_COUNT_IN_PROGRESSION:
        return None

    for num in str_nums_arr:
        array_of_nums.append(
            int(num) if num != MISSED_NUMBER_DELIMITER else num
        )

    delimiter_index = array_of_nums.index(MISSED_NUMBER_DELIMITER)

    # missed first number
    if delimiter_index == 0:
        farther_number = array_of_nums[2]
        closer_number = array_of_nums[1]
        missed_number = closer_number - (farther_number - closer_number)
    # missed last number
    elif delimiter_index == len(array_of_nums) - 1:
        farther_number = array_of_nums[-3]
        closer_number = array_of_nums[-2]
        missed_number = closer_number + (closer_number - farther_number)
    else:
        farther_number = array_of_nums[delimiter_index + 1]
        closer_number = array_of_nums[delimiter_index - 1]
        missed_number = closer_number + (farther_number - closer_number) / 2

    return str(int(missed_number))


def get_question_value():
    progression_length = random.randint(
        PROGRESSION_LENGTH_MIN,
        PROGRESSION_LENGTH_MAX
    )
    progression_number = random.randint(
        PROGRESSION_NUMBER_MIN,
        PROGRESSION_NUMBER_MAX
    )
    progression_step = random.randint(
        PROGRESSION_STEP_MIN,
        PROGRESSION_STEP_MAX
    )
    progression_empty_index = random.randint(0, progression_length - 1)
    progression_string = ''

    index = 0

    while index < progression_length:
        progression_number_in_str_representation = '{}'\
            if index == progression_length - 1\
            else '{} '

        progression_number = progression_number \
            if index == 0 \
            else progression_number + progression_step

        if index != progression_empty_index:
            progression_string += progression_number_in_str_representation\
                .format(progression_number)
        else:
            progression_string += progression_number_in_str_representation\
                .format(MISSED_NUMBER_DELIMITER)
        index += 1

    return progression_string
