"""
COMP.CS.100 Programming 1
3.3 Student credit calculator
Jani Ollenberg
H288244
"""

def main ():
    months = int(input("Enter the number of months: "))
    credits_sum = 0
    zero_credits_in_a_row = 0
    for i in range(1, months + 1):
        credits = int(input(f"Enter the number of credits in month {i} "))
        credits_sum += credits
        if credits == 0:
            zero_credits_in_a_row += 1
        else:
            zero_credits_in_a_row = 0
        if zero_credits_in_a_row == 2:
            print("You did have too many study breaks!")
            break
    if zero_credits_in_a_row != 2:
        average_credits = credits_sum / months
        if average_credits >= 5.5:
            print(f"You are a full time student and your monthly credit point average is {average_credits}")
        else:
            print(f'Your monthly credit point average {average_credits} does not classify you as a full time student.')

if __name__ == "__main__":
    main()