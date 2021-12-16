"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Fractions code template
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
    number = Fraction(54, 19)
    number.simplify()
    print(number.return_string())
    frac = Fraction(-2, 4)
    frac.return_string()
    complement = frac.complement()
    print(complement.return_string())
    reciprocal = frac.reciprocal()
    print(reciprocal.return_string())
    print("multiply")
    frac1 = Fraction(2, 3)
    frac2 = Fraction(3, 4)
    product = frac1.multiply(frac2)
    print(product.return_string())
    #'6/12'
    product.simplify()
    print(product.return_string())
    #'1/2'

    print("quotient")
    frac1 = Fraction(4, 8)
    frac2 = Fraction(2, 1)
    quotient = frac1.divide(frac2)
    print(quotient.return_string())
    print('should be 4/16')
    quotient.simplify()
    print(quotient.return_string())
    print('shoulde be 1/4')
    print("\nSum")
    frac1 = Fraction(2, 3)
    frac2 = Fraction(1, 6)
    sum = frac1.add(frac2)
    print(sum.return_string())
    print('= 15/18')
    sum.simplify()
    print(sum.return_string())
    print('= 5/6')
    print("\nDeduction")
    frac1 = Fraction(2, 3)
    frac2 = Fraction(1, 6)
    difference = frac1.deduct(frac2)
    print(difference.return_string())
    print('should be 9/18')
    difference.simplify()
    print(difference.return_string())
    print("= 1/2")

    frac1 = Fraction(4, 9)
    frac2 = Fraction(5, 9)
    print(f"{frac1.return_string()} Lesser than {frac2.return_string()}")
    print(frac1 < frac2)
    print(frac2 < frac1)
    frac2 = Fraction(5, 12)
    print(f"\n{frac1.return_string()} Greater than {frac2.return_string()}")
    print(frac1 > frac2)
    print(frac2 > frac1)
    print(frac1, frac2)

if __name__ == "__main__":
    main()