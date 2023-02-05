"""
INPUT MESSAGES
"""
SELECT_NUMBER_VICTORIES = "Select the number of the needed victories: "
SELECT_NUMBER_PLAYERS = "Select the number of the players (1 or 2): "
SELECT_OPTION = "Select your option (piedra, papel, tijera, salir): "

"""
SINGLE MESSAGES
"""
PLAYER_WON_ROUND = "Player {} won the round"
PLAYER_WON_GAME = "Player {} won the game.\nCongratulations!!!"
# COMPUTER_WON_GAME = "Player {} won the game.\nBest luck next time!!!"
NOBODY_WINS = "You decided to leave the game with a tied score"

"""
ERRORS
"""
INVALID_NUMBER_FORMAT = "ERROR: The input is not a number"
INVALID_NUMBER_VICTORIES = "ERROR: The number of the victories is not valid"
INVALID_NUMBER_PLAYERS = "ERROR: The number of players is not valid"
INVALID_OPTION = "ERROR: This option is not a valid option"
INVALID_PLAYER = "ERROR: This type of player doesn't exist. It has to be computer or user"  # NOQA
