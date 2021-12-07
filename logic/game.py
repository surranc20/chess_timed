from .pieces.king import King


class Game:
    """Game class that contains the main function for the chess game (move).
    The main function in main.py simply runs move over and over again until
    the game is over."""

    def __init__(self, board, player_1, player_2):
        """Creates a game object.
        :param board: The board the game will be played on.
        :type board: Board
        :param player_1: Player who will go first and use the white pieces.
        :type player_1: Player
        :param player_2: Player who will go second and use the black pieces.
        :type player_2: Player
        """
        self.board = board
        self.game_over = False
        self.player_1 = player_1
        self.player_2 = player_2

        self.turn = 0

    def is_over(self):
        """Returns whether or not the game is over.

        :returns: Whether or not the game is over
        :rtype: boolean
        """
        return self.game_over

    def move(self):
        """Executes a single players turn."""

        # Use turn number to figure out whose turn it actually is.
        if self.turn % 2 == 0:
            moving = self.player_1
            opponent = self.player_2
        else:
            moving = self.player_2
            opponent = self.player_1

        # Repeatedly ask player for desired move until they enter a valid move.
        while True:
            piece_choice = self.get_piece_choice(moving)
            move_choice = self.get_move_choice(piece_choice, moving, opponent)

            # Player can stay in this loop by pressing 'q' in move_choice func.
            # This will have them stay in the loop. Otherwise break.
            if move_choice != "repick":
                break

        self.move_piece(piece_choice, move_choice, moving, opponent)

        # Check to see if the opponent is mated.
        if not self.can_escape(opponent):
            self.winner = moving
            self.game_over = True

        self.turn += 1

    def move_piece(self, piece_choice, move_choice, moving, opponent):
        """Moves a piece between two squares. Captures opponent's piece should
        it exist.
        :param piece_choice: The location of the piece to move.
        :type piece_choice: String (Two chars long. Column Row ex. A7, D8...)
        :param move_choice: The location of the square to move to.
        :type move_choice: String (Two chars long. Column Row ex. A7, D8...)
        :param moving: The player whose turn it is.
        :type moving: Player
        :param opponent: The player not moving.
        :type opponent: Player
        """
        # Extract the x, y coords from piece and move locations.
        px, py = self.parse_board_choice(piece_choice)
        mx, my = self.parse_board_choice(move_choice)

        # Grab the pieces that exist at said locations.
        piece = self.board.board[py][px].piece
        target_piece = self.board.board[my][mx].piece

        # Change the location of the piece in the players piece map.
        moving.pieces[piece] = (mx, my)

        # Get rid of the opponents piece if necessary.
        if target_piece is not None:
            opponent.pieces.pop(target_piece)

        # Move piece
        self.board.board[py][px].piece = None
        self.board.board[my][mx].piece = piece

    def get_piece_choice(self, moving):
        """Ask the player what piece they want to move.
        :param moving: The player whose turn it is
        :type moving: Player

        :returns: The location of the piece to move
        :rtype: string of length 2 (ex. A7, D8...)
        """

        # Ask the player what piece to move repeatedly until a valid piece is
        # selected.
        while True:
            print(f'\n{moving.color.value}\'s turn')
            piece_choice = input("Input piece to move... ").upper()

            # Check to see if the player can move this piece.
            validate_piece = self.piece_is_valid(piece_choice, moving)
            if validate_piece is True:
                break
            elif validate_piece == "enemy":
                print("That's not your piece!")
            elif validate_piece is None:
                print("There is no piece there!")
            elif validate_piece == "invalid":
                print("Input invalid!")
                print("Please input a valid piece.")
                print("Input should be the desired column " +
                      "then row with no spaces (ex. A7).")

        return piece_choice

    def piece_is_valid(self, piece_choice, player):
        """Checks to see if the player can move the piece at specified
        location.

        :param piece_choice: Location of piece to move
        :type piece_choice: String
        :param player: Player who is currently moving
        :type player: Player

        :returns: None, Boolean, or String (that contains info on why move is
                  invalid)
        """
        # See if the location is a valid location.
        if not self.valid_board_location(piece_choice):
            return "invalid"

        # Get x, y coords from the string input and grab the piece at said pos.
        x, y = self.parse_board_choice(piece_choice)
        piece = self.board.board[y][x].piece

        # See if the player can move said piece.
        if piece is None:
            return None
        elif piece.color == player.color:
            return True
        else:
            return "enemy"

    def get_move_choice(self, piece_location, moving, opponent):
        """Gets the location of the square the player wants to move to.

        :param piece_location: The location of the piece to be moved
        :type piece_location: String (of len 2 with Column then Row ex A7)
        :param moving: Player who is currently trying to move
        :type moving: Player
        :param opponent: Player who is not moving
        :type opponent: Player

        :returns: The location the player wants to move
        :rtype: String
        """
        # Repeatedly ask player to input move location until one is valid.
        while True:
            move_choice = input("Input desired move location " +
                                "(or press q to pick new piece)... ").upper()

            # Player can enter q if they want to select a new piece to move.
            if move_choice == "Q":
                return "repick"

            # See if the move is a valid move and proceed accordingly.
            validate_choice = self.move_is_valid(
                piece_location, move_choice, moving, opponent)

            if validate_choice is True:
                break
            else:
                print("Move is invalid.")

        return move_choice

    def move_is_valid(self, piece_location, move_choice, moving, opponent):
        """Checks to see if a move is a valid move.
        :param piece_location: Location of the piece to be moved
        :type piece_location: String (len 2 with format Column Row ex. A7)
        :param move_choice: Where the player wants to move to
        :type move_choice: String (len 2 with format Column Row ex. A7)
        :param moving: Player who is moving
        :type moving: Player
        :param opponnent: Player not moving
        :type opponent: Player

        :returns: Whether or not the move is valid
        :rtype: Boolean
        """
        # Check to see if desired move location is on board
        if not self.valid_board_location(move_choice):
            return "invalid"

        # Grab the piece being moved.
        old_x, old_y = self.parse_board_choice(piece_location)
        piece = self.board.board[old_y][old_x].piece

        # Grab the coords of the square to move to.
        x, y = self.parse_board_choice(move_choice)

        # Check to see if a given piece can make said move.
        if piece.move_is_valid(self.board, old_x, old_y, x, y):

            # Make sure the player does not check themselves with move.
            if self.temp_move_is_checked(piece_location, move_choice,
                                         moving, opponent):
                print("This move leaves you checked!")
                return False

            # Move is valid and they don't check themselves
            return True

        # Move was not on the board.
        else:
            return False

    def temp_move_is_checked(self, piece_location, move_choice,
                             moving, opponent, parsed=False):
        if not parsed:
            px, py = self.parse_board_choice(piece_location)
            mx, my = self.parse_board_choice(move_choice)
        else:
            px, py = piece_location
            mx, my = move_choice
        piece = self.board.board[py][px].piece
        target_piece = self.board.board[my][mx].piece

        moving.pieces[piece] = (mx, my)
        if target_piece is not None:
            opponent.pieces.pop(target_piece)

        self.board.board[py][px].piece = None
        self.board.board[my][mx].piece = piece

        checked = self.is_checked(moving)

        moving.pieces[piece] = (px, py)
        if target_piece is not None:
            opponent.pieces[target_piece] = (mx, my)
        self.board.board[py][px].piece = piece
        self.board.board[my][mx].piece = target_piece

        if checked:
            return True
        else:
            return False

    def valid_board_location(self, location):
        if len(location) != 2:
            return False
        if location[0] not in ["A", "B", "C", "D", "E", "F", "G", "H"]:
            return False
        if location[1] not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            return False
        return True

    def parse_board_choice(self, move_choice):
        x, y = ord(move_choice[0]) - 65, int(move_choice[1]) - 1
        return (x, y)

    def is_checked(self, player):
        if player is self.player_1:
            op = self.player_2
        else:
            op = self.player_1

        king_loc = None
        for piece in player.pieces:
            if type(piece) is King:
                king_loc = player.pieces[piece]

        for piece, location in op.pieces.items():
            x, y = location
            if king_loc in piece.generate_possible_moves(self.board, x, y):
                return True

        return False

    def can_escape(self, player):
        if player is self.player_1:
            op = self.player_2
        else:
            op = self.player_1

        for piece, location in player.pieces.items():
            x, y = location

            for move in piece.generate_possible_moves(self.board, x, y):
                if not self.temp_move_is_checked((x, y), move, player,
                                                 op, True):
                    return True
        return False
