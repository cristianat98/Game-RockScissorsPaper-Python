import logging
from game.board import GameBoard
from game.messages import (
    INVALID_NUMBER_FORMAT,
    INVALID_NUMBER_PLAYERS,
    SELECT_NUMBER_PLAYERS,
    SELECT_NUMBER_VICTORIES
)
from game.variables import COMPUTER, USER


logger = logging.getLogger(__name__)


def run() -> None:
    try:
        number_players = int(input(SELECT_NUMBER_PLAYERS))
        logger.info(f"Number of players: {number_players}")
        number_victories = int(
            input(SELECT_NUMBER_VICTORIES)
        )
        logger.info(f"Number of needed victories: {number_victories}")
    except ValueError:
        raise ValueError(INVALID_NUMBER_FORMAT)

    if number_players not in [1, 2]:
        raise ValueError(INVALID_NUMBER_PLAYERS)

    if number_players == 1:
        player_2 = COMPUTER
    else:
        player_2 = USER

    board = GameBoard(number_victories, USER, player_2)
    board.run()


if __name__ == "__main__":
    try:
        run()
    except Exception as error:
        logger.error(str(error))
