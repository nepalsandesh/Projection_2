import pygame
import numpy
import object_operation
import random
from shapes import *
import torus
import _12_30_2022 as dec30
from circle import Circle
from new_approach.array_operations import Cartesian

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
FPS = 60


axis = Cartesian(1920,1080,1)

# points = [(random.randint(-100,100), random.randint(-100,100), random.randint(-100,100)) for i in range(100)]

cuboid = []

for x in range(5):
    for y in range(5):
        for z in range(5):
            cuboid.append((x-2.5,y-2.5,z-2.5))


points = numpy.array(torus.Points())
# points = tetrahedron

circle = Circle(50, 5)




# points = cuboid
# points = circle.get_coordinates()
scale = 10000
number_of_points = len(points)



obj = object_operation.Object(scale, 200, points, (1920, 1080))

distance = 200
angle = 0.01
pause = False

obj2 = dec30.Object(10, 10, numpy.zeros((5,5,5)))
obj2.modify_matrix()


control = False

while True:
    clock.tick(FPS)
    screen.fill((0,0,0))
    # [exit() for event in pygame.event.get() if event.type == pygame.QUIT]
    pygame.display.set_caption(str(clock.get_fps()))
    
    points_array =  obj.get_projected_array(save=True, limit=5000)


    obj.handle_event()


    



    """Under Development Renderings"""
    # for point in points_array:
    #     pygame.draw.line(screen, (155, 155, 0), point, points_array[10])
         
    
    # pygame.draw.lines(screen, (155, 155, 100), True, points_array, 1)
    # for point in points_array:
    #     pygame.draw.line(screen, (155, 100, 255), point, random.choice(points_array))
    
    
    # for point in points_array:
        # pygame.draw.circle(screen, (0,255,255), point, 5)

    # for i in range(len(points_array)):
    #     pygame.draw.line(screen, (155,155,25), points_array[i-1], points_array[i], 5)

                # pass
        

    
    
    
    if len(obj.corners) > 2:
        # pygame.draw.lines(screen, (144,244,44), False, obj.corners)
        for i in obj.corners:
            # pygame.draw.circle(screen, (118, 118,255), i, 1)
            pass
    
    
    
    """Drawing stuffs here"""
    


    # obj.draw_lines(screen=screen, color=(100, 20, 70))   
    obj.draw_ellipse(screen, line=False, numv=100)
    # obj.draw_ellipses(number_of_points, screen)
    # obj.connect_points(screen, torus.Indexes())

    
    # for tetrahedron points connection
    # for points in tetrahedron_connection:
        # pygame.draw.lines(screen, (255,255,255), False, obj.coordinates(), 1)
    
    axis.draw_axis(screen, (75,75,75), 2)
    
    pygame.display.flip()
    pygame.event.pump()


    

    
    
    
    
    
