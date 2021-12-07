from logic.player import Player
from logic.board import Board
from logic.colors import Colors
from logic.game import Game


def main():
    """Main loop for the chess game. Creates chess game and prints winner when
    the game is over"""
    player_1 = Player(Colors.WHITE)
    player_2 = Player(Colors.BLACK)
    board = Board(player_1, player_2)
    game = Game(board, player_1, player_2)

    while not game.is_over():
        print(f'\n{board}')
        game.move()

    print(f'{game.winner.color.value} won in {game.turn} moves!')


if __name__ == '__main__':
    main()

# TODO: en passant, castle, promote
