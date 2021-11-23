"""
COMP.CS.100 Programming 1
Car program
Jani Ollenberg
H288244
"""

from math import sqrt


def menu():
    """
    This is a text-based menu. You should ONLY TOUCH TODOs inside the menu.
    TODOs in the menu call functions that you have implemented and take care
    of the return values of the function calls.
    """

    tank_size = read_number("How much does the vehicle's gas tank hold? ")
    gas = tank_size  # Tank is full when we start
    gas_consumption = read_number("How many liters of gas does the car " +
                                  "consume per hundred kilometers? ")
    x = 0.0  # Current X coordinate of the car
    y = 0.0  # Current Y coordinate of the car

    while True:
        print("Coordinates x={:.1f}, y={:.1f}, "
              "the tank contains {:.1f} liters of gas.".format(x, y, gas))

        choice = input("1) Fill 2) Drive 3) Quit\n-> ")

        if choice == "1":
            to_fill = read_number("How many liters of gas to fill up? ")
            gas = fill(tank_size, to_fill, gas)

        elif choice == "2":
            new_x = read_number("x: ")
            new_y = read_number("y: ")
            gas, x, y = drive(x, y, new_x, new_y, gas, gas_consumption)

        elif choice == "3":
            break

    print("Thank you and bye!")


def fill(tank_size, gas_filled, current_gas):
    """
    This function has three parameters which are all FLOATs:
      (1) the size of the tank
      (2) the amount of gas that is requested to be filled in
      (3) the amount of gas in the tank currently

    The parameters have to be in this order.
    The function returns one FLOAT that is the amount of gas in the
    tank AFTER the filling up.

    The function does not print anything and does not ask for any
    input.
    """
    filled_tank = current_gas + gas_filled
    if filled_tank > tank_size:
        filled_tank = tank_size

    return filled_tank


def drive(current_x, current_y, destination_x, destination_y, gas, consumption):
    """
    This function has six parameters. They are all floats.
      (1) The current x coordinate
      (2) The current y coordinate
      (3) The destination x coordinate
      (4) The destination y coordinate
      (5) The amount of gas in the tank currently
      (6) The consumption of gas per 100 km of the car

    The parameters have to be in this order.
    The function returns three floats:
      (1) The amount of gas in the tank AFTER the driving
      (2) The reached (new) x coordinate
      (3) The reached (new) y coordinate

    The return values have to be in this order.
    The function does not print anything and does not ask for any
    input.
    """
    wanted_x = destination_x - current_x
    wanted_y = destination_y - current_y
    max_travel = how_far_can_go(gas, consumption)
    wanted_travel = diagonal_distance(current_x, current_y, destination_x, destination_y)
    if wanted_travel > max_travel:
        reached_ratio = max_travel/wanted_travel
        gas_left = 0
    else:
        reached_ratio = 1
        gas_left = gas - wanted_travel /100 * consumption
    reached_x = current_x +(wanted_x*reached_ratio)
    reached_y = current_y + (wanted_y*reached_ratio)

    # It might be usefull to make one or two assisting functions
    # to help the implementation of this function.

    return gas_left, reached_x, reached_y


      # Implement your own functions here. You are required to
      # implement at least two functions that take at least
      # one parameter and return at least one value.  The
      # functions have to be used somewhere in the program.
def diagonal_distance(x, y, xTo, yTo):
    """
    pythagoras theorem
    :param x, y, xTo, yTo: where we been and where we wanna go
    :return: whats the straight line distance there
    """
    return sqrt((xTo-x)**2 +(yTo-y)**2)

def how_far_can_go(gas, consumption):
    """
    how many km can car travel
    :param: gas, consumption
    :return: how many km can we go
    """
    return gas*100/consumption

def read_number(prompt, error_message="Incorrect input!"):
    """
    DO NOT TOUCH THIS FUNCTION.
    This function reads input from the user.
    Also, don't worry if you don't understand it.
    """

    try:
        return float(input(prompt))

    except ValueError:
        print(error_message)
        return read_number(prompt, error_message)


def main():
    menu()


if __name__ == "__main__":
    main()
