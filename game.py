"""
Game.py is responsible for setting up the chessboard, placing the pieces, 
implementing the score system, and defining the rules of the game.

Note 1: It does not control individual pieces directly; their behavior is 
defined in separate scripts located in the Chess_pieces folder.

Note 2: To customize the appearance of the pieces, edit the "pieces.json" 
file where their attributes are defined.
"""
from Chess_pieces.Common import Common
import json


class Game:
    blocks = {
        "white": "O",  # Representation of white squares on the chessboard.
        "black": "#"  # Representation of black squares on the chessboard.
    }
    turn = {"number": 1,
            "color": "white"}  # Stores the current turn number and specifies whether it's White or Black's turn.
    victory_by = None

    def __init__(self, player1="Player 1", player2="Player 2"):
        self.board = [
            [Common()] * 7 + [Common("Pawn", "White")],
            [Common()] * 8,
            [Common()] * 8,
            [Common()] * 8,
            [Common()] * 8,
            [Common()] * 8,
            [Common()] * 8,
            [Common("Pawn", "Black"), Common("King", "Black")] + [Common()] * 6
        ]  # The chessboard is represented as a 8x8 matrix of Common objects, with some initialized pieces in their starting positions.

        self.players = {
            "white": player1,
            "black": player2
        }  # Stores the players' names, associating them with the respective teams (White and Black).
        self.pieces = {
            "Black": [piece for row in self.board for piece in row if piece.team == "Black"],
            "White": [piece for row in self.board for piece in row if piece.team == "White"]
        }  # Collect all the pieces created for both players and stored it.

        self.rows, self.cols = len(self.board), len(self.board[0])  # Defines the size of the board.

        mean_rows = sum([len(row) for row in self.board]) / self.rows
        if mean_rows != self.cols:
            raise ValueError(
                "The provided board matrix is irregular. Ensure every row has the same number of columns to correctly define the chessboard.")

    def __repr__(self):
        """
        Generates a string representation of the chessboard in its current state, 
        including column labels, row numbers, and the placement of pieces.
        :return: A string rendering of the chess game board.
        """

        spacer = "\t"  # Defines the separation symbol between columns and row labels for the chessboard display.
        cols = '  '.join([chr(i + 65) for i in range(len(self.board))])

        game_board = f"{spacer}\t{cols}\n"  # Adds column labels (A-H) to the top of the board for reference.

        for row_idx in range(-1, -self.rows - 1,
                             -1):  # Iterates through rows from top to bottom to construct the board's visual representation.
            game_board += f"{spacer}{self.rows + 1 + row_idx}\t"  # Appends the row number on the left for easier navigation.
            for col_idx in range(self.cols):
                if self.board[row_idx][col_idx].team is not None:
                    game_board += f"{self.board[row_idx][col_idx].display}  "
                else:
                    game_board += f"{self.blocks['black'] if (row_idx * 7 + col_idx) % 2 else self.blocks['white']}  "
            game_board += "\n"

        return game_board  # Returns the completed chessboard rendering as a string.

    def get_player_turn(self, message=""):
        player_name = self.players[
            f"{self.turn['color']}"]  # Retrieves the name of the player whose turn it currently is based on the team's color.
        return f"Turn {self.turn['number']} - {player_name}{message}\n"

    @staticmethod
    def move_decipher(move):
        lower_move = move.lower()  # Converts the input move notation to lowercase for consistent parsing.

        try:
            piece = lower_move[0]  # Extracts the piece identifier from the move string (e.g., 'Q' for Queen, 'P' for Pawn).
        except IndexError:
            return errors["InvalidFormatMove"].replace("{move}", move)

        try:
            current_position, destination = lower_move[1:].split('-')
        except ValueError:
            return errors["InvalidLengthMove"].replace("{move}",
                                                       move)  # Returns a predefined error message if the input move format is invalid.
        return piece, current_position, destination


path = r"C:\Users\Student 01\Downloads\Chess-2P\errors_messages.json"
with open(path) as file:
    errors = json.load(file)[0]
