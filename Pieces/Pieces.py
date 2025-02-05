import json


class Pieces:
    alive = 0

    def __init__(self, piece, team):
        self.pieces = piece
        self.team = team

    def move(self):
        pass


with open('../pieces.json') as file:
    pieces = json.load(file)

black_pieces, white_pieces = pieces

if __name__ == "__main__":
    print(black_pieces)
    print(white_pieces)
