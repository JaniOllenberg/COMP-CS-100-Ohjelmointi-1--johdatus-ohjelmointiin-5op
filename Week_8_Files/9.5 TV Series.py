"""
COMP.CS.100 Programming 1
Read genres and tv-series from a file into a dict.
Print a list of the genres in alphabetical order
and list tv-series by given genre on user's command.
Jani Ollenberg
H288244
"""

def read_file(filename):
    """
    Reads and saves the series and their genres from the file.
    :param filename: str name of file to read
    :return:
    TODO: comment the parameter and the return value.
    """

    genres_movies = {}
    try:
        file = open(filename, mode="r")

        for row in file:

            # If the input row was correct, it contained two parts:
            # · the show name before semicolon (;) and
            # · comma separated list of genres after the semicolon.
            # If we know that a function (method split in this case)
            # returns a list containing two elements, we can assign
            # names for those elements as follows:
            name, genres = row.rstrip().split(";")

            genres = genres.split(",")
            for genre in genres:
                if genre not in genres_movies:
                    genres_movies[genre] = []
                genres_movies[genre].append(name)
        file.close()
        return  genres_movies

    except ValueError:
        print("Error: rows were not in the format name;genres.")
        return None

    except IOError:
        print("Error: the file could not be read.")
        return None


def main():
    filename = input("Enter the name of the file: ")
    genre_data = read_file(filename)
    print("Available genres are: ", end="")
    list_genres = ", ".join(sorted(genre_data))
    print(list_genres)
    while True:
        genre = input("> ")

        if genre == "exit":
            return
        try:
            for movie in sorted(genre_data[genre]):
                print(movie)
        except:
            pass
if __name__ == "__main__":
    main()
