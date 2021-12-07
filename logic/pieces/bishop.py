from .piece import Piece
from ..colors import Colors


class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.white_unicode_val = '\u2657'
        self.black_unicode_val = '\u265d'

    def generate_possible_moves(self, board, old_x, old_y):
        possible_moves = set()
        delta_x = [-1, 1]
        delta_y = [-1, 1]

        for dx in delta_x:
            for dy in delta_y:
                for diag in range(1, 8):
                    pos_x = dx * diag + old_x
                    pos_y = dy * diag + old_y
                    if board.move_on_board(pos_x, pos_y):
                        if board.board[pos_y][pos_x].piece is None:
                            possible_moves.add((pos_x, pos_y))
                        elif board.board[pos_y][pos_x].piece.color != \
                                self.color:
                            possible_moves.add((pos_x, pos_y))
                            break
                        elif board.board[pos_y][pos_x].piece.color == \
                                self.color:
                            break
                    else:
                        break

        return possible_moves
