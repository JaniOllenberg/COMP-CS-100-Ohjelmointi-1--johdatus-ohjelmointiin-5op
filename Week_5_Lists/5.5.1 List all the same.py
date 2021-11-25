"""
COMP.CS.100 Programming 1
5.5.1 Check if all members of list are the same
Jani Ollenberg
H288244
"""
def are_all_members_same(list_to_check):
    """
    Check if list members are all same.
    :param: list
    :return: True or False
    """
    first_value = list_to_check[1]
    for i in list_to_check:
        if i != first_value:
            return False
    return True
def main():
    print(are_all_members_same([42, 42, 42, 43, 42]))
    print(are_all_members_same([1,1,1,1,1]))
    

if __name__ == "__main__":
    main()