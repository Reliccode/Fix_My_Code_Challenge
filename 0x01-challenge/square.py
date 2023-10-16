#!/usr/bin/python3

class Square:

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def perimeter_of_my_square(self):
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main":
    s = Square(width=12, height=9)
    print(s)
    print("Area of my square:", s.area_of_my_square())
    print("Perimeter of my square:", s.perimeter_of_my_square())
