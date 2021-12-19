"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: H288244
Name:       Jani Ollenberg
Email:      jani.ollenberg@tuni.fi

Click counter program with reset, increase, decrese and quit buttons.
"""

from tkinter import *


class Counter:
    def __init__(self):
        # TODO: You have to creater one label and four buttons and store
        #       them in the following attributes:
        #
        #       self.__current_value_label  # Label displaying the current value of the counter.
        #       self.__reset_button         # Button which resets counter to zero.
        #       self.__increase_button      # Button which increases the value of the counter by one.
        #       self.__decrease_button      # Button which decreases the value of the counter by one.
        #       self.__quit_button          # Button which quits the program.
        #
        #       Make sure you name the components exactly as shown above,
        #       otherwise the automated tests will fail.
        self.__mainWindow = Tk()
        self.__mainWindow.option_add("*Font", "Verdana 36")
        self.__counter = 0
        self.__current_value_label = Label(self.__mainWindow,
                                             text=self.__counter)
        self.__current_value_label.pack()
        self.__reset_button = Button(self.__mainWindow, text="Reset",
                                         command=self.reset)
        self.__reset_button.pack(side=LEFT)
        self.__increase_button = Button(self.__mainWindow, text="Increase",
                                        command=self.increase)
        self.__increase_button.pack(side=LEFT)
        self.__decrease_button = Button(self.__mainWindow, text="Decrease",
                                        command=self.decrease)
        self.__decrease_button.pack(side=LEFT)
        self.__quit_button = Button(self.__mainWindow, text="Quit",
                                         command=self.quit)
        self.__quit_button.pack(side=LEFT)
        self.__mainWindow.mainloop()

    # TODO: Implement the rest of the needed methods here.
    def reset(self):
        """
        Resets the counter.
        """
        self.__counter = 0
        self.__current_value_label.configure(text=self.__counter, foreground="black")
    
    def quit(self):
        self.__mainWindow.destroy()
    
    def increase(self):
        self.__counter += 1
        print("increase button pressed")
        print(self.__counter)
        self.__current_value_label.configure(text=self.__counter, foreground="green")
    def decrease(self):
        self.__counter -= 1
        self.__current_value_label.configure(text=self.__counter, foreground="red")
    
def main():
    # There is no need to modify the main function.
    # As a matter of fact, automated tests ignore main
    # once again.

    Counter()


if __name__ == "__main__":
    main()
