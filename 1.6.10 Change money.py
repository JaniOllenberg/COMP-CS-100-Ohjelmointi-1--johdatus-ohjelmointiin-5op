"""
COMP.CS.100
1.6.10 Change Money
Jani Ollenberg
H288244
"""

def main():
    price = int(input("Purchase price: "))
    paid_amount = int(input("Paid amount of money: "))

    if price >= paid_amount:
        print("No change")
    else:
        change = paid_amount - price
        tens = change // 10
        change = change - (tens*10)

        fives = change // 5
        change = change-(fives*5)

        twos = change // 2
        change = change - (twos*2)

        ones = change //1

        print("Offer change:")
        if tens > 0:
            print(f'{tens} ten-euro notes')
        if fives > 0:
            print(f'{fives} five-euro notes')
        if twos >0:
            print(f'{twos} two-euro coins')
        if ones > 0:
            print(f'{ones} one-euro coins')

if __name__ == "__main__":
    main()