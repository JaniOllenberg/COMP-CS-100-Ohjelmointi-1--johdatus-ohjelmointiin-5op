"""
COMP.CS.100
2.8.3 Days of the year
Jani Ollenberg
H288244
"""

def main():
    for month in range(1, 13):
        for day in range(1, 32):
            if month == 1 and day > 31:
                break
            if month == 2 and day > 28:
                break
            if month == 3 and day > 31:
                break
            if month == 4 and day > 30:
                break
            if month == 5 and day > 31:
                break
            if month == 6 and day > 30:
                break
            if month == 7 and day > 31:
                break
            if month == 8 and day > 31:
                break
            if month == 9 and day > 30:
                break
            if month == 10 and day > 31:
                break
            if month == 11 and day > 30:
                break
            if month == 12 and day > 31:
                break
            print(f'{day}.{month}.')

if __name__ == "__main__":
    main()