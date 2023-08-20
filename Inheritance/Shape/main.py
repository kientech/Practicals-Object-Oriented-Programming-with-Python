import math

class Shape:
    def area(self):
        pass
    
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def __str__(self):
        return f'Circle area: {self.area():.2f}'
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f'Rectangle area: {self.area():.2f}'
        
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height
    
    def __str__(self):
        return f'Triangle area: {self.area():.2f}'
    

circle = Circle(2)
print(circle)

rectangle = Rectangle(2, 5)
print(rectangle)

triangle = Triangle(3, 8)
print(triangle)
