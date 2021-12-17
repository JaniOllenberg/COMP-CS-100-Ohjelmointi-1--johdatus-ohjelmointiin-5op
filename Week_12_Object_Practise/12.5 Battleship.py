"""
COMP.CS.100 Programming 1
Battleship game. Shoot at coordinates A0 to J9 and try to sink all battleships.
Jani Ollenberg
H288244
"""

class Battleship:
    """
    Class defines a battleship for the game.
    """
    def __init__(self, ship_type, coordinates):
        """
        Initialize a new battleship.
        :param ship_type: str, type of the ship, determines size
        :param coordinates: list of coordinates of the ship
        """
        self.__ship_type = ship_type
        self.__coordinates = coordinates
        self.__has_sunk = False
        self.__hits_taken = []

        # check that coordinates are in correct format A0 to J9
        valid_x_coordinates = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        valid_y_coordinates = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for i in self.__coordinates:
            x = i[0]
            y = i[1:]
            if x not in valid_x_coordinates:
                raise ValueError("Error in ship coordinates!")
            if y not in valid_y_coordinates:
                raise ValueError("Error in ship coordinates!")

    def get_coordinates(self):
        """
        Give all coordinates of the ship.
        :return: list of coordinates
        """
        return self.__coordinates
    
    def been_hit(self, coordinate):
        """
        Checks if ship has been hit in this coordinate.
        :param coordinate: str, XY position of shot
        :return bool: True or false
        """
        if coordinate.upper() in self.__coordinates:
            return True
        else:
            return False
    
    def has_sunk(self):
        """
        Has boat been destroyed already.
        :return bool: True or false
        """
        return self.__has_sunk
    
    def hit(self, coordinate, sunk_ships):
        """
        Register a hit to the ship.
        :param coordinate: str, XY location of shot
        :param sunk_ships: list, all ship objects already sunk
        """
        # see if ship is in that coordinate and add to list of shots taken
        if self.been_hit(coordinate):
            self.__hits_taken.append(coordinate)
        
        # if ship has hits in all its coordinates it will sink
        if len(self.__hits_taken) == len(self.__coordinates):
            self.__has_sunk = True
            print(f"You sank a {self.__ship_type}!")
            sunk_ships.append(self)
        
    def get_type_character(self):
        """
        Return the character of the ship type for printing.
        :return character: str
        """
        if self.__ship_type == "battleship":
            return "B"
        if self.__ship_type == "cruiser":
            return "C"
        if self.__ship_type == "destroyer":
            return "D"
        if self.__ship_type == "submarine":
            return "S"
# Battleship class ends here    

def read_board_from_file(filename):
    """
    Reads the ship locations from file.
    :param filename: name of file to read from
    :return all_ships[]: list of all the ships from file
    """
    try:
        data = open(filename, mode="r")
    except:
        print("File can not be read!")
        return False
    
    # list to store all ships in
    all_ships = []

    for line in data:
        ship_data = []
        line = line.rstrip()
        ship_data = line.split(";")
        ship_coordinates = ship_data[1:]

        try:
            # create new battleship object with type and list of coordinates
            # raises ValueError if ship_coordinates are in wrong format
            new_ship = Battleship(ship_data[0], ship_coordinates)
        except ValueError as error_message:
            print(error_message)
            return False

        all_ships.append(new_ship)

    # check for overlapping ships
    checked_coordinates = []
    for ship in all_ships:
        full_coordinates = ship.get_coordinates()
        for coordinate in full_coordinates:
            if coordinate in checked_coordinates:
                print("There are overlapping ships in the input file!")
                return False
            checked_coordinates.append(coordinate)

    # boat locations read successfully without errors
    # return the list of all Battleship objects
    return all_ships
    
def print_board(all_shots, all_ships):
    """
    Prints the board with coordinates and all the shots fired
    :param all_shots: list of all shots fired so far
    :param all_ships: list of all Battleship objects on board
    """
    print()
    # print top row
    print("  A B C D E F G H I J  ")

    # complicated structure to loop through all coordinates on board
    for y in range(10):
        # start by printing line number on the side
        print(y, end="")

        for x in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']:
            current_coordinate = str(f"{x}{y}") # coordinate to print for

            if current_coordinate in all_shots: # current coordinate has been
                boat_hit = False                # shot, which char to print?

                for ship in all_ships: # check if any ship has been hit
                    if ship.been_hit(current_coordinate):
                        boat_hit = True
                        if not ship.has_sunk(): # print X if boat was hit
                            print(" X", end="")

                        # print ship type letter if boat was sunk
                        else: print(f" {ship.get_type_character()}", end="")

                if boat_hit == False:   # print a star " *"
                    print(" *", end="") # if no boats in current_coordinate

            else: # print empty spaces if current_coordinate hasn't been shot
                print("  ", end="")

            if x == "J": # after J coordinate print line number on the side
                print("", y)

    # print bottom row            
    print("  A B C D E F G H I J  \n")

def is_valid_command(input):
    """
    Checks that command is in format a0 to J9
    :param input: str, command inputted
    :return bool: True or False
    """
    if input == "":
        print("Invalid command!")
        return False
        
    x = input[0].upper()

    try: # raises an error if second coordinate is not a number
        y = int(input[1:])
    except:
        print("Invalid command!")
        return False

    # check that first coordinate is letter A-J and number is 0-9
    if x in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']:
        if y in range(0, 10):
            return True
    
    print("Invalid command!")
    return False

def shoot(coordinate, all_ships, all_shots, sunk_ships):
    """
    Shooting logic of the game.
    :param coordinate: str, coordinate of shot
    :param all_ships: list of all ships
    :param all_shots: list of all shots fired
    :param sunk_ships: list of all sunk ships
    :return bool: True if shooting is successfull
    """

    # first check if location has already been shot at
    if coordinate.upper() in all_shots:
        print("Location has already been shot at!")
        return False
    
    # go through all ships to see if they have been sunk
    # list of sunk_ships needed to check if shot sinks a new ship for printing
    for ship in all_ships:
        if ship not in sunk_ships:
            ship.hit(coordinate, sunk_ships)
    return True


def main():

    # ask for file to read ships from or use "battleship.txt" as dfault
    filename = input("Enter file name: ") or "battleship.txt"

    # read the file and return list of all Battleship objects
    all_ships = read_board_from_file(filename)

    # quit if there was an error reading file or with ship coordinates
    if all_ships == False:
        return

    # list of all shots fired
    all_shots = []

    # list of all sunk ships
    sunk_ships = []

    while True:
        print_board(all_shots, all_ships)

        # win game if all ships are destroyed
        game_won = True
        for ship in all_ships:
            if ship not in sunk_ships:
                game_won = False
        if game_won == True:
            print("Congratulations! You sank all enemy ships.")
            return

        coordinate = input("Enter place to shoot (q to quit): ")

        if coordinate == 'q' or coordinate == 'Q':
            print("Aborting game!")
            return

        if is_valid_command(coordinate):

            # shoot() returns true if it's in a new location
            if shoot(coordinate, all_ships, all_shots, sunk_ships):
                all_shots.append(coordinate.upper())


if __name__ == "__main__":
    main()