"""
Ohjelmointi 1 / Programming 1
Trangle's Area when the Sides Are Known
Jani Ollenberg
H288244
"""

from math import sqrt

def area(a, b, c):
    """
    Calculates area of a triangle
    :a, b, c: side lengths of the triangle
    :return: area
    """
    
    perimeter = a + b + c
    s = perimeter/2
    area = sqrt((s)*(s - a)*(s - b)*(s - c))
    return area

def main():
    line1 = float(input("Enter the length of the first side: "))
    line2 = float(input("Enter the length of the second side: "))
    line3 = float(input("Enter the length of the third side: "))

    triangle_area = area(line1, line2, line3)
    print(f"The triangle's area is {triangle_area:.1f}")


if __name__ == "__main__":
    main()
