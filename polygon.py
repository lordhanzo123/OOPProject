# MAKE BEAM AND COLUMN
# pymunk: physics for the polygon
import pymunk as pm
from pymunk import Vec2d

# pygame: create beams and columns
import pygame
import math


# Polygon: mean multiple shape and size
class Polygon():  # Polygon works to create a beam and frame column.
    def __init__(self, pos, length, height, space, mass=5.0):  # atributes of polygon

        # pos:               where the polygon is locate.
        # length, height:     size of polygon
        # space:             shape of the body of polygon
        # mass:              default mass.

        moment = 1000  # default moment
        body = pm.Body(mass, moment)  # "Body" class in pymunk
        body.position = Vec2d(pos)  # Vec2d defines gravity of the position

        shape = pm.Poly.create_box(body, (length, height))  # creat_box function, static method of pymunk
        shape.color = (0, 0, 255)  # BLUE color, RBG code
        shape.friction = 0.5
        shape.collision_type = 2

        space.add(body, shape)

        self.body = body
        self.shape = shape

        wood = pygame.image.load("./resources/images/wood.png").convert_alpha()
        wood2 = pygame.image.load("./resources/images/wood2.png").convert_alpha()

        rect = pygame.Rect(251, 357, 86, 22)  # extract the desired rec for using as a beam.
        # Ox, Oy: 251, 357
        # width, height: 86, 22
        self.beam_image = wood.subsurface(rect).copy()  # load the rect image.

        rect = pygame.Rect(16, 252, 22, 84)  # extract wood uses as columns
        self.column_image = wood2.subsurface(rect).copy()

    def to_pygame(self, p):  # to_pygame standard function,
        # P: body position create by pymunk module
        # *important* =>to delute a beam and comlum
        """Convert pymunk to pygame coordinates"""
        return int(p.x), int(-p.y + 600)  # return coordinate
        # p,x : X part and Y part
        # -p, y+ 600: others X part, Y part

    def draw_poly(self, element, screen):
        """Draw beams and columns"""
        poly = self.shape
        ps = poly.get_vertices()  # get vertices from pygame

        ps.append(ps[0])  # get the first position of the vertices above

        ps = map(self.to_pygame, ps)
        # call to_pygame function on all every elements of this ps
        # this ps contains a list of polygon vertices
        # convert "ps" => vector "p"
        # the position of the vertices
        """explain:
        import math
        listNumber = [1,2,3,4,5] 
        squareRoot = list(map(math.sqrt, listNumber))
        print(squareRoot)
        CONSOLE:
        [1, sqrt(2), sqrt(3), sqrt(4), sqrt(5)]
        """

        ps = list(ps)
        color = (255, 0, 0)  # RED color
        pygame.draw.lines(screen, color, False, ps)  # draw a line for the beams

        """Check either the polygon is a beam or a column"""
        if element == 'beams':
            p = poly.body.position #polygon body position
            p = Vec2d(self.to_pygame(p)) #convert pymunk to pygame

            angle_degrees = math.degrees(poly.body.angle) + 180 #rotate a beam as desire
            #for each rotation, it will shift by 180 degree

            rotated_logo_img = pygame.transform.rotate(self.beam_image,
                                                       angle_degrees)
            offset = Vec2d(rotated_logo_img.get_size()) / 2.
            #"offset" is vec2D contain 2 points
            """Number 2 is for rotate distance/displacement for the column and beam
            ==> Try changing to others number to show difference
            """

            p = p - offset #new position
            np = p


            """blit function"""
            screen.blit(rotated_logo_img, (np.x, np.y))
            #np.x, np.y: new position



        if element == 'columns':
            p = poly.body.position
            p = Vec2d(self.to_pygame(p))
            angle_degrees = math.degrees(poly.body.angle) + 180
            rotated_logo_img = pygame.transform.rotate(self.column_image,
                                                       angle_degrees)
            offset = Vec2d(rotated_logo_img.get_size()) / 2.
            p = p - offset
            np = p
            screen.blit(rotated_logo_img, (np.x, np.y))
