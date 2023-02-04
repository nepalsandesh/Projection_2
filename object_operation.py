import pygame
import numpy
from math import sin, cos
import random
from numba import jit


class Object:
    """This is an Object class where 3d object can be created and different operations can be done"""
    
    def __init__(self, scale, distance,  coordinates_array, resolution):
        self.scale = scale
        self.distance = distance
        
        self.coordinates = self.create_object(coordinates_array)
        self.resolution = resolution
        self.corners = []
        self.connect_points = []
        
    
    # This function takes array of points and converts into numpy (3,1) matrix of each point
    def create_object(self, coordinates_array):
        coordinates = []
        for coordinate in coordinates_array:
            coordinates.append(numpy.matrix([
                [coordinate[0]],
                [coordinate[1]],
                [coordinate[2]]
            ]))
        return coordinates
            

    # Rotation on x-axis
    def rotate_x(self, angle):
        rotation_x_matrix = numpy.matrix([
            [1, 0, 0],
            [0, cos(angle), -sin(angle)],
            [0, sin(angle), cos(angle)]
        ])
        self.coordinates = [numpy.dot(rotation_x_matrix, point) for point in self.coordinates]
    
    
    # Rotation on y-axis
    def rotate_y(self, angle):
        rotation_y_matrix = numpy.matrix([
            [cos(angle), 0, -sin(angle)],
            [0, 1, 0],
            [sin(angle), 0, cos(angle)]
        ])  
        self.coordinates = [numpy.dot(rotation_y_matrix, point) for point in self.coordinates]
            
    
    # Rotation on z-axis
    def rotate_z(self, angle):
        rotation_z_matrix = numpy.matrix([
            [cos(angle), -sin(angle), 0],
            [sin(angle), cos(angle), 0],
            [0, 0, 1]
        ])
        self.coordinates = [numpy.dot(rotation_z_matrix, point) for point in self.coordinates]
    

    def get_projected_array(self, save=False, limit=10):
        # z =  1/(distance - self.)
        # perspective_matrix = numpy.matrix([
        #     [z, 0, 0],
        #     [0, z, 0]
        # ])
        
        # self.coordinates = [numpy.dot(perspective_matrix, point) for point in self.coordinates]
        array = []
        for i in range(len(self.coordinates)):
            z = 1/(self.distance - self.coordinates[i][2])
            projection_matrix = numpy.matrix([
                [z, 0, 0],
                [0, z, 0]
            ])
            coordinate = numpy.dot(projection_matrix, self.coordinates[i])
        
            x = int(coordinate[0]*self.scale + self.resolution[0]//2)
            y = int(coordinate[1]*self.scale + self.resolution[1]//2)
            array.append((x, y))
            
            _2d_point = [x,y]
            
            if save == True:
                self.append_corners(_2d_point)
                
                if len(self.corners) > limit:
                    self.corners.pop(0)
                             
        return array
            
        
    
    def handle_event(self):
        """Event handler for the object"""
        
        rotate = not False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_x]:
            self.rotate_x(0.01)
            
        if keys[pygame.K_y]:
            self.rotate_y(0.01)

        if keys[pygame.K_z]:
            self.rotate_z(0.01)

        if keys[pygame.K_w]:
            self.scale *= 1.01

        if keys[pygame.K_s]:
            self.scale /= 1.01
            
        if keys[pygame.K_UP]:
            self.distance *= 1.01

        if keys[pygame.K_DOWN]:
            self.distance /= 1.01  
             
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            return exit()
            
            
            
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         pygame.quit()
                
                
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_ESCAPE:
        #             pygame.quit()
                    
        #         if event.key == pygame.K_w:
        #             print("Hi")
        #             self.scale *= 1.08
                    
        #         if event.key == pygame.K_s:
        #             self.scale /= 1.08
                    
        #         if event.key == pygame.K_x:
        #             self.rotate_x(1)
        
        # if event.type == pygame.KEYDOWN:
            

        #     if event.key == pygame.K_SPACE:
        #         pause = True
                
        #     if event.key == pygame.K_r:
        #         control = True


        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_SPACE:
        #         pause = False
                
        #     if event.key == pygame.K_r:
        #         control = False
        

        # if event.key == pygame.K_UP:
        #     print("==================++++++++++++++")
        #     self.distance *= 1.05
            
        # if event.key == pygame.K_DOWN:
        #     print("==================++++++++++++++")
        #     self.distance /= 1.05
        
        

    def  append_corners(self, _2dPoint):
        self.corners.append(_2dPoint)
        
    def get_corners(self):
        return self.corners
    
    def draw_lines(self, screen, color):
        if len(self.corners) > 2:
            pygame.draw.lines(screen, color, False, self.corners, 1)    


    def draw_ellipse(self, screen,numv, color=(118,118,255), line=False):
        if len(self.corners) > 2:
            for i in range(len(self.corners)):
                pygame.draw.circle(screen, color, self.corners[i], 1)
                if line == True:
                    if len(self.corners)%numv == 0:
                    # pass
                        # print("svajrvnvsjsvnsvnvwinweiufwe")
                        if len(self.corners) > numv:
                            pygame.draw.line(screen, (55, 155, 55), self.corners[numv], self.corners[i], 1)
                            
                            
    
    def draw_ellipses(self, number_of_points, screen, ):
        for i in range(len(self.corners)):
        
            print("++++++______--------->>>>>>>")
            pygame.draw.line(screen, (255,155,55), self.corners[i], self.corners[i-number_of_points], 1)
            

    def connect_points(self, screen, points_sequence):
        # connection = []
        # for i in range(len(points_sequence)):
        #     z = 1/(self.distance - points_sequence[i][2])
        #     projection_matrix = numpy.matrix([
        #         [z, 0, 0],
        #         [0, z, 0]
        #     ])
        #     coordinate = numpy.dot(projection_matrix, self.coordinates[i])
        
        #     x = int(coordinate[0]*self.scale + self.resolution[0]//2)
        #     y = int(coordinate[1]*self.scale + self.resolution[1]//2)
        #     connection.append((x, y))
            
        # pygame.draw.lines(screen, (155,115,99), False, connection)
        
        pass