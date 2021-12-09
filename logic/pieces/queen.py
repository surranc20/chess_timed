from .piece import Piece
from .bishop import Bishop
from .rook import Rook
from ..colors import Colors


class Queen(Piece):
    def __init__(self, color):
        """Create a Queen with a certain color.
        :param color: The color of a chess piece
        :type color: Color
        """
        super().__init__(color)
        self.white_unicode_val = '\u2655'
        self.black_unicode_val = '\u265b'

    def generate_possible_moves(self, board, old_x, old_y):
        """Generates all possible moves that a queen can make. It does not
        check to see if the move will leave a player checked. So not every
        move generated by this function is actually a valid move.
        :param board: The chess board
        :type board: Board
        :param old_x: The x location the piece is starting at
        :type old_x: Int
        :param old_y: The y location the piece is starting at
        :type old_y: Int
        :returns: List of all possible moves
        :rtype: List
        """
        # Queen is really just a bishop and rook combined
        rook = Rook(self.color)
        rook_options = rook.generate_possible_moves(board, old_x, old_y)

        bishop = Bishop(self.color)
        bishop_options = bishop.generate_possible_moves(board, old_x, old_y)

        possible_moves = set()
        possible_moves.update(rook_options)
        possible_moves.update(bishop_options)

        return possible_moves
