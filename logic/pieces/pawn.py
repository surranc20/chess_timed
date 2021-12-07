from .piece import Piece
from ..colors import Colors


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.white_unicode_val = '\u2659'
        self.black_unicode_val = '\u265F'
        self.moved = False

    def generate_possible_moves(self, board, old_x, old_y):
        delta = 1 if self.color == Colors.WHITE else - 1
        distance = 1 if self.moved else 2
        possible_moves = set()
        for y in range(1, distance + 1):
            pos_y = old_y + y * delta

            if not board.move_on_board(old_x, pos_y):
                continue

            if board.board[pos_y][old_x].piece is None:
                if y == 1:
                    possible_moves.add((old_x, pos_y))
                elif y == 2 and \
                        board.board[pos_y - delta][old_x].piece is None:
                    possible_moves.add((old_x, pos_y))

        for x in [-1, 1]:
            pos_x = old_x + x
            pos_y = old_y + delta
            if not board.move_on_board(pos_x, pos_y):
                continue

            pos_piece = board.board[pos_y][pos_x].piece
            if pos_piece is not None and pos_piece.color != self.color:
                possible_moves.add((pos_x, pos_y))

        return possible_moves
