mport os
import sys
import math
import time
import pygame
current_path = os.getcwd()
import pymunk as pm
from characters import Bird
from level import Level


pygame.init() #intialize pygames
screen = pygame.display.set_mode((1200, 650))  #Set screen size

#import spirte and render background
#To make an image transparent you need an image with alpha values -> convert_alpha()

redbird = pygame.image.load(
    "../resources/images/red-bird3.png").convert_alpha()
background = pygame.image.load(
    "../resources/images/background1.png").convert_alpha()
sling_image = pygame.image.load(
    "../resources/images/sling-3.png").convert_alpha()
full_sprite = pygame.image.load(
    "../resources/images/full-sprite.png").convert_alpha()
rect = pygame.Rect(181, 1050, 50, 50)

cropped = full_sprite.subsurface(rect).copy() #crop the full sprite
pig_image = pygame.transform.scale(cropped, (30, 30)) #Take out the pig
buttons = pygame.image.load(
    "../resources/images/selected-buttons.png").convert_alpha()
pig_happy = pygame.image.load(
    "../resources/images/pig_failed.png").convert_alpha()
stars = pygame.image.load(
    "../resources/images/stars-edited.png").convert_alpha()

rect = pygame.Rect(0, 0, 200, 200)
star1 = stars.subsurface(rect).copy()
rect = pygame.Rect(204, 0, 200, 200)
star2 = stars.subsurface(rect).copy()
rect = pygame.Rect(426, 0, 200, 200)
star3 = stars.subsurface(rect).copy()
rect = pygame.Rect(164, 10, 60, 60)
pause_button = buttons.subsurface(rect).copy()
rect = pygame.Rect(24, 4, 100, 100)
replay_button = buttons.subsurface(rect).copy()
rect = pygame.Rect(142, 365, 130, 100)
next_button = buttons.subsurface(rect).copy()
clock = pygame.time.Clock()
rect = pygame.Rect(18, 212, 100, 100)
play_button = buttons.subsurface(rect).copy()
clock = pygame.time.Clock() #set the clock
running = True
# the base of the physics
space = pm.Space()   #Create the space
space.gravity = (0.0, -700.0)  #set gravity move down therefore y=-700
#Create empty list
pigs = []
birds = []
balls = []
polys = []
beams = []
columns = []
poly_points = []
ball_number = 0
polys_dict = {}
mouse_distance = 0 #drag from the mouse
rope_length = 90
angle = 0
x_mouse = 0 #x drag position of mouse
y_mouse = 0 #y drag position of mouse
count = 0 #to count bird
mouse_pressed = False
t1 = 0   #
tick_to_next_circle = 10  #transtion between each bird
#Set RGB
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
sling_x, sling_y = 135, 450  #position before stretch
sling2_x, sling2_y = 160, 450 #position after stretch
#Set attribute at the start of game
score = 0
game_state = 0
bird_path = []
counter = 0
restart_counter = False
bonus_score_once = True
#Set the font for the game
bold_font = pygame.font.SysFont("arial", 30, bold=True)
bold_font2 = pygame.font.SysFont("arial", 40, bold=True)
bold_font3 = pygame.font.SysFont("arial", 50, bold=True)
wall = False
