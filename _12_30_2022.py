import pygame
import numpy


class Object:
    def __init__(self, scale, distance, matrix):
        self.scale = scale
        self.distance = distance
        self.matrix = matrix
        
    def modify_matrix(self, function=None):
        for x in range(numpy.shape(self.matrix)[0]):
            for y in range(numpy.shape(self.matrix)[1]):
                for z in range(numpy.shape(self.matrix)[2]):
                    self.matrix[x,y,z] = x+y+z
                                 
    
    
    
    def get_matrix(self):
        return self.matrix
                    
        
        
            
arr = numpy.zeros((5,5,5))

obj = Object(1, 1, arr)

obj.modify_matrix()

new_arr = obj.get_matrix()

print(new_arr)