from ..colors import Colors


class Piece:
    def __init__(self, color):
        self.color = color
        self.white_unicode_val = None
        self.black_unicode_val = None
        self.moved = False

    def __repr__(self):
        if self.color == Colors.WHITE:
            return self.white_unicode_val
        else:
            return self.black_unicode_val

    def move_is_valid(self, board, old_x, old_y, new_x, new_y):
        possible_moves = \
            self.generate_possible_moves(board, old_x, old_y)

        if (new_x, new_y) in possible_moves:
            return True
        else:
            return False

    def generate_possible_moves(self, board, old_x, old_y):
        return []
