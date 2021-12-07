from .piece import Piece
from ..colors import Colors


class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.white_unicode_val = '\u2654'
        self.black_unicode_val = '\u265a'

    def generate_possible_moves(self, board, old_x, old_y):
        possible_moves = set()

        delta_x = [-1, 0, 1]
        delta_y = [-1, 0, 1]

        for dx in delta_x:
            for dy in delta_y:
                pos_x = old_x + dx
                pos_y = old_y + dy

                if board.move_on_board(pos_x, pos_y):
                    if board.board[pos_y][pos_x].piece is None:
                        possible_moves.add((pos_x, pos_y))
                    elif board.board[pos_y][pos_x].piece.color != self.color:
                        possible_moves.add((pos_x, pos_y))

        return possible_moves
