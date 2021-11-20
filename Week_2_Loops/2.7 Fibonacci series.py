"""
COMP.CS.100 Ohjelmointi 1
2.7 Fibonacci series
Jani Ollenberg
H288244
"""

def main():
    howMany = int(input("How many Fibonacci numbers do you want? "))
    previous = 0
    current = 1
    next = 1
    for i in range(1, howMany+1):
        current = next
        print(f'{i}. {current}')
        next = current + previous
        previous = current
    # 1. 1
    # 2. 1
    # 3. 2
    # 4. 3
    # 5. 5
    # 6. 8
    # 7. 13

if __name__ == "__main__":
    main()