"""
COMP.CS.100 Programming 1
Dictionary in dictionary.
Jani Ollenberg
H288244
"""
def read_file(filename):
    """
    Read file and create a dictionary in a dictionary out of it
    :param filename: str, name of .csv file
    :return: data structure
    """
    data_file = open(filename, mode="r")
    data = {}
    Lines = data_file.readlines()
    line1 = Lines[0].rstrip().split(";")
    # print(Lines)
    # print(line1)
    # # create data dictionary from first line
    # for keys in line1:
    #     data[keys] = []
    for line in Lines:
        line = line.rstrip()
        parts = line.split(";")
        # print(parts)
        # create dictionaries in dictionary with keys
        data[parts[0]] = {}
        facts = {}
        # print(parts[0])
        for values in range(1, len(line1)):
            facts[line1[values]] = parts[values]
            # print(parts[values])
            # print(facts)
        data[parts[0]] = facts
    # print(data)
    return data    

def main():
    info = read_file("contacts.csv")
    print(info["Archie"]["name"])
    print(info["Mike"]["phone"])
    print(info["Tom"]["email"])
if __name__ == "__main__":
    main()