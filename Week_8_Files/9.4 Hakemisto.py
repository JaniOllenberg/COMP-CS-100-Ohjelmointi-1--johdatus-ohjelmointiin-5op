"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

Example for creating an alphabetical index for a book.
Esimerkkiohjelma kirjan aakkosellisen hakemiston muodostaminen.
"""

def main():
    alphabetical_index = {}
    input_filename = input("Input filename: ")

    try:
        file_stream = open(input_filename, mode="r")

        for line in file_stream:
            data_fields = line.split()

            if len(data_fields) != 2:
                raise ValueError("Bad line: page number is missing!")

            keyword = data_fields[0]
            page_number = int(data_fields[1])

            if page_number < 0:
                raise ValueError("Bad page number!")

            if keyword not in alphabetical_index:
                alphabetical_index[keyword] = [page_number]
            else:
                alphabetical_index[keyword].append(page_number)

    except OSError:
        print("Error in reading the file!")
        return

    except ValueError as error_message:
        print(error_message)
        return

    output_filename = input("Output filename: ")

    try:
        file_stream = open(output_filename, mode="w")

        for keyword in sorted(alphabetical_index):
            print(keyword, "", end="", file=file_stream)

            for page_number in sorted(alphabetical_index[keyword]):
                print(page_number, "", end="", file=file_stream)

            print(file=file_stream)

    except OSError:
        print("Error in writing the file!")


if __name__ == "__main__":
    main()
