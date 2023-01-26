import pygame
from array_operations import Cartesian
import sympy
import numpy


pygame.init()


width, height = 1920, 1080
resolution = width, height


screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()
FPS = 60

# =================== Other objects and variables  ===================
axis = Cartesian(width, height, 1)




# ========================================================

# Functions
def handle_input():
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        return exit()
    

# Sympy stuffs------------------------
x = sympy.symbols('x')
fx = sympy.sin(x) * 100


x_arr = numpy.linspace(0, 1920,150)


# ------------------------------------

while True:
    
    clock.tick(FPS)
    screen.fill((0,0,0))
    handle_input()
    
    # drawing stuffs
    axis.draw_axis(screen, (155,155,155), 5)

    
    for i in range(0,len(x_arr)):
        y = fx.subs(x, x_arr[i])
        
        pygame.draw.circle(screen, (155,55,155), numpy.floor((x_arr[i], y+height//2)), 5)
    
    
    pygame.display.flip()
    pygame.event.pump()