from .colors import Colors
from .square import Square
from .pieces.pawn import Pawn
from .pieces.rook import Rook
from .pieces.queen import Queen
from .pieces.king import King
from .pieces.bishop import Bishop
from .pieces.knight import Knight


class Board:
    def __init__(self, player_1, player_2):
        self.board = []
        colors = [Colors.WHITE, Colors.BLACK]
        piece_locs = self.place_initial_pieces()

        colors_index = 0
        for y in range(8):
            row = []
            for x in range(8):
                if (x, y) in piece_locs:
                    piece = piece_locs[(x, y)]
                    if piece.color == Colors.WHITE:
                        player_1.pieces[piece] = (x, y)
                    else:
                        player_2.pieces[piece] = (x, y)
                else:
                    piece = None
                row.append(Square(colors[colors_index % 2], x, y, piece))
                colors_index += 1
            colors_index += 1
            self.board.append(row)

    def __repr__(self):
        board = ["   A B C D E F G H"]
        for row_num, row in enumerate(self.board):
            row_string = [str(row_num + 1) + " "]
            for square in row:
                row_string.append(str(square))
            board.append("".join(row_string))
        board.append("   A B C D E F G H")
        return "\n".join(board)

    def place_initial_pieces(self):
        locs = {}
        back_row_pieces = [Rook, Knight, Bishop,
                           Queen, King, Bishop, Knight, Rook]
        for x in range(8):
            locs[(x, 1)] = Pawn(Colors.WHITE)
            locs[(x, 0)] = back_row_pieces[x](Colors.WHITE)

            locs[(x, 6)] = Pawn(Colors.BLACK)
            locs[(x, 7)] = back_row_pieces[x](Colors.BLACK)

        return locs

    def move_on_board(self, x, y):
        return 0 <= x <= 7 and 0 <= y <= 7
