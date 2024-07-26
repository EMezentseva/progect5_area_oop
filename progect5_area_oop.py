from math import pi


class Shape:
    def calculate_area(self):
        return None


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return round(pi * self.radius**2, 2)


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        

    def calculate_area(self):
        self.sides = [self.side1, self.side2, self.side3]
        self.sides.sort()
        if (self.sides[2]) * 2 == (self.sides[1]) * 2 + (self.sides[0]) ** 2: #проверка: является ли треугольник прямоугольным
            return round(self.sides[1] * self.sides[0] / 2, 2)
        else:
            self.p = (self.side1 + self.side2 + self.side3) / 2  
            return round((self.p * (self.p - self.side1) * (self.p - self.side2) * (self.p - self.side3)) ** 0.5, 2)
       
        

shapes = [Circle(5), Triangle(3, 5, 4)] #ввести значения

for Shape in shapes:
    area = Shape.calculate_area()
    print(f"Area of {type(Shape).__name__}: {area}")

# Тесты для проверки
circle = Circle(5)
assert round(circle.calculate_area(), 2) == 78.54

triangle = Triangle(3, 5, 4)
assert round(triangle.calculate_area(), 2) == 6.00  