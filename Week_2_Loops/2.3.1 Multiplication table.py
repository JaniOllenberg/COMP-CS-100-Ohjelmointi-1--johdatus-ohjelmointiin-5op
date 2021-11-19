"""
COMP:CS.100
2.3.1. Multiplication table
Jani Ollenberg
H288244
"""

def main():
    number = input("Choose a number: ")
    number = int(number)
    i = 1
    while i <= 10:
        print(i, "*", number, "=", i*number)
        i += 1
        

if __name__ == "__main__":
    main()