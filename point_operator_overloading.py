from re import X
from tokenize import Pointfloat
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
         self.x  = x
         self.y = y

        #Operating overloading class method
    def __add__(self, other):
        if isinstance(other, Point): #instance of other inputs 
            x = self.x + other.x
            y = self.y + other.y
            return Point(x,y)
        else:
            x = self.x + other
            y  = self.y + other
            return Point(x,y)




    def plot(self):
        plt.scatter(self.x, self.y)

a = Point(2,3)
b = Point(2,3)
#b = a + 5

c = a + b 
c.plot()
plt.show()
#print (c.x, c.y) # this will return (4,6)