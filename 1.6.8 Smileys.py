"""
COMP.CS.100
1.6.8 Smileys
Jani Ollenberg
H288244
"""

def main():

    mood = int(input("How do you feel? (1-10) "))
    
    if mood < 1 or mood > 10:
        print("Bad input!")
    else:
        if mood == 10:
            print("A suitable smiley would be :-D")
        elif mood < 10 and mood > 7:
            print("A suitable smiley would be :-)")
        elif mood == 1:
            print("A suitable smiley would be :'(")
        elif mood < 4 and mood > 1:
            print("A suitable smiley would be :-(")
        else:
            print("A suitable smiley would be :-|")




if __name__ == "__main__":
    main()