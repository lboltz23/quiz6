from abc import ABC, abstractmethod

class Area(ABC):
    @abstractmethod
    def get_area(self, length, width, radius):
        print("area")

class RectangleArea(Area):
    def get_area(self, length, width, radius):
        print("rectangle area")

class SquareArea(Area):
    def get_area(self, length, width, radius):
        print("square area")

class CircleArea(Area):
    def get_area(self, length, width, radius):
        print("circle area")

class TriangleArea(Area):
    def get_area(self, length, width, radius):
        print("triangle area")

class EquiTriangleArea(Area):
    def get_area(self, length, width, radius):
        print("equilateral triangle area")
class ParallelogramArea(Area):
    def get_area(self, length, width, radius):
        print("parallelogram area")

class Shape:
    def __init__(self, length, width, radius):
        self.length = length
        self.width = width
        self.radius = radius

    def get_area(self, areamethod):
        areamethod.get_area(self.length, self.width, self.radius)
  

def main():
    area1 = Shape(0, 0, 5)
    area2 = Shape(4, 5, 0)
    print("Areas of shapes:")
    area1.get_area(CircleArea())
    area2.get_area(SquareArea())

if __name__ == "__main__":
    main()