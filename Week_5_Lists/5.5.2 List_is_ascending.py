"""
COMP.CS.100 Programming 1
5.5.2 Check if list is sorted.
Jani Ollenberg
H288244
"""
def is_the_list_in_order(list_to_check):
    """
    check if list is same as sorted list
    :param: list to check
    :return: True or False
    """
    if list_to_check == sorted(list_to_check):
        return True
    else:
        return False
def main():
    print(is_the_list_in_order([1,2,3,4,5,6,7]))
    print(is_the_list_in_order([1,2,3,4,5,8,7]))
    print(is_the_list_in_order([]))
if __name__ == "__main__":
    main()