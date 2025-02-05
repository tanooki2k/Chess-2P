"""
Game.py is responsible for setting up the chessboard, placing the pieces, 
implementing the score system, and defining the rules of the game.

Note 1: It does not control individual pieces directly; their behavior is 
defined in separate scripts located in the Chess_pieces folder.

Note 2: To customize the appearance of the pieces, edit the "pieces.json" 
file where their attributes are defined.
"""
from Chess_pieces.Common import Common


class Game:
    blocks = {
        "white": "O",
        "black": "#"
    }  # Symbols used to visually represent the chessboard's alternating white and black squares.
    turn = {"number": 1, "color": "white"}  # Tracks the current turn number and the color of the player who has to move

    def __init__(self, player1="Player 1", player2="Player 2"):
        self.board = [
            [Common("Pawn", "Black"), Common("King", "Black"), 0, 0, 0, 0, 0, 0],
            [0] * 8,
            [0] * 8,
            [0] * 8,
            [0] * 8,
            [0] * 8,
            [0] * 8,
            [0, 0, 0, 0, 0, 0, 0, Common("Pawn", "White")]

        ]
        self.players = {"white": player1, "black": player2}

    def __repr__(self):
        cols = '  '.join([chr(i + 65) for i in range(len(self.board))])

        game_board = f"\t{cols}\n"  # Create the guide A-H columns coordinates.

        for row_idx in range(
                len(self.board)):  # Loop through each row to construct the chessboard representation, including pieces and squares.
            game_board += f"{8 - row_idx}\t"
            for col_idx in range(len(self.board[row_idx])):
                if self.board[row_idx][col_idx]:
                    game_board += f"{self.board[row_idx][col_idx].display}  "
                else:
                    game_board += f"{self.blocks['black'] if (row_idx * 7 + col_idx) % 2 else self.blocks['white']}  "
            game_board += "\n"

        return game_board  # Return the chess board

    def get_player_turn(self, message=""):
        player_name = self.players[f"{self.turn['color']}"]  # Get the name of the player's turn
        return f"Turn {self.turn['number']} - {player_name}{message}"
