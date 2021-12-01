"""
COMP.CS.100 Programming 1
6.14 Make text lines even number of characters long.
Jani Ollenberg
H288244
"""
def input_text():
    """
    Get the text from user.
    """
    print("Enter text rows. Quit by entering an empty row.")
    text = []
    while True:
        line = input()
        if line == "":
            break
        text.append(line)
    return text
def how_many_words_for_new_line(text, start_index, width):
    """
    Check how many words can fit on new line.
    :return: number of words that can fit.
    """
    new_line = ""
    numberOfWords = 0
    while len(new_line) < width:
        if start_index + numberOfWords >= len(text):
            break
        new_line += text[start_index + numberOfWords]
        new_line += " "
        numberOfWords += 1
        print(len(new_line))
    return numberOfWords - 1
def create_new_line(text, start_index, width, wordsToAdd):
    """
    Creates the new line with appropriate spacing.
    """
    # loop until width wide
    words = text[start_index:start_index + wordsToAdd]
    " ".join(words)
    print(words)
    # while len(new_line) < width:
    #     pass
def even_text_to_width(text, width):
    """
    Even text lines to width nubmer of characters.
    :param text: str
    :param width:, int
    :return: str, evened text
    """
    split_text = text.split()
    print(split_text)
    evened_text = []
    new_line = ""
    word_counter = 0
    while word_counter < len(split_text):
        words_on_new_line = 0
        wordsToAdd = how_many_words_for_new_line(split_text, word_counter, width)
        new_line = create_new_line(split_text, word_counter, width, wordsToAdd)
        # while len(new_line) < width:
        #     new_line += split_text[word_counter]
        #     new_line += " "
        #     words_on_new_line = + 1
        #     word_counter += 1
        #     if word_counter >= len(split_text):
        #         break
        #     if len(new_line) > width:
        #         pass
        word_counter += 1
        evened_text.append(new_line)
        new_line = ""
    return evened_text
def main():
    # text = input_text()
    text = """CHAPTER VIII - CONCERNING THOSE WHO HAVE OBTAINED A PRINCIPALITY BY
WICKEDNESS
Although a prince may rise from a private station in two ways, neither
of which can be entirely attributed to fortune or genius, yet it is
manifest to me that I must not be silent on them, although one could be
more copiously treated when I discuss republics. These methods are
when, either by some wicked or nefarious ways, one ascends to the
principality, or when by the favour of his fellow-citizens a private
person becomes the prince of his country. And speaking of the first
method, it will be illustrated by two examples--one ancient, the other
modern--and without entering further into the subject, I consider these
two examples will suffice those who may be compelled to follow them."""
    width = int(input("Enter the number of characters per line: "))
    evened_text = even_text_to_width(text, width)
    for i in range(len(evened_text)):
        print(evened_text[i] + " ("+str(len(evened_text[i])) + ")")
if __name__ == "__main__":
    main()