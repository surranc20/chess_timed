from .piece import Piece
from .bishop import Bishop
from .rook import Rook
from ..colors import Colors


class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.white_unicode_val = '\u2655'
        self.black_unicode_val = '\u265b'

    def generate_possible_moves(self, board, old_x, old_y):
        rook = Rook(self.color)
        rook_options = rook.generate_possible_moves(board, old_x, old_y)

        bishop = Bishop(self.color)
        bishop_options = bishop.generate_possible_moves(board, old_x, old_y)

        possible_moves = set()
        possible_moves.update(rook_options)
        possible_moves.update(bishop_options)

        return possible_moves
