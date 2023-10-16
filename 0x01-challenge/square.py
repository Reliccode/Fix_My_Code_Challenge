#!/usr/bin/python3

class Square():

    def __init__(self, side_length):
        self.width = side_length
        self.height = side_length

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def perimiter_of_my_square(self):
        """ Perimeter of the square """
        return self.width * 4

    def __str__(self):
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(side_length=12)
    print(s)
    print(s.area_of_my_square())
    print(s.perimiter_of_my_square())
