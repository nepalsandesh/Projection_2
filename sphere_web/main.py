import pygame
import numpy
import sys
from rendering_objects import Sphere




class Render:
    """Render class , consisting main loop"""
    
    def __init__(self):
        pygame.init()
        self.WIDTH, self.HEIGHT = 1920,1080
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
    
    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
    
    def update(self):
        self.clock.tick()
        pygame.display.flip()
        pygame.display.set_caption(str(self.clock.get_fps()))
    
    def draw(self):
        self.screen.fill('black')
        sph.create_sphere()
        sph.draw_points(self.screen, (255,255,255), 10)

        
    def run(self):
        while True:
            self.check_event()
            self.draw()
            self.update()


    
if __name__ == '__main__':
    render = Render()
    sph = Sphere(300, (render.WIDTH, render.HEIGHT), 10)
    render.run()
