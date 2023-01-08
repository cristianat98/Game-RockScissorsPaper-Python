import random

from messages import (
    COMPUTER_WON_GAME,
    COMPUTER_WON_ROUND,
    INVALID_NUMBER_VICTORIES,
    INVALID_OPTION,
    NOBODY_WINS,
    SELECT_OPTION,
    USER_WON_GAME,
    USER_WON_ROUND
)
from variables import COMPUTER, PAPEL, PIEDRA, SALIR, TIJERA, USER


class GameBoard:
    """
    Class to manage the Board of the game Rock-Scissors-Paper
    """

    number_victories: int
    options: tuple = (PIEDRA, PAPEL, TIJERA, SALIR)

    def __init__(self, number_victories: int) -> None:
        """
        Function to initialize the number of the victories in the Board.

        This number have to be higher than 0
        """

        if number_victories <= 0:
            raise ValueError(INVALID_NUMBER_VICTORIES)

        self.number_victories = number_victories

    def run(self) -> None:

        victories_user = 0
        victories_computer = 0

        while (
            victories_user < self.number_victories
            and victories_computer < self.number_victories
        ):

            user_option = input(SELECT_OPTION)
            user_option = user_option.lower()
            if user_option not in self.options:
                print(INVALID_OPTION)
                continue
            if user_option == SALIR:
                break

            computer_option = random.choice(self.options[0:3])

            winner = self.determine_result(user_option, computer_option)
            if winner == USER:
                victories_user += 1
                print(USER_WON_ROUND)
            elif winner == COMPUTER:
                victories_computer += 1
                print(COMPUTER_WON_ROUND)

            self.print_result(victories_user, victories_computer)

        if victories_user > victories_computer:
            print(USER_WON_GAME)
        elif victories_computer > victories_user:
            print(COMPUTER_WON_GAME)
        else:
            print(NOBODY_WINS)

    def determine_result(self, user_option: str, computer_option: str) -> str:
        """
        Function to determine who wins with the given options

        Args:
            option_user (str): Option selected by the user
            option_computer (str): Option selected by the computer

        Returns:
            str: Winner or draw (In case the options are the same)
        """
        if user_option == computer_option:
            return "draw"

        if (
            user_option not in self.options or
            computer_option not in self.options
        ):
            raise ValueError(INVALID_OPTION)

        if user_option == PIEDRA:
            if computer_option == TIJERA:
                return USER
            else:
                return COMPUTER

        elif user_option == PAPEL:
            if computer_option == PIEDRA:
                return USER
            else:
                return COMPUTER

        else:
            if computer_option == PAPEL:
                return USER
            else:
                return COMPUTER

    def print_result(
        self, victories_user: int, victories_computer: int
    ) -> None:
        """
        Function to print the actual results
        """

        print("*" * 10)
        print(f"User victories: {victories_user}")
        print(f"Computer victories: {victories_computer}")
