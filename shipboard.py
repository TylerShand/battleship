from time import sleep


class ShipBoard:

    def __init__(self, board, ship_coords, BOARD_SIZE, VERTICAL_SHIP, HORIZONTAL_SHIP):
        self.board = board
        self.ship_coords = ship_coords
        self.BOARD_SIZE = BOARD_SIZE
        self.VERTICAL_SHIP = VERTICAL_SHIP
        self.HORIZONTAL_SHIP = HORIZONTAL_SHIP

    # Makes sure the coordinates and direction are in a standard format
    def format_placement(self, placement, ship_size, ship):
        if len(placement) < 4:
            print('ERROR: Incorrect input')
            return self.place_ship(ship)

        placement = placement.split(' ')

        coordinates = placement[0]
        # Catches intances where no placement[1] is recieved
        try:
            up_down_left_right = placement[1]
        except IndexError:
            print('ERROR: Incorrect input')
            return self.place_ship(ship)

        # Formatting for coordinates
        if len(coordinates) == 3 and not coordinates.isalpha():
            coordinates = coordinates[0] + str(int(coordinates[1:]) - 1)
        elif len(coordinates) == 2 and not coordinates.isalpha():
            coordinates = coordinates[0] + str(int(coordinates[1]) - 1)
        else:
            print('ERROR: Incorrect input')
            return self.place_ship(ship)

        # Formatting for directions
        if up_down_left_right[0].lower() == 'u':
            up_down_left_right = 'up'
        elif up_down_left_right[0].lower() == 'd':
            up_down_left_right = 'down'
        elif up_down_left_right[0].lower() == 'l':
            up_down_left_right = 'left'
        elif up_down_left_right[0].lower() == 'r':
            up_down_left_right = 'right'
        else:
            print('ERROR: Incorrect input')
            return self.place_ship(ship)
        placement = coordinates, up_down_left_right
        return self.check_placement(placement, ship_size, ship)

    def place_ship(self, ship):
        ship_name = ship[0]
        ship_size = ship[1]
        print('Where do you want to place your {}?'.format(ship_name))
        print('[COORDINATES] [UP/DOWN/RIGHT/LEFT]')
        print('(Seperate with spaces)')
        print('i.e. a1 down')
        print('----------------------------------------')
        placement = input('> ').lower()
        return self.format_placement(placement, ship_size, ship)

    # Checks if the ship is hitting a border of the board and displays an
    # appropriate error message
    def check_placement(self, placement, ship_size, ship):
        error_message = 'ERROR: Hit {} border'

        direction = placement[1]

        coordinates = placement[0]
        coordinate_letter = placement[0][0]
        coordinate_number = placement[0][1]

        if direction == 'up':
            if int(coordinate_number) - ship_size <= 0:
                print(error_message.format('TOP'))
                sleep(1)
                return self.place_ship(ship)
        if direction == 'down':
            if int(coordinate_number) + ship_size > self.BOARD_SIZE:
                print(error_message.format('BOTTTOM'))
                sleep(1)
                return self.place_ship(ship)
        if direction == 'left':
            if (ord(coordinate_letter) - 97) - ship_size <= 0:
                print(error_message.format(direction.upper()))
                sleep(1)
                return self.place_ship(ship)
        if direction == 'right':
            if (ord(coordinate_letter) - 97) + ship_size > self.BOARD_SIZE:
                print(error_message.format(direction.upper()))
                sleep(1)
                return self.place_ship(ship)
        return self.add_to_board(placement, ship_size, ship)

    # Adds ships to the board
    # Displays and error message if a ship intersects with an existing ship
    def add_to_board(self, placement, ship_size, ship):
        direction = placement[1]
        ship_name = ship[0]

        # Coordinate letter and number
        letter = ord(placement[0][0]) - 97
        number = int(placement[0][1])

        if direction == 'up':
            for i in range(0, ship_size):
                if self.board[number - i][letter] == self.VERTICAL_SHIP:
                    print('ERROR: hit existing ship.')
                    return self.place_ship(ship)
                if self.board[number - i][letter] == self.HORIZONTAL_SHIP:
                    print('ERROR: hit existing ship.')
                    return self.place_ship(ship)
                self.board[number - i][letter] = self.VERTICAL_SHIP
                self.ship_coords[ship_name][1].append(str(letter) + str(number - i))

        if direction == 'down':
            for i in range(0, ship_size):
                if self.board[number + i][letter] == self.VERTICAL_SHIP:
                    print('ERROR: hit existing ship.')
                    return self.place_ship(ship)
                if self.board[number + i][letter] == self.HORIZONTAL_SHIP:
                    print('ERROR: hit existing ship.')
                    return self.place_ship(ship)
                self.board[number + i][letter] = self.VERTICAL_SHIP
                self.ship_coords[ship_name][1].append(str(letter) + str(number + i))

        if direction == 'left':
            for i in range(0, ship_size):
                if self.board[number][letter - i] == self.VERTICAL_SHIP:
                    print('ERROR: hit existing ship.')
                    return self.place_ship(ship)
                if self.board[number][letter - i] == self.HORIZONTAL_SHIP:
                    print('ERROR: hit existing ship.')
                    return self.place_ship(ship)
                self.board[number][letter - i] = self.HORIZONTAL_SHIP
                self.ship_coords[ship_name][1].append(str(letter - i) + str(number))
        if direction == 'right':
            for i in range(0, ship_size):
                if self.board[number][letter + i] == self.VERTICAL_SHIP:
                    print('ERROR: hit existing ship.')
                    return self.place_ship(ship)
                if self.board[number][letter + i] == self.HORIZONTAL_SHIP:
                    print('ERROR: hit existing ship.')
                    return self.place_ship(ship)
                self.board[number][letter + i] = self.HORIZONTAL_SHIP
                self.ship_coords[ship_name][1].append(str(letter + i) + str(number))
        return None
