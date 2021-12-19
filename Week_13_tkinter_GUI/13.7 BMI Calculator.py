"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

Body Mass Index calculator. Insert weight in kg and height in cm.
Calculates the BMI with the formula weight(kg)/(height(m)^2)
Jani Ollenberg
H288255
"""

from tkinter import *
from tkinter import font


class Userinterface:

    def __init__(self):
        self.__mainwindow = Tk()
        self.__mainwindow.option_add("*Font", "Verdana 36")

        # TODO: Create an Entry-component for the weight.
        self.__weight_value = Entry(self.__mainwindow)
        self.__weight_label = Label(self.__mainwindow, text="Weight(kg)")

        # TODO: Create an Entry-component for the height.
        self.__height_value = Entry(self.__mainwindow)
        self.___height_label = Label(self.__mainwindow, text="Height(cm)")

        # TODO: Create a Button that will call the calculate_BMI-method.
        # TODO: Change the colour of the Button to something else than
        #       the default colour.
        self.__calculate_button = Button(self.__mainwindow,
                                         text="Calculate BMI", 
                                         background="#000fff000",
                                         command=self.calculate_BMI)

        # TODO: Create a Label that will show the decimal value of the BMI
        #      after it has been calculated.
        self.__result_text = Label(self.__mainwindow, text="BMI result")

        # TODO: Create a Label that will show a verbal description of the BMI
        #       after the BMI has been calculated.
        self.__explanation_text = Label(self.__mainwindow,
                                        text= "           weight(kg) \n"
                                              "BMI = ----------------\n"
                                              "           height(m)^2\n")

        # TODO: Create a button that will call the stop-method.
        self.__stop_button = Button(self.__mainwindow,
                                    text="Stop",
                                    command=self.stop)

        # TODO: Place the components in the GUI as you wish.
        # If you read the Gaddis book, you can use pack here instead of grid!
        self.__weight_label.grid()
        self.__weight_value.grid()
        self.___height_label.grid()
        self.__height_value.grid()
        self.__calculate_button.grid()
        self.__stop_button.grid()
        self.__result_text.grid()
        self.__explanation_text.grid()

    # TODO: Implement this method.
    def calculate_BMI(self):
        """
        Part b) This method calculates the BMI of the user and
        displays it. First the method will get the values of
        height and weight from the GUI components
        self.__height_value and self.__weight_value.  Then the
        method will calculate the value of the BMI and show it in
        the element self.__result_text.

        Part e) Last, the method will display a verbal
        description of the BMI in the element
        self.__explanation_text.
        """
        try:
            weight = int(self.__weight_value.get())
            height = int(self.__height_value.get())
        except:
            error = "Error: height and weight must be numbers."
            self.__explanation_text.configure(text=error)
            self.reset_fields()
            return
            
        if height < 0 or weight < 0:
            self.reset_fields()
            self.__explanation_text.configure(text="Error: height and weight"
                                                   " must be positive.")
        else:
            bmi = weight/((height/100) ** 2)
            if 18.5 < bmi < 25: 
                analysis = "Your weight is normal."
            elif bmi > 25:
                analysis = "You are overweight."
            elif bmi < 18.5:
                analysis = "You are underweight."
            bmi = str(f"{bmi:.2f}")

            self.__result_text.configure(text=bmi)
            self.__explanation_text.configure(text=analysis)

    # TODO: Implement this method.
    def reset_fields(self):
        """
        In error situations this method will zeroize the elements
        self.__result_text, self.__height_value, and self.__weight_value.
        """

        self.__result_text.configure(text="")
        self.__height_value.delete(0, END)
        self.__weight_value.delete(0, END)

    def stop(self):
        """
        Ends the execution of the program.
        """

        self.__mainwindow.destroy()

    def start(self):
        """
        Starts the mainloop.
        """
        self.__mainwindow.mainloop()


def main():
    # Notice how the user interface can be created and
    # started separately.  Don't change this arrangement,
    # or automatic tests will fail.
    ui = Userinterface()
    ui.start()


if __name__ == "__main__":
    main()
