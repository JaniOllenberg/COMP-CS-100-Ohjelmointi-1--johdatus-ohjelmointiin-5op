"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Fractions calculator.
Jani Ollenberg
H288244
"""

class Fraction:
    """
    This class represents one single fraction that consists of
    numerator (osoittaja) and denominator (nimittäjä).
    """

    def __init__(self, numerator, denominator):
        """
        Constructor. Checks that the numerator and denominator are of
        correct type and initializes them.

        :param numerator: int, fraction's numerator
        :param denominator: int, fraction's denominator
        """

        # isinstance is a standard function which can be used to check if
        # a value is an object of a certain class.  Remember, in Python
        # all the data types are implemented as classes.
        # ``isinstance(a, b´´) means more or less the same as ``type(a) is b´´
        # So, the following test checks that both parameters are ints as
        # they should be in a valid fraction.
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError

        # Denominator can't be zero, not in mathematics, and not here either.
        elif denominator == 0:
            raise ValueError

        self.__numerator = numerator
        self.__denominator = denominator

    def __lt__(self, frac2):
        expanded_self = self.expand(frac2)
        expanded_frac2 = frac2.expand(self)
        if expanded_self.get_numerator() < expanded_frac2.get_numerator():
            return True
        else:
            return False

    def __gt__(self, frac2):
        expanded_self = self.expand(frac2)
        expanded_frac2 = frac2.expand(self)
        if expanded_self.get_numerator() > expanded_frac2.get_numerator():
            return True
        else:
            return False
    
    def __str__(self):
        return self.return_string()
    
    def complement(self):
        """
        Vastaluku.
        :return complement: Fraction object
        """
        # if fraction is positive, turn to negative
        if self.__numerator * self.__denominator > 0:
            complement = Fraction(-self.__numerator, self.__denominator)
        else:
            # turn fraction positive
            complement = Fraction(abs(self.__numerator), abs(self.__denominator))
        return complement

    def reciprocal(self):
        """
        Käänteisluku.
        :return: Fraction object"""
        return Fraction(self.__denominator, self.__numerator)

    def return_string(self):
        """
        :returns: str, a string-presentation of the fraction in the format
                       numerator/denominator.
        """

        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""

        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"

    def simplify(self):
        divisor = greatest_common_divisor(self.__numerator, self.__denominator)
        self.__numerator = self.__numerator // divisor
        self.__denominator = self.__denominator // divisor

    def get_numerator(self):
        return self.__numerator
    def get_denominator(self):
        return self.__denominator

    def multiply(self, frac2):
        numerator = self.__numerator * frac2.get_numerator()
        denominator = self.__denominator * frac2.get_denominator()
        return Fraction(numerator, denominator)

    def divide(self, quotient):
        return self.multiply(quotient.reciprocal())

    def add(self, frac2):
        frac1_numerator = self.__numerator * frac2.get_denominator()
        frac1_denominator = self.__denominator * frac2.get_denominator()

        frac2_numerator = frac2.get_numerator() * self.__denominator
        frac2_denominator = frac2.get_denominator() * self.__denominator

        addition = Fraction ((frac1_numerator + frac2_numerator), frac1_denominator)
        return addition
    
    def expand(self, frac2):
        frac1_numerator = self.__numerator * frac2.get_denominator()
        frac1_denominator = self.__denominator * frac2.get_denominator()
        return Fraction(frac1_numerator, frac1_denominator)

    def deduct(self, frac2):
        expanded_frac1 = self.expand(frac2)
        expanded_frac2 = frac2.expand(self)
        deducted_numerator = expanded_frac1.get_numerator() \
                            - expanded_frac2.get_numerator()
        return Fraction(deducted_numerator, expanded_frac1.get_denominator())

def greatest_common_divisor(a, b):
    """
    Euclidean algorithm. Returns the greatest common
    divisor (suurin yhteinen tekijä).  When both the numerator
    and the denominator is divided by their greatest common divisor,
    the result will be the most reduced version of the fraction in question.
    """

    while b != 0:
        a, b = b, a % b

    return a

def main():
    fractions_dict = {}
    while True:
        command = input("> ")

        if command == "add":
            line = input("Enter a fraction in the form integer/integer: ")
            a, b = line.split("/")
            frac = Fraction(int(a), int(b))
            frac_name = input("Enter a name: ")
            fractions_dict[frac_name] = frac
        elif command == "print":
            name = input("Enter a name: ")
            found = False
            for i in fractions_dict:
                if i == name:
                    print(f"{name} = {fractions_dict[i]}")
                    found = True
                    break
            if found == False:
                print(f"Name {name} was not found")
        elif command == "*":
            a = input("1st operand: ")
            if a not in fractions_dict:
                print(f"Name {a} was not found")
                continue
            b = input("2nd operand: ")
            if b not in fractions_dict:
                print(f"Name {b} was not found")
                continue
            multiplied = fractions_dict[a].multiply(fractions_dict[b])
            print(f"{fractions_dict[a]} * {fractions_dict[b]} = {multiplied}")
            multiplied.simplify()
            print("simplified", multiplied)

        elif command == "file":
            filename = input("Enter the name of the file: ")
            try:
                file = open(filename, mode="r")
                for line in file:
                    name, fraction = line.split("=")
                    fracA, fracB = fraction.split("/")
                    frac = Fraction(int(fracA), int(fracB))
                    fractions_dict[name] = frac
            except:
                print("Error: the file cannot be read.")
        
        elif command == "list":
            for i in sorted(fractions_dict):
                print(f"{i} = {fractions_dict[i]}")
        elif command == "quit":
            print("Bye bye!")
            return
        else:
            print("Unknown command!")

if __name__ == "__main__":
    main()