class Polygon: #the class name always start with a variable 
    def __init__(self, sides, name):
        self.sides = sides
        self.name = name

square = Polygon(4, "sqaure")
pentagon = Polygon(5, "pentagon")

print(square.sides)
print(square.name)


print(pentagon.sides)
print(pentagon.name)
