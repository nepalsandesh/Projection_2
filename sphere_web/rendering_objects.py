import pygame
import numpy as np


class Sphere:
    """Rendering body object class"""
    
    def __init__(self, radius, screen_size, no_of_points):
        self.radius = radius
        self.screen_size = screen_size
        self.WIDTH , self.HEIGHT = self.screen_size
        self.no_of_points = no_of_points
        self.sphere_coordinate = []
        self.create_sphere()
        
        
    def create_sphere(self):
        self.sphere_coordinate = []
        for i in np.arange(0,self.no_of_points):
            rand_angle = np.random.rand() * np.pi*2
            point = [np.cos(rand_angle)*self.radius + self.WIDTH//2 , np.sin(rand_angle)*self.radius + self.HEIGHT//2]
            self.sphere_coordinate.append(point)

    def get_sphere_coordinate(self):
        return self.sphere_coordinate
        

    def draw_points(self, screen, color, points_radius):
        for i in self.sphere_coordinate:
            pygame.draw.circle(screen, color, i, points_radius)
    
