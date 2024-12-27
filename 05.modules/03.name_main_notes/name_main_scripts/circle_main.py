import math
import sys


def area(radius):
    radius_pow = math.pow(radius, 2)
    area = math.pi * radius_pow
    return area


def perimeter(radius):
    return 2 * math.pi * radius


# "sys.argv" is used to pass argument through CLI
# if __name__ == "__main__":
#     file_name = sys.argv[0]
#     radius = float(sys.argv[1])
#     print(f"File name: {file_name}")
#     print(f"Radius is {radius}")
#     print(f"The Circle Area with radius = {radius} equal {area(radius)}")


# It is a good practice not to put multiple lines of code within the
# "if __name__ == "__main__"" instead define the main() function,

# Better Practice:
def main():
    file_name = sys.argv[0]
    radius = float(sys.argv[1])
    print(f"File name: {file_name}")
    print(f"Radius is {radius}")
    print(f"The Circle Area with radius = {radius} equal {area(radius)}")
    print(f"The Circle Perimeter with radius = {radius}\
 equal {perimeter(radius)}")


if __name__ == "__main__":
    main()
