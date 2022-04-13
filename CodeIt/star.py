class ShapePrinter:
    def __init__(self, height):
        self.height = height
    
    def printTriangle(self):
        for i in range(1, self.height + 1):
            print("*" * i)
        return "----------"
shape_1 = ShapePrinter(3)
shape_2 = ShapePrinter(5)
shape_3 = ShapePrinter(10)
print(shape_1.printTriangle())
print(shape_2.printTriangle())
print(shape_3.printTriangle())