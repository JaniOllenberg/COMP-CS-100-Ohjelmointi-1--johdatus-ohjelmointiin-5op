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
    OVER_100 = False
    while OVER_100 == False:
        print(i, "*", number, "=", i*number)
        if i*number > 100:
            OVER_100 = True
        i += 1
        

if __name__ == "__main__":
    main()