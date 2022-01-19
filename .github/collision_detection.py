# Pygame Collision Detcction Practice, Tarita Brown, Jan 19, 2022, 1:58PM, v0.3

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

