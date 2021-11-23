"""
COMP.CS.100 Programming 1
Compare floating-point decimals with epsilon precision
Jani Ollenberg
H288244
"""

def compare_floats(value1, value2, epsilon):
    """
    Compares floats.
    :param value1, value2,epsilon:
    :return:
    """
    if abs(value1 - value2) < epsilon:
        return True
    else:
        return False

def main():
    EPSILON = 0.000000001
    print(compare_floats(0.00000000000000000001, 0.0000000000000000002, EPSILON))

    print(compare_floats(0.0002, 0.0000002, EPSILON))


if __name__ == "__main__":
    main()