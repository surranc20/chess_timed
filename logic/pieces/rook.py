from .piece import Piece
from ..colors import Colors


class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.white_unicode_val = '\u2656'
        self.black_unicode_val = '\u265C'

    def generate_possible_moves(self, board, old_x, old_y):
        possible_moves = set()
        delta_x = [-1, 1]
        delta_y = [-1, 1]

        for dx in delta_x:
            for x in range(1, 8):
                pos_x = dx * x + old_x
                if board.move_on_board(pos_x, old_y):
                    if board.board[old_y][pos_x].piece is None:
                        possible_moves.add((pos_x, old_y))
                    elif board.board[old_y][pos_x].piece.color != self.color:
                        possible_moves.add((pos_x, old_y))
                        break
                    else:
                        break
                else:
                    break

        for dy in delta_y:
            for y in range(1, 8):
                pos_y = dy * y + old_y
                if board.move_on_board(old_x, pos_y):
                    if board.board[pos_y][old_x].piece is None:
                        possible_moves.add((old_x, pos_y))
                    elif board.board[pos_y][old_x].piece.color != self.color:
                        possible_moves.add((old_x, pos_y))
                        break
                    else:
                        break
                else:
                    break

        return possible_moves
