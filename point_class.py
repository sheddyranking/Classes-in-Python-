import matplotlib.pyplot as plt

class Piont:
     def __init__(self, x, y):
         self.x  = x
         self.y = y

     def plot(self):
        plt.scatter(self.x, self.y)


graph = Piont(4 ,5)
graph.plot()

plt.show()
          