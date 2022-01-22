import turtle
 
class Polygon: #the class name always start with a upper case variable 
    def __init__(self, sides, name):
        self.sides = sides
        self.name = name

    #drawing the shape base on the parametres passed into the class.
    #to do that we define a CLASS METHOD.

    def draw(self):
        for i in range(self.sides):
            turtle.forward(100)
            turtle.right(90)
        turtle.done()

 

square = Polygon(4, "sqaure")
pentagon = Polygon(5, "pentagon")

print(square.sides)
print(square.name)


print(pentagon.sides)
print(pentagon.name)

square.draw()