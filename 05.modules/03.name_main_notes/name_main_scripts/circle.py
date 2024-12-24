import math


def area(radius):
    radius_pow = math.pow(radius, 2)
    area = math.pi * radius_pow
    return area


# print(area(2))
# print(__name__)

if __name__ == "__main__":
    print(area(2))
    print(__name__)
