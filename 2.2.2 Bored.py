"""
COMP.CS.100
2.2.2 Are you bored?
Jani Ollenberg
H288244
"""

def main():
    while True:
        answer = input("Answer Y or N: ")
        if answer == 'y' or answer == 'Y' or answer == 'n' or answer == 'N':
            print(f'You answered {answer}')
            break
        else:
            print("Incorrect entry.")

    

if __name__ == "__main__":
    main()