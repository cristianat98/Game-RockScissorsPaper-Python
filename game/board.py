from game.player import Player
from game.messages import (
    INVALID_NUMBER_VICTORIES,
    INVALID_OPTION,
    NOBODY_WINS,
    PLAYER_WON_GAME,
    PLAYER_WON_ROUND
)
from game.constants import OPTIONS_AVAILABLE, ROCK, SCISSOR, PAPER, EXIT


class GameBoard:
    """
    Class to manage the Board of the game Rock-Scissors-Paper
    """

    PLAYER_1: Player
    PLAYER_2: Player
    NUMBER_VICTORIES: int
    OPTIONS: tuple = OPTIONS_AVAILABLE

    def __init__(
        self, number_victories: int, player_1: str, player_2: str
    ) -> None:
        """
        Function to initialize the number of the victories in the Board.

        This number have to be higher than 0
        """

        if number_victories <= 0:
            raise ValueError(INVALID_NUMBER_VICTORIES)

        self.PLAYER_1 = Player(player_1, "Player 1")
        self.PLAYER_2 = Player(player_2)
        self.NUMBER_VICTORIES = number_victories

    def run(self) -> None:

        victories_player_1 = 0
        victories_player_2 = 0

        while (
            victories_player_1 < self.NUMBER_VICTORIES
            and victories_player_2 < self.NUMBER_VICTORIES
        ):

            option_1 = self.PLAYER_1.select_option()
            option_2 = self.PLAYER_2.select_option()
            if option_1 == EXIT or option_2 == EXIT:
                break
            winner = self.determine_result(option_1, option_2)
            if winner == 1:
                victories_player_1 += 1
                print(PLAYER_WON_ROUND.format(str(winner)))
            elif winner == 2:
                victories_player_2 += 1
                print(PLAYER_WON_ROUND.format(str(winner)))

            self.print_result(victories_player_1, victories_player_2)

        if victories_player_1 > victories_player_2:
            print(PLAYER_WON_GAME.format("1"))
        elif victories_player_2 > victories_player_1:
            print(PLAYER_WON_GAME.format("2"))
        else:
            print(NOBODY_WINS)

    def determine_result(self, option_1: str, option_2: str) -> int:
        """
        Function to determine who wins with the given options

        Args:
            option_1 (str): Option selected by the player 1
            option_2 (str): Option selected by the player 2

        Returns:
            int: 1 in case Player 1 wins, 2 in case Player 2 wins
                 or 0 in case nobody wins
        """

        if (
            option_1 not in self.OPTIONS
            or option_2 not in self.OPTIONS
        ):
            raise ValueError(INVALID_OPTION)

        if option_1 == option_2:
            return 0

        if option_1 == ROCK and option_2 == SCISSOR:
            return 1
        elif option_1 == PAPER and option_2 == ROCK:
            return 1
        elif option_1 == SCISSOR and option_2 == PAPER:
            return 1
        else:
            return 2

    def print_result(
        self, victories_user: int, victories_computer: int
    ) -> None:
        """
        Function to print the actual results
        """

        print("*" * 10)
        print(f"User victories: {victories_user}")
        print(f"Computer victories: {victories_computer}")
