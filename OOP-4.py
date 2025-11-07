## OVERRIDING....

class Shape:
    def area(self):
        return "Generic Shape Area Calculation"
    
class Rectangle(Shape):
    def __init__(self , width , height):
        self.width = width
        self.height = height

    def area(self):
        return self.width*self.height


s = Shape()
r = Rectangle(10,3)

print(f"Shape area : {s.area()}")
print(f"Rectangle area: {r.area()}")

