import random

MISSED_NUMBER_DELIMITER = '..'


def show_game_conditions():
    print('What number is missing in the progression?')


def get_correct_answer(expression):
    str_nums_arr = expression.split(' ')
    array_of_nums_len = len(str_nums_arr)
    array_of_nums = []

    if array_of_nums_len < 3:
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
    progression_length = random.randint(5, 15)
    progression_number = random.randint(1, 50)
    progression_step = random.randint(1, 10)
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
