#!/usr/bin/python3

class Square():
    """A class representing a square."""

    def __init__(self, side_length):
        """
        Initialize a Square object with the given side length.

        Args:
            side_length (int): The side length of the square.
        """
        self.width = side_length
        self.height = side_length

    def area_of_my_square(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.width * self.width

    def perimiter_of_my_square(self):
        """
        Calculate the perimeter of the square.

        Returns:
            int: The perimeter of the square.
        """
        return self.width * 4

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: A string in the format 'width/height'.
        """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(side_length=12)
    print(s)
    print(s.area_of_my_square())
    print(s.perimiter_of_my_square())
