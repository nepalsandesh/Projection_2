import pygame
import numpy
from math import sin, cos



width, height = 1920, 1080
black, white, blue = (0,0,0), (255,255,255), (20, 20, 255)
centre = (width//2, height//2)


pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Persective Cube Projection")
clock = pygame.time.Clock()
FPS = 60

points = []
points.append(numpy.matrix([-1, -1, 1]))
points.append(numpy.matrix([1, -1, 1]))
points.append(numpy.matrix([1, 1, 1]))
points.append(numpy.matrix([-1, 1, 1]))
points.append(numpy.matrix([-1, -1, -1]))
points.append(numpy.matrix([1, -1, -1]))
points.append(numpy.matrix([1, 1, -1]))
points.append(numpy.matrix([-1, 1, -1]))


scale = 800
theta = 0
perspective_distance = 5


spiro_list = []

def spiro_draw(points):
    if len(points) > 1:
        pygame.draw.lines(screen, blue, False, points)
        for point in points:
            pygame.draw.circle(screen, (255, 255, 0), point, 2)



while True:
    clock.tick(FPS)
    screen.fill(black)
    pygame.display.set_caption(str(clock.get_fps()))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
                
    
    rotation_x = numpy.matrix([
        [1, 0, 0],
        [0, cos(theta), -sin(theta)],
        [0, sin(theta), cos(theta)]
    ])
    
    rotation_y = numpy.matrix([
        [cos(theta), 0, -sin(theta)],
        [0, 1, 0],
        [sin(theta),0, cos(theta)]
    ])
    
    rotation_z = numpy.matrix([
        [cos(theta), -sin(theta), 0],
        [sin(theta), cos(theta), 0],
        [0, 0, 1]
    ])
                
    for point in points:
        rotated_3d = numpy.dot(rotation_x, point.reshape(3,1))
        rotated_3d = numpy.dot(rotation_y, rotated_3d)
        # rotated_3d = numpy.dot(rotation_z, rotated_3d)
        
        perspective = 1/(perspective_distance - rotated_3d[2])
        
        projection_matrix = numpy.matrix([
            [perspective, 0, 0],
            [0, perspective , 0]
        ])
        
        projected_2d = numpy.dot(projection_matrix, rotated_3d)
        
        x = int(projected_2d[0] * scale + centre[0])
        y = int(projected_2d[1] * scale + centre[1])
        
        
        spiro_list.append([x,y])
        if len(spiro_list) > 300:
            spiro_list.pop(0)
        spiro_draw(spiro_list)
        # pygame.draw.circle(screen, white, (x,y), 60)
        
        exmple_array = []

        
    theta += 0.01
    pygame.display.flip()