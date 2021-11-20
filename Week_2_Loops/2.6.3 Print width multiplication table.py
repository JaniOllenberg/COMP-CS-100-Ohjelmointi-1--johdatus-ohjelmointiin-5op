"""
COMP.CS.100 Ohjelmointi 1
2.6.3 10x10 multiplication table
Jani Ollenberg
H288244
"""

def main():
    for i in range(1, 11):
        for j in range(1, 11):
            print(f'{i*j:4}', end="")
        print()

if __name__ == "__main__":
    main()
