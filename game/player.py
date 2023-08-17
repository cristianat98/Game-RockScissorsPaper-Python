import logging
import random

from game.messages import INVALID_OPTION, INVALID_PLAYER, SELECT_OPTION
from game.constants import COMPUTER, OPTIONS_AVAILABLE, USER

logger = logging.getLogger(__name__)


class Player:
    TYPE: str
    NAME: str
    OPTIONS: tuple = OPTIONS_AVAILABLE

    def __init__(self, type: str, name: str = None) -> None:
        """Constructor of the Class

        Args:
            type (str): Type of the player: user or computer
            name (str): Name of the player
        """

        if type not in [COMPUTER, USER]:
            logger.error(INVALID_PLAYER)
            raise ValueError(INVALID_PLAYER)

        if type == COMPUTER:
            self.NAME = COMPUTER
        else:
            self.NAME = name if name else "Player 1"

        self.TYPE = type

    def select_option(self) -> str:
        """Function to select an option to play

        Returns:
            str: Option chosen by the player
        """

        if self.TYPE == COMPUTER:
            option = random.choice(self.OPTIONS[0:3])
        else:
            valid_option = False
            while not valid_option:
                option = input(SELECT_OPTION)
                option = option.lower()
                if option not in self.OPTIONS:
                    print(INVALID_OPTION)
                else:
                    valid_option = True

        return option
