"""
COMP:CS.100 Programming 1
5.3.1 add number to list and print all positive numbers
Jani Ollenberg
H288244
"""

def main():
    list = []
    print("Give 5 numbers: ")
    for i in range(0, 5):
        number = int(input("Next number: "))
        list.append(number)
    print("The numbers you entered that were greater than zero were:")
    for numbers in list:
        if numbers > 0:
            print(numbers)



if __name__ =="__main__":
    main()