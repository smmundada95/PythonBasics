import math

def area_of_triangle(base, height):
    return base * height / 2

def perimeter(side1, side2, side3):
    return side1 + side2 + side3

def semi_perimeter(side1, side2, side3):
    return perimeter(side1, side2, side3)/2

def area_hero(side1, side2, side3):
    semi = semi_perimeter(side1, side2, side3)
    area = math.sqrt(semi * (semi - side1) * (semi - side2) * (semi - side3))
    return area

area = area_hero(3,4,5)
