"""
COMP.CS.100 Programming 1
Make a list and count how many of a number is present.
Jani Ollenberg
H288244
"""
def input_to_list(numbers):
    """
    ask numbers and return them in a list
    """
    list = []
    print(f'Enter {numbers} numbers:')
    for i in range(numbers):
        number = int(input())
        list.append(number)
    return list

def main():
    numbers = int(input("How many numbers do you want to process: "))
    list_inputs = input_to_list(numbers)
    search = int(input("Enter the number to be searched: "))
    matches = list_inputs.count(search)
    if matches > 0:
        print(f'{search} shows up {matches} times among the numbers you have entered.')
    else:
        print(f'{search} is not among the numbers you have entered.')
if __name__ == "__main__":
    main()