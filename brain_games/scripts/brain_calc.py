#!/usr/bin/env python
import brain_games.cli_common
import brain_games.games.brain_calc
import brain_games.games.common_logic


def main():
    user_name = brain_games.cli_common.welcome_user()
    brain_games.games.brain_calc.show_game_conditions()
    brain_games.games.common_logic.show_and_handle_questions(
        brain_games.games.brain_calc.get_correct_answer,
        brain_games.games.brain_calc.get_question_value,
        user_name
    )


if __name__ == '__main__':
    main()
