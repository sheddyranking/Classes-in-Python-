import matplotlib.pyplot as plt

class Point:
     def __init__(self, x, y):
         self.x  = x
         self.y = y

     def plot(self):
        plt.scatter(self.x, self.y)


graph = Point(4 ,5)
graph.plot()

plt.show()
          