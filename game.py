class Game:
    blocks = {"white": "O", "black": "#"}

    def __init__(self, player1="Player 1", player2="Player 2"):
        self.board = [[self.blocks["white"] if i % 2 else self.blocks["black"] for i in range(8)] for _ in range(8)]
        self.player1 = player1
        self.player2 = player2

    def __repr__(self):
        game_board = ""
        for row in self.board:
            for col in row:
                game_board += col + "  "
            game_board += "\n"
        return game_board
