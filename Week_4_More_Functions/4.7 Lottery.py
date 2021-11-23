"""
Comp.cs.100
Lottery odds calculator
Jani Ollenberg
H288244
"""
def factorial(number):
    """
    Calculate factorial of a number
    """
    factorial = 1
    for i in range(1, number+1):
        factorial = i * factorial
    return factorial

def lottery_odds(total, drawn):
    """
    calculate lottery odds
    """
    odds = factorial(total)/(factorial(total-drawn)*factorial(drawn))
    return int(odds)

def main():

    
    while True:
        
        total_balls = int(input("Enter the total number of lottery balls: "))
        drawn_balls = int(input("Enter the number of the drawn balls: "))
        if drawn_balls <= 0 or total_balls <= 0:
            print("The number of balls must be a positive number.")
            break
        if drawn_balls > total_balls:
            print("At most the total number of balls can be drawn.")
            break

        lottery_max = lottery_odds(total_balls, drawn_balls)
        print(f"The probability of guessing all {drawn_balls} balls correctly is 1/{lottery_max}")
        break


        

if __name__ == "__main__":
    main()