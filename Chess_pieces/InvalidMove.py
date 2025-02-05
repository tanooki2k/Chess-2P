"""
Defines custom error classes for handling invalid moves in the game.
"""


class InvalidMoveError(ValueError):
    def __init__(self, move):
        super().__init__(
            f"Invalid move: '{move}'. This move is either not allowed for the selected piece or violates the movement rules.")


class OutOfBoundsError(ValueError):
    def __init__(self, move):
        super().__init__(
            f"Invalid move: '{move}'. This move is out of bounds.")
