#My Firat PyGame, Tarita Brown, 11/29/21 

import pygame, sys 
from pygame.locals import *

# start Pygame
pygame.init()

# Setup our window.
windowSurface = pygame.display.set_mode((500,400), 0,32)
pygame.display.set_caption('Hello, world!')

# Setup Colors
BLACK = (0, 0, 0,)
WHITE = (255, 255, 255)
RED = (255, 0,0) 
GREEN = (0, 255, 0) 
BLUE = ( 0, 0, 255)

# Setup font.\
basicFront = pygame.font.SysFont(None,48)

# Set text.
text = basicFont.render('Hello, world!', True, WHITE, BLUE)
textRect = text.get_rect()
