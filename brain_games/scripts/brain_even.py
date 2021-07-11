#!/usr/bin/env python
import brain_games.cli_common
import brain_games.cli_brain_even


def main():
    user_name = brain_games.cli_common.welcome_user()
    brain_games.cli_brain_even.show_game_conditions()
    brain_games.cli_brain_even.show_and_handle_questions(user_name)


if __name__ == '__main__':
    main()
