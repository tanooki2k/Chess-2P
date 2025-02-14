"""
Defines the base configuration for all chess pieces as a parent class,
including display attributes for each piece.

Note: The child classes inheriting from this class implement 
the specific movement logic for each piece.
"""
import json


class Common:
    alive = 0

    def __init__(self, kind=None, team=None):
        self.type = kind
        self.team = team

        if kind is not None:
            try:
                self.display = pieces[f"{self.team}"][f"{self.type}"]
            except KeyError:
                raise KeyError(
                    f"Invalid piece configuration: Type '{self.type}' or Team '{self.team}' is not defined. Please check the pieces definition.")

    def move(self):
        pass



pieces={
"White": {
      "Pawn": "♟",  "Rook": "♜",
      "Knight": "♞", "Bishop": "♝",
      "Queen": "♛","King": "♚"
    },

"Black": {
      "Pawn": "♙", "Rook": "♖",
      "Knight": "♘", "Bishop": "♗",
      "Queen": "♕", "King": "♔"
    }
}



r"""
path = r'C:\Users\Student 01\Downloads\\Chess-2P\pieces.json'
with open(path) as file:
    pieces = json.load(file)[0]
    
"""

if __name__ == "__main__":
    print(pieces)
