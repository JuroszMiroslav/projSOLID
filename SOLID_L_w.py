from typing import List

# Rectangle class
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    # Calculate rectangle area
    def calculate_area(self):
        return self._width * self._height

# Square class, inherits from Rectangle
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    @property
    def width(self):
        return self._width

    @width.setter
    # In square, setting width also sets height
    def width(self, value):
        self._width = self._height = value

    @property
    def height(self):
        return self._height

    @height.setter
    # In square, setting height also sets width
    def height(self, value):
        self._height = self._width = value

    # Calculate square area
    def calculate_area(self):
        return self._width * self._width

# Function to calculate total area of multiple rectangles
def calculate_total_area(rects:List[Rectangle]):
    total_area = 0
    for obj in rects:
        total_area += obj.calculate_area()
    return total_area

rects = [Rectangle(5,6),Square(10)]
print (calculate_total_area(rects))