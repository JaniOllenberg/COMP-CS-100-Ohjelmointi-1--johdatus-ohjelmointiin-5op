"""
COMP.CS.100 Programming 1
Find the longest substring with alphabetically ordered characters.
Jani Ollenberg
H288244
"""
def longest_substring_in_order(text):
    """
    Find the longest substring in alphabetical order.
    :param text: str
    :return: str
    """
    previous_longest = ""
    most_longest = ""
    last_char_checked = ""
    for i in range(len(text)):
        for j in range(i, len(text)):
            substring = text[i:j+1]
            if j == i:
                if text[j] >= text[j]:
                    previous_longest = substring
            else:
                if text[j] >= text[j-1]:
                    previous_longest = substring
                else:
                    last_char_checked = text[j]
                    break
        if len(previous_longest) > len(most_longest):
            most_longest = previous_longest
        previous_longest = last_char_checked
    return most_longest
def main():
    text = input("Give text: ")
    print(longest_substring_in_order(text))
    print(longest_substring_in_order("abcabcdefgabab"))
    print(longest_substring_in_order("acdkbarstyefgioprtyrtyx"))

if __name__ == "__main__":
    main()