"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: H288244
Name:   Jani Ollenberg
Email:  jani.ollenberg@tuni.fi

Template for sorting by price assignment.
"""

PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.70, "grasshopper": 13.25,
    "sushi": 19.90, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}

def price(key):
    """
    Used for sorting dict for price
    Not sure how it works tbh :D
    """
    return PRICES[key]
    
def main():
    
    # print(sorted(PRICES, key=price))
    for product in sorted(PRICES, key=price):
        print(f'{product} {PRICES[product]:.2f}')


if __name__ == "__main__":
    main()
