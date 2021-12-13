"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Template for the product assignment.
Jani Ollenberg
H288244
"""

class Product:
    """
    This class defines a simplified product for sale in a store.
    """

    # TODO: Define all the methods here.  You can see what they are,
    #       what parameters they take, and what their return value is
    #       by examining the main-function carefully.
    #
    #       You also need to consider which attributes the class needs.
    #
    #       You are allowed to modify the main function, but your
    #       methods have to stay compatible with the original
    #       since the automatic tests assume that.
    def __init__(self, name, price, sale_percentage = 0.0):
        """
        :param name: str, product name
        :param price: float, product price
        :param sale_percentage: float, sale percentage, default = 0.0
        """
        self.__name = name
        self.__price = price
        self.__sale_percentage = sale_percentage

    def get_price(self):
        """
        Get price of product
        :return price: float, product price
        """
        if self.__sale_percentage == 0:
            return self.__price
        else:
            return self.__price * (1 - self.__sale_percentage / 100)

    def set_sale_percentage(self, sale_percentage):
        """
        Set sale percentage for product.
        :param sale_percentage: float, sale for the product
        """      
        self.__sale_percentage = sale_percentage
    
    def printout(self):
        """
        Print product information.
        """
        print(self.__name)
        print(f"  price: {self.__price:.2f}")
        print(f"  sale%: {self.__sale_percentage:.2f}")
        # if self.__sale_percentage == 0:
        #     print(f"Normal price: {self.__price:.2f}")
        # else:
        #     print(f"Sale price: {self.get_price()}")

def main():
    ################################################################
    #                                                              #
    #  You can use the main-function to test your Product class.   #
    #  The automatic tests will not use the main you submitted.    #
    #                                                              #
    #  Voit käyttää main-funktiota Product-luokkasi testaamiseen.  #
    #  Automaattiset testit eivät käytä palauttamaasi mainia.      #
    #                                                              #
    ################################################################

    test_products = {
        "milk":   1.00,
        "sushi": 12.95,
    }

    for product_name in test_products:
        print("=" * 20)
        print(f"TESTING: {product_name}")
        print("=" * 20)

        prod = Product(product_name, test_products[product_name])

        prod.printout()
        print(f"Normal price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(10.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(25.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)


if __name__ == "__main__":
    main()
