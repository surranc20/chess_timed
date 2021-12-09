from .colors import Colors
from .square import Square
from .pieces.pawn import Pawn
from .pieces.rook import Rook
from .pieces.queen import Queen
from .pieces.king import King
from .pieces.bishop import Bishop
from .pieces.knight import Knight


class Board:
    """Board class that stores all the chess pieces."""

    def __init__(self, player_1, player_2):
        """Creates a board object and initializes/assigns all the chess
        pieces.
        :param player_1: The player using the white pieces
        :type player_1: Player
        :param player_2: The player using the black pieces
        :type player_2: Player
        """
        self.board = []
        colors = [Colors.WHITE, Colors.BLACK]

        # Dictionary that contains the starting locations of chess pieces.
        piece_locs = self.place_initial_pieces()

        # Use colors index variable to properly assign colors to Squares
        colors_index = 0
        for y in range(8):
            row = []
            for x in range(8):
                # Check to see if this location starts with a piece.
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
        """Returns the str version of the board.
        :returns: Str version of the board
        :rtype: String
        """
        board = ["   A B C D E F G H"]
        for row_num, row in enumerate(self.board):
            row_string = [str(row_num + 1) + " "]
            for square in row:
                row_string.append(str(square))
            board.append("".join(row_string))
        board.append("   A B C D E F G H")
        return "\n".join(board)

    def place_initial_pieces(self):
        """"Creates a dictionary with chess pieces and their start locations.
        :returns: Dictionary with pieces and their locations
        :rtype: Dictionary
        """
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
        """Checks to see if a move is on the board
        :param x: X location
        :type x: Int
        :param y: Y location
        :type y: Int
        :returns: Whether or not an (x, y) pair is on the board
        :rtype: Boolean
        """
        return 0 <= x <= 7 and 0 <= y <= 7
