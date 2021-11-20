"""
COMP.CS.100
2.4.1 Number series game Zip Boing
Jani Ollenberg
H288244
"""

def main():
    # print numbers or zip if divisible by 2 and boing if divisible by 7
    # print zip boing if disisible by 2 and 7

    numbers = int(input("How many numbers would you like to have? "))
    
    for index in range(1, numbers+1):
        if index % 3 == 0 and index % 7 == 0:
            print("zip boing")
            continue
        if index % 3 == 0:
            print("zip")
            continue
        if index % 7 == 0:
            print("boing")
            continue
        print(index)


if __name__ == "__main__":
    main()