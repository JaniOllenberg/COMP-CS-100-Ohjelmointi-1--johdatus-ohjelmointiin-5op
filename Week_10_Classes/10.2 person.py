"""
The first example of a home made class.
"""

class Person:
    """
    This class models a person with a simple electronic wallet.
    """

    def __init__(self, name, initial_money):
        """
        A person object is initialized with the name and
        the initial amount of money in the wallet.

        :param name: str, the name of the person whose
            spending the object is following.
        :param initial_money: float, how much money will
            there be in the wallet at the point of creation.
        """

        self.__name = name
        self.__money = initial_money

    def printout(self):
        """
        When a person's data is needed to be printed on
        screen this method will handle it.  Also good
        for debugging and testing purposes.
        """

        print("—" * 25)
        print("Name:  ", self.__name)
        print("Wealth:", self.__money)

    def add_money(self, amount):
        """
        It is possible to add money in the electronic wallet.

        :param amount: float, the amount of money added.

        :return: True if operation successfull, False otherwise.
        """

        if amount < 0.0:
            return False
        else:
            self.__money += amount
            return True

    def make_payment(self, price):
        """
        When making a payment, money needs to be
        deducted from the person's wallet.

        :param price: float, the price of the purchase
            i.e. how much money to deduct from the wallet.
        """

        if price < 0.0:
            print("The price can't be negative.")
        elif price > self.__money:
            print("You can't afford that.")
        else:
            self.__money -= price


def main():
    # Let's create an object of type Person, name it denzil,
    # and  use to spy on Prof. Dexter's spending.
    denzil = Person("Denzil Dexter", 100.00)

    # How is Denzil's wealth in the beginning?
    denzil.printout()

    # One happy day Denzil gets his paycheck. Not much.
    if not denzil.add_money(120.37):
        print("Adding money to the wallet failed.")

    # How are things after the payday?
    denzil.printout()

    # Denzil buys a lunch worth 2.90€ in the dining hall.
    denzil.make_payment(2.90)

    # How's wealth after 2.90€ lunch?
    denzil.printout()


if __name__ == "__main__":
    main()
