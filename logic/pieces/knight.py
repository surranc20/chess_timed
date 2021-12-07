from .piece import Piece
from ..colors import Colors


class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.white_unicode_val = '\u2658'
        self.black_unicode_val = '\u265e'

    def generate_possible_moves(self, board, old_x, old_y):
        possible_moves = set()
        possible_ls = [(2, 1), (2, -1), (1, 2), (1, -2), (-1, 2),
                       (-1, -2), (-2, 1), (-2, -1)]

        for move in possible_ls:
            x, y = move
            pos_x = x + old_x
            pos_y = y + old_y
            if board.move_on_board(pos_x, pos_y):
                if board.board[pos_y][pos_x].piece is None:
                    possible_moves.add((pos_x, pos_y))
                elif board.board[pos_y][pos_x].piece.color != self.color:
                    possible_moves.add((pos_x, pos_y))

        return possible_moves
