"""
App.py is responsible for orchestrating the chess game by utilizing the modules
developed in other files, but it does not contain the game logic itself.

Note: All the messages displayed during program execution are loaded from
the "dialogues.json" file.
"""

from game import Game
import json

path = "/home/javier/PycharmProjects/Chess2P/dialogues.json"
with open(path) as file:
    script = json.load(file)[0]


def play():
    print(script["Welcoming"])
    player1 = ask_the_name(script["Player1"], "Player 1")
    player2 = ask_the_name(script["Player2"], "Player 2")

    chess = Game(player1, player2)
    run = True
    print()

    # while run:
    print(chess.get_player_turn(script["Turn"]))
    print(chess)
    move = input(script["Move"] + "\n")
    print(chess.move_decipher(move))


def ask_the_name(message, default=None):
    var = input(message + " ")
    if var.strip():
        return var
    return default


if __name__ == "__main__":
    play()
