"""
COMP.CS.100
2.8.1 Are you bored?
Jani Ollenberg
H288244
"""

def main():
    while True:
        answer = input("Bored? (y/n) ")
        if answer == 'y' or answer == 'Y':
            print("Well, let's stop this, then.")
            break
        if answer !='N' and answer !='n':
            print("Incorrect entry.")

    

if __name__ == "__main__":
    main()