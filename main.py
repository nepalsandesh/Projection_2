import pygame
import object_operation
import random

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
FPS = 1

points = [(random.randint(-100,100), random.randint(-100,100), random.randint(-100,100)) for i in range(50)]



obj = object_operation.Object(100, 200, points, (1920, 1080))

distance = 200


while True:
    # clock.tick(1)
    screen.fill((0,0,0))
    # [exit() for event in pygame.event.get() if event.type == pygame.QUIT]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
                
            # if event.key == pygame.K_w:
            #     print("==================++++++++++++++")
            #     obj.scale *= 1.1
                
            # if event.key == pygame.K_s:
            #     print("==================++++++++++++++")
            #     obj.scale /= 1.1
                
            # if event.key == pygame.K_UP:
            #     print("==================++++++++++++++")
            #     distance *= 1.1
                
            # if event.key == pygame.K_DOWN:
            #     print("==================++++++++++++++")
            #     distance /= 1.1
        
            obj.handle_event(event)
        


    points_array =  obj.get_projected_array(save=True, limit=5000)



    for point in points_array:
        pygame.draw.circle(screen, (0,255,255), point, 5)


    # for point in points_array:
    #     pygame.draw.line(screen, (155, 155, 0), point, points_array[0])
         
    
    # pygame.draw.lines(screen, (155, 155, 100), True, points_array, 1)
    # for point in points_array:
    #     pygame.draw.line(screen, (155, 100, 255), point, random.choice(points_array))
    
    
    if len(obj.corners) > 2:
        # pygame.draw.lines(screen, (144,244,44), False, obj.corners)
        for i in obj.corners:
            pygame.draw.circle(screen, (118, 118,255), i, 1)
    
        
    # obj.rotate_x(0.0005)
    obj.rotate_y(0.01)
    obj.rotate_z(0.01)
    
    pygame.display.flip()
    
    
    
    
    