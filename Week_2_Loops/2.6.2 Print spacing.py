"""
COMP.CS.100 Ohjelmointi 1
2.6.2 Tulostuksen välilyönnit
Jani Ollenberg
H288244
"""

def main():
    name = input("Tell us your name: ")
    print('Hey ', name, ", the printout formatting is going well!", sep="")

if __name__ == "__main__":
    main()