from time import sleep
from shipboard import ShipBoard
from guessboard import GuessBoard


SHIP_INFO = [
    ("Aircraft Carrier", 5),
    ("Battleship", 4),
    ("Submarine", 3),
    ("Cruiser", 3),
    ("Patrol Boat", 2)
]

BOARD_SIZE = 10
VERTICAL_SHIP = '|'
HORIZONTAL_SHIP = '-'

MISS = '.'
HIT = '*'
SUNK = '#'

P1_BOARD = None
P1_GUESSES_BOARD = None
p1_ship_coords = None
P2_BOARD = None
P2_GUESSES_BOARD = None
p2_ship_coords = None


def reset_boards():
    global P1_BOARD
    global P1_GUESSES_BOARD
    global p1_ship_coords
    global P2_BOARD
    global P2_GUESSES_BOARD
    global p2_ship_coords

    P1_BOARD = [
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
    ]

    P1_GUESSES_BOARD = [
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
    ]
    p1_ship_coords = {
        'Aircraft Carrier': [0, []],
        'Battleship': [0, []],
        'Submarine': [0, []],
        'Cruiser': [0, []],
        'Patrol Boat': [0, []]
    }
    P2_BOARD = [
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
    ]

    P2_GUESSES_BOARD = [
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
    ]
    p2_ship_coords = {
        'Aircraft Carrier': [0, []],
        'Battleship': [0, []],
        'Submarine': [0, []],
        'Cruiser': [0, []],
        'Patrol Boat': [0, []]
    }


def clear_screen():
    print("\033c", end="")


def print_board_heading():
    print("   " + " ".join([chr(c) for c in range(ord('A'),
          ord('A') + BOARD_SIZE)]))


def print_board(board):
    print_board_heading()

    row_num = 1
    for row in board:
        print(str(row_num).rjust(2) + " " + (" ".join(row)))
        row_num += 1


def display_boards(player, ship_board, guess_board):
    print('{}\'s turn'.format(player))
    print()  # Add a blank line
    print('Guesses:')
    print_board(guess_board)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Ships:')
    print_board(ship_board)
    print()  # Add a blank line


def end_turn(player):
    input('Switch players...')
    clear_screen()
    input('{}, hit ENTER to continue.'.format(player))
    clear_screen()


def display_end_screen(player1, player1_board, player2, player2_board):
    # Player 1 and player 2 here do not refer to the actually players
    # in the game; they refer to the order within just this function.
    print('{} is the winner!'.format(player1))
    print('{}\'s board:'.format(player1))
    print_board(player1_board)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('{}\'s board:'.format(player2))
    print_board(player2_board)
    print()  # Add a blank line


class Game:

    def play_again(self, replay):
        if replay[0].lower() == 'y':
            return True
        else:
            return False

    def play(self):
        clear_screen()
        reset_boards()

        # Get player names
        player1 = input('Player 1\'s name: ').title()
        player2 = input('Player 2\'s name: ').title()

        # Setup boards
        p1_ship_board = ShipBoard(
            P1_BOARD,
            p1_ship_coords,
            BOARD_SIZE,
            VERTICAL_SHIP,
            HORIZONTAL_SHIP
        )
        p2_ship_board = ShipBoard(
            P2_BOARD,
            p2_ship_coords,
            BOARD_SIZE,
            VERTICAL_SHIP,
            HORIZONTAL_SHIP
        )
        p1_guess_board = GuessBoard(
            P1_GUESSES_BOARD,
            P2_BOARD,
            p2_ship_board.ship_coords,
            MISS,
            HIT,
            SUNK,
            VERTICAL_SHIP,
            HORIZONTAL_SHIP
        )
        p2_guess_board = GuessBoard(
            P2_GUESSES_BOARD,
            P1_BOARD,
            p1_ship_board.ship_coords,
            MISS,
            HIT,
            SUNK,
            VERTICAL_SHIP,
            HORIZONTAL_SHIP
        )

        # Player 1 places ships
        for ship in SHIP_INFO:
            clear_screen()
            display_boards(player1, P1_BOARD, P1_GUESSES_BOARD)
            p1_ship_board.place_ship(ship)
            clear_screen()
            display_boards(player1, P1_BOARD, P1_GUESSES_BOARD)

        end_turn(player2)

        # Player 2 places ships
        for ship in SHIP_INFO:
            clear_screen()
            display_boards(player2, P2_BOARD, P2_GUESSES_BOARD)
            p2_ship_board.place_ship(ship)
            clear_screen()
            display_boards(player2, P2_BOARD, P2_GUESSES_BOARD)

        end_turn(player1)

        # Game loop starts
        while True:
            clear_screen()

            # Player 1's turn
            display_boards(player1, P1_BOARD, P1_GUESSES_BOARD)
            p1_guess_board.get_guess()
            clear_screen()
            display_boards(player1, P1_BOARD, P1_GUESSES_BOARD)
            sleep(1)

            # Check for game end
            if p1_guess_board.hit_count == p1_guess_board.HITS_TO_WIN:
                clear_screen()
                display_end_screen(player1, P1_BOARD, player2, P2_BOARD)
                replay = input('Do you want to play again? ')
                if self.play_again(replay):
                    self.play()
                else:
                    break

            end_turn(player2)

            # Player 2's turn
            display_boards(player2, P2_BOARD, P2_GUESSES_BOARD)
            p2_guess_board.get_guess()
            clear_screen()
            display_boards(player2, P2_BOARD, P2_GUESSES_BOARD)
            sleep(1)

            # Check for game end
            if p2_guess_board.hit_count == p2_guess_board.HITS_TO_WIN:
                clear_screen()
                display_end_screen(player2, P2_BOARD, player1, P1_BOARD)
                replay = input('Do you want to play again? ')
                self.play_again(replay)
                if self.play_again(replay):
                    self.play()
                else:
                    break

            end_turn(player1)

if __name__ == '__main__':
    Game().play()
