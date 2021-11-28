"""
COMP.CS.100 Programming 1
6.6 Reverse names to correct order.
Jani Ollenberg
H288244
"""
def reverse_name(name_original):
    """
    Tidy name and reverse first name after last name.
    :param name_original: string name
    :return: reversed name
    """
    split = name_original.split(',')
    index = 0
    for i in split:
        split[index] = i.strip()
        index += 1
    reversed = []
    reverse_index = -1
    for i in split:
        reversed.append(split[reverse_index])
        reverse_index -= 1 
    finished = " ".join(reversed)
    finished = finished.strip()
    return finished
def main():
    print(reverse_name("Techie, Teddy"))
    print(reverse_name("Scumble,    Arnold"))
    print(reverse_name("Fortunato,Frank"))
    print(reverse_name("von Grünbaumberger, Herbert"))
    print(reverse_name("   Duck,     Donald  "))
    print(reverse_name("X,"))
    print(reverse_name(",X"))
    print(reverse_name(" , Y "))
    print(reverse_name("Stuart Student"))
    print(reverse_name("Mando"))
if __name__ == "__main__":
    main()