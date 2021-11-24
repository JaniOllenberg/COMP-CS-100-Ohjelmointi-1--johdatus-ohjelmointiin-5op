"""
COMP:CS.100 Programming 1
5.3.2 add 5 numbers to a list and go through them in reverse order
Jani Ollenberg
H288244
"""

def main():
    list = []
    print("Give 5 numbers: ")
    for i in range(0, 5):
        number = int(input("Next number: "))
        list.append(number)
    print("The numbers you entered, in reverse order:")
    index = -1
    while index >= -len(list):
        print(list[index])
        index -=1



if __name__ =="__main__":
    main()