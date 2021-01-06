import pymunk as pm
from pymunk import Vec2d #Vector in 2 dimension


class Bird():
    def __init__(self, distance, angle, x, y, space):  #constructor
        self.life = 20
        mass = 5 #weight of bird
        radius = 12
        inertia = pm.moment_for_circle(mass, 0, radius, (0, 0)) #calculate inertia for the solid circle
        body = pm.Body(mass, inertia) #create rigid body
        body.position = x, y

        power = distance * 53 #set the power
        impulse = power * Vec2d(1, 0)  #set the impulse
        angle = -angle

        body.apply_impulse_at_local_point(impulse.rotated(angle)) #add this local impulse to body as if applied from  the body local point
        shape = pm.Circle(body, radius, (0, 0)) #use class circle from pymunk
        shape.elasticity = 0.95 #set for the sling
        shape.friction = 1
        '''There are 3 types of collision: Bird,Pigs,Woods'''
        shape.collision_type = 0
        space.add(body, shape)
        self.body = body
        self.shape = shape

#Similiarly for the pigs
class Pig():
    def __init__(self, x, y, space):
        self.life = 20
        mass = 5
        radius = 14
        inertia = pm.moment_for_circle(mass, 0, radius, (0, 0))
        body = pm.Body(mass, inertia)
        body.position = x, y
        shape = pm.Circle(body, radius, (0, 0))
        shape.elasticity = 0.95
        shape.friction = 1
        shape.collision_type = 1
        space.add(body, shape)
        self.body = body
        self.shape = shape
