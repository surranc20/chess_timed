class Player:
    """Player class. Could be extended to include things like a name, record,
    etc. Currently keeps track of the players pieces and their color."""

    def __init__(self, color):
        """Creates a player object with a given color.
        :param color: Color of the pieces the player will use
        :type color: Enumerated Color value (Colors.WHITE, or Colors.BLACK)
        """
        self.color = color
        self.pieces = {}
