class Shape:
    def __init__(self):
        pass
    def area(self):
        print(f"Area not defined for generic shape.")

class Rectangle(Shape):
    def __init__(self, width, length):
        super().__init__()
        self.width = width
        self.length = length
    def area(self):
        print(f"Area of rectangle: {self.width * self.length}")

r1 = Rectangle(5, 10)
r1.area()