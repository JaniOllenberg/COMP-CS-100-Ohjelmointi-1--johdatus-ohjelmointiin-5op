"""
COMP.CS.100 Programming 1
Jani Ollenberg
H288244
"""
def main():
    width = 0
    height = 0
    while True:
        try:
            width = int(input("Enter the width of a frame: "))
            break
        except:
            continue
    while True:
        try:
            height = int(input("Enter the height of a frame: "))
            break
        except:
            continue
    mark = input("Enter a print mark: ")
    print()
    for i in range(height):
        print(mark*width)
if __name__ == "__main__":
    main()