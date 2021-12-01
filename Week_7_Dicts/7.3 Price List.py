"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: H288244
Name: Jani Ollenberg
Email:  jani.ollenberg@tuni.fi

Template for pricelist assignment.
"""

PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.7, "grasshopper": 13.25,
    "sushi": 19.9, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}


def main():
    while True:
        query = input("Enter product name: ")
        query = query.strip()
        if query == "":
            print("Bye!")
            break
        else:
            if query in PRICES:
                price = PRICES[query] 
            else:
                print(f"Error: {query} is unknown.")
                continue
            print(f"The price of {query} is: {price}")
if __name__ == "__main__":
    main()
