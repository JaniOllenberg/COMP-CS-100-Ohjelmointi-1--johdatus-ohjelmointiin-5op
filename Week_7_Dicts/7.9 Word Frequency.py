"""
COMP.CS.100 Programming 1
Calculate frequency of occurence of each word in given text.
Jani Ollenberg
H288244
"""
def main():
    dictionary = {}
    print("Enter rows of text for word counting. Empty row to quit.")
    while True:
        row = input()
        if row == "":
            break
        else:
            row_list = row.split()
            # print(row_list)  
            for word in row_list:
                word = word.lower()
                if word not in dictionary:
                    dictionary[word] = 1
                else:
                    dictionary[word] += 1
            # print(dictionary)
    for word in sorted(dictionary):
        print(f"{word} : {dictionary[word]} times")

if __name__ == "__main__":
    main()