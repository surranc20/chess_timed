class Square:
    """Square class that emulates a square you would see on a chess board. A
    square can possible hold a piece and the square will be either white or
    black."""

    def __init__(self, color, x, y, piece=None):
        """Creates a square with a given color, position, and possible piece.

        :param color: Color for the square
        :type color: Should be an enumerated Color value (either Colors.WHITE
                     or Colors.BLACK)
        :param x: X coordinate of the square
        :type x: Positive integer
        :param y: Y coordinate of the square
        :type y: Positive integer
        :param piece: Chess piece the square holds
        :type piece: None or Piece
        """
        self.color = color
        self.piece = piece
        self.pos = (x, y)

    def __repr__(self):
        """Defines how a square should look when printed to the terminal

        :returns: | | or | piece |
        :rtype: String
        """
        # Only the first square gets a |. This avoids having two || between
        # squares.
        start = "|" if self.pos[0] == 0 else ""
        end = "|"

        if self.piece is None:
            piece = self.color.value[0]
        else:
            piece = str(self.piece)

        return start + piece + end
