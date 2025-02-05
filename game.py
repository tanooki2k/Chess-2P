class Game:
    blocks = {"white": "O", "black": "#"}  # The symbol that represent the chess' blocks.

    def __init__(self, player1="Player 1", player2="Player 2"):
        self.board = [
            [self.blocks["white"] if (i * 7 + j) % 2 else self.blocks["black"] for j in range(8)]
            for i in range(8)
        ]
        self.player1 = player1
        self.player2 = player2

    def __repr__(self):
        col = '  '.join([chr(i + 65) for i in range(len(self.board))])
        game_board = f"\t{col}\n"  # Create the guide A-H columns coordinates.
        for row_idx in range(len(self.board)):  # Generate all the Chess bord with its respective blocks and pieces.
            game_board += f"{8 - row_idx}\t"
            for col in self.board[row_idx]:
                game_board += col + "  "
            game_board += "\n"

        return game_board  # Return the chess board
