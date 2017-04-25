from time import sleep


class GuessBoard:

    # Holds the number of hits required to win
    HITS_TO_WIN = 5  # Change to 17
    # Holds the current number of hits
    hit_count = 0

    def __init__(self, guess_board, opponent_board, ship_coords, MISS, HIT,
                 SUNK, VERTICAL_SHIP, HORIZONTAL_SHIP):
        self.guess_board = guess_board
        self.opponent_board = opponent_board
        self.ship_coords = ship_coords
        self.MISS = MISS
        self.HIT = HIT
        self.SUNK = SUNK
        self.VERTICAL_SHIP = VERTICAL_SHIP
        self.HORIZONTAL_SHIP = HORIZONTAL_SHIP

    # Get guess from a player, format it and pass it to the check_guess
    # method
    def get_guess(self):
        print('Guess the position of the enemy ship:')
        print('[COORDINATES]')
        print('i.e. b3')
        print('----------------------------------------')
        guess = input('> ').lower()
        return self.format_guess(guess)

    # Makes sure the guess in a standard format
    def format_guess(self, guess):
        if len(guess) == 3:
            guess = guess[0] + str(int(guess[1:]) - 1)
        elif len(guess) == 2:
            guess = guess[0] + str(int(guess[1]) - 1)
        else:
            print('ERROR: Incorrect input')
            return self.get_guess()
        return self.check_guess(guess)

    # Checks if the guess is a hit or miss and displays it accordingly
    def check_guess(self, guess):
        coordinate_letter = ord(guess[0]) - 97
        coordinate_number = int(guess[1])
        guess_pos = self.opponent_board[coordinate_number][coordinate_letter]

        count = 0

        if (guess_pos == self.VERTICAL_SHIP or
                guess_pos == self.HORIZONTAL_SHIP):
            self.guess_board[coordinate_number][coordinate_letter] = self.HIT
            self.opponent_board[coordinate_number][coordinate_letter] = \
                self.HIT
            self.hit_count += 1
            for ship in self.ship_coords.keys():
                if ((str(coordinate_letter) + str(coordinate_number))
                        in self.ship_coords[ship][1]):
                    self.ship_coords[ship][0] = self.ship_coords[ship][0] + 1
                    print('HIT')
                    sleep(1)
                    MAX_COUNT = len(self.ship_coords[ship][1])
                    if self.ship_coords[ship][0] == MAX_COUNT:
                        print('You sunk the enemy {}!'.format(ship))
                        for i in self.ship_coords[ship][1]:
                            letter = int(i[0])
                            number = int(i[1])
                            self.guess_board[number][letter] = self.SUNK
                            self.opponent_board[number][letter] = self.SUNK
                        sleep(2)
        else:
            self.guess_board[coordinate_number][coordinate_letter] = self.MISS
            print('MISS!')
            sleep(1)
