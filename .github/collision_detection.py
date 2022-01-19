# Pygame Collision Detcction Practice, Tarita Brown, Jan 19, 2022, 2:10PM, v0.5

import pygame, sys, random
from pygame.locals import *

# Setup Pygame
pygame.init()
mainClock = pygame.time.Clock()

# Setup the PyGame Window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT),0,32)
pygame.display.set_caption('Collision Detection 2022')

# setup colors.
BLACK = (0, 0, 0)
GREEN = (0, 225, 0)
WHITE = (225, 255, 255)

# Setup the player and food date structures.
foodCounter = 0
NEWFOOD = 40
FOODSIZE = 20
player = pygame.Rect(300, 100, 50, 50)
foods = []

for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))

# Movement Variables
moveLeft = False
moveRight = False
moveUp = False
moveDown = False 

MOVESPEED = 6