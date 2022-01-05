# Simple Animation with PyGame, Tarita Brown, 1/05/22, 2:45PM, v0.3

import pygame, sys, time 
from pygame.locals import *

# Setup PyGame
pygame.init()

# Setup the Window 
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Animation Example!')

# Setup the direction variables.
DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'

MOVESPEED = 4 


# Setup color values.
WHITE = (255, 255, 255)
RED = (255,0, 0)
GREEN = (0,225,0)
BLUE = (0, 0, 255) 