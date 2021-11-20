"""
This program reads numbers from the user until the user inputs the
word "quit" or she has entered 20 numbers.  Then the program prints on
screen the average of the entered numbers.
"""

def main():
      # The maximum amount of numbers the user can input.
      MAX_NUMBER_OF_INPUTS = 20

      # The command user can type from the keyboard to finish entering
      # numbers prematurely before all 20 numbers have been entered.
      QUIT_COMMAND = "quit"

      # Stores the sum of all numbers entered.
      sum = 0.0

      # Counts how many numbers have been entered so far.
      counter = 0

      while counter < MAX_NUMBER_OF_INPUTS:
            user_input = input(f"Enter the next number ({QUIT_COMMAND} to finish): ")

            if user_input == QUIT_COMMAND:
                  # If the user enters QUIT_COMMAND (i.e. quit) the break
                  # command is used to quit the loop immediatelly.
                  # The next command which is executed is the one
                  # following the loop construct.
                  # In this case it is the statement begining
                  # with "if counter == 0:".
                  break

            sum += float(user_input)
            counter += 1

      if counter == 0:
            print("Error: no numbers entered, can't calculate average!")
      else:
            print(f"The average of the entered numbers:", sum / counter)


if __name__ == "__main__":
    main()