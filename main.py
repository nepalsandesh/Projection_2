import pygame
import object_operation
import random

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
FPS = 1

points = [(random.randint(-100,100), random.randint(-100,100), random.randint(-100,100)) for i in range(100)]



obj = object_operation.Object(100, 200, points, (1920, 1080))

distance = 200


while True:
    clock.tick()
    screen.fill((0,0,0))
    # [exit() for event in pygame.event.get() if event.type == pygame.QUIT]
    pygame.display.set_caption(str(clock.get_fps()))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
                   
            obj.handle_event(event)
        


    points_array =  obj.get_projected_array(save=True, limit=5000)



    for point in points_array:
        pygame.draw.circle(screen, (0,255,255), point, 5)


    """Under Development Renderings"""
    # for point in points_array:
    #     pygame.draw.line(screen, (155, 155, 0), point, points_array[0])
         
    
    # pygame.draw.lines(screen, (155, 155, 100), True, points_array, 1)
    # for point in points_array:
    #     pygame.draw.line(screen, (155, 100, 255), point, random.choice(points_array))
    
    
    # if len(obj.corners) > 2:
    #     pygame.draw.lines(screen, (144,244,44), False, obj.corners)
    #     for i in obj.corners:
    #         pygame.draw.circle(screen, (118, 118,255), i, 1)
    
    
    
    """Drawing stuffs here"""
        
    # obj.rotate_x(0.01)
    # obj.rotate_y(0.01)
    obj.rotate_z(0.01)
    
    # obj.draw_lines(screen=screen, color=(118,199,255))
    obj.draw_ellipse(screen, line=True, numv=100)
    
    
    pygame.display.flip()
    
    
    
    
    
