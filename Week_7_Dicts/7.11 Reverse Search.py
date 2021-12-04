"""
COMP.CS.100 Programming 1
Implementation of reverse dictionary search.
Jani Ollenberg
H288244
"""

def reverse_search_from_dictionary(dictionary, payload):
    """
    Search for the keys of a dictionary that are associated with the payload.
    A simple loop-based solution.

    :param dictionary: dict, the keys are searched from this data structure.
    :param payload: any type, payload for which the keys are searched for.
    :return: list, keys associated with payload equal to the given payload.
    An empty list is returned, if no keys with the payload are found.
    """
    # Several keys may have an equal payload.
    found_keys = []

    # Get the keys of the dictionary.
    keys = dictionary.keys()

    # Search for the keys linearly.
    for key in keys:
        # Add the current key to the end of the list, if its payload is equal
        # to the given one.
        if dictionary.get(key) == payload:
            found_keys.append(key)

    # Return the result.
    return found_keys

def populate_dictionary():
    """
    Creates, fills and returns a dictionary. The entries are atomic and they
    are read from the user.

    :return: dict, a populated dictionary.
    """
    dictionary = {}
    another_entry = True

    while another_entry:
        key = input("Enter a key (empty key stops): ")
        if key != "":
            payload = input("Enter a payload: ")
            dictionary[key] = payload
        else:
            another_entry = False

    return dictionary

def main():
    # Read the entries from the user.
    entries = populate_dictionary()

    # Read the payload for the reverse search.
    payload = input("Enter payload for the reverse search: ")

    # Do the reverse search from the dictionary.
    search_result = reverse_search_from_dictionary(entries, payload)

    # Report result.
    print(search_result)

if __name__ == "__main__":
    main()
