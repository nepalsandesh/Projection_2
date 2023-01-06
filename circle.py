import pygame
import numpy
import sympy


class Circle:
    """Making and getting a circle object"""
    
    def __init__(self, points, scale=1):
        self.x = numpy.linspace(0, numpy.pi*2, points)
        self.scale = scale
    
    
    def get_coordinates(self):
        """returns the cartesian coordinates of a circle"""
        arr = numpy.zeros((len(self.x), 3))
        for i in range(len(arr)):
            arr[i] = [numpy.cos(self.x[i])*self.scale, numpy.sin(self.x[i])*self.scale, 0]#(numpy.cos(self.x[i])*numpy.sin(self.x[i]))*self.scale]
        
        # print(arr)
        return arr
            


c = Circle(4, 10)

c.get_coordinates()