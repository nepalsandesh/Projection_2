import numpy as np
import pygame



class Cartesian:
    """A class for creating and displaying x,y axis"""
    
    def __init__(self, width, height, scale):
        self.width = width
        self.height = height
        self.scale = scale
        

    
    def draw_axis(self, screen , color, line_width):
        x_left = (0 , self.height//2)
        x_right =  (self.width, self.height//2)
        y_top = (self.width//2, 0)
        y_bottom = (self.width//2, self.height)
        
        pygame.draw.line(screen, color, x_left, x_right, line_width)
        pygame.draw.line(screen, color, y_top, y_bottom, line_width)