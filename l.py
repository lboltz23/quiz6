
class Shape:
    def get_area(self):
        print("The shape area")

class ShapeWithWidth:
    def set_width(self, width):
        self.width = 0
        print("The width is 0")
class ShapeWithHeight:
    def set_height(self, height):
        self.height = 0
        print("The height is 0")
class CircleShape:
    def set_radius(self, width, height):
        self.radius = height/2
        print("The radius is ", self.radius)

class RectangleArea:
    def get_area(self):
        area = self.width * self.height
        print(area)
    
    
class Circle(Shape, CircleShape, ShapeWithWidth, ShapeWithHeight):
    def get_area():
        print("Circle area:")
    def set_width(self, width):
        self.width = width
        print("The width is set",self.width)
    def set_height(self, height):
        self.height = height
        print("The height is set", self.height)
    def set_radius(self, width, height):
        self.radius = height/2
        print("The radius is ", self.radius)    

class Rectangle(Shape, RectangleArea, ShapeWithWidth, ShapeWithHeight):
    def get_area(self):
        area = self.width * self.height
        print(area)
        print("Rectanglle area")

    def set_width(self,width):
        self.width = width
        print("The width is ", self.width)

    def set_height(self, height):
        self.height = height
        print("The height is", self.height)
class Triangle(Shape):
    def get_area(self):
        area = self.width * self.height
        print("Triangle area", area)

def set_width_and_height(shape, width, height):
    if isinstance(shape, ShapeWithHeight):
        shape.set_height(height)
    if isinstance(shape, ShapeWithWidth):
        shape.set_width(width)
    if isinstance(shape,(CircleShape)):
        shape.set_radius(width, height)
    elif isinstance(shape, Shape):
        shape.width = width
        shape.height = height
        shape.get_area()


def main():

    triangle = Triangle()
    shape2 = Rectangle()
    shape3 = Circle()

    set_width_and_height(shape2, 3, 4)

if __name__ == "__main__":
    main()