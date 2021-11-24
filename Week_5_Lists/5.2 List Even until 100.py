"""
COMP.CS.100 Programming 1
List all the even number 0-100
Jani Ollenberg
H288244
"""

def main():
    for i in range(0, 101):
        if i % 2 == 0:
            print(i)
    
    for i in range(100, -1, -1):
        if i % 2 == 0:
            print(i)

if __name__ == "__main__":
    main()