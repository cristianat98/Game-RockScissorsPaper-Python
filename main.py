from game.board import GameBoard
from game.messages import INVALID_NUMBER_FORMAT, SELECT_NUMBER_VICTORIES


def run() -> None:
    try:
        number_victories = int(
            input(SELECT_NUMBER_VICTORIES)
        )
    except ValueError:
        raise ValueError(INVALID_NUMBER_FORMAT)

    board = GameBoard(number_victories)
    board.run()


if __name__ == "__main__":
    try:
        run()
    except Exception as error:
        print(str(error))
