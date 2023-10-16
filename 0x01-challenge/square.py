#!/usr/bin/python3

class Square:
    """
    A class representing a square.

    Attributes:
        width (int): The width of the square.
        height (int): The height of the square
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a Square object.

        Args:
            width (int): The width of the square.
            height (int): The height of the square (optional, defaults to 0).
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.width * self.width

    def perimeter(self):
        """
        Calculate and return the perimeter of the square.

        Returns:
            int: The perimeter of the square.
        """
        return 4 * self.width

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: A string representing the square's dimensions.
        """
        return f"Square({self.width})"


if __name__ == "__main":
    s = Square(width=12)
    print(s)
    print("Area:", s.area())
    print("Perimeter:", s.perimeter())
