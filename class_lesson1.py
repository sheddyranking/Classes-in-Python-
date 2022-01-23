import turtle
 
class Polygon: #the class name always start with a upper case variable 
    def __init__(self, sides, name, size, color ="red",line_thickness = 2):
        self.sides = sides
        self.name = name
        self.size = size
        self.color = color
        self.line_thickness = line_thickness

    #drawing the shape base on the parametres passed into the class.
    #to do that we define a CLASS METHOD.

    def draw(self):
        turtle.color(self.color)
        turtle.pensize(self.line_thickness)
        for i in range(self.sides):
            turtle.forward(self.size)
            turtle.right(90)
        turtle.done()

 

square = Polygon(4, "sqaure", 100)
pentagon = Polygon(5, "pentagon", 100)

print(square.sides)
print(square.name)


print(pentagon.sides)
print(pentagon.name)

square.draw()