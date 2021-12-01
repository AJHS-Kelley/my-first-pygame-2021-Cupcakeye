#My Firat PyGame, Tarita Brown, 12/1/21 2:11 PM

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
textRect.centerx = windowSurface.get_rect().centerx
textRect.centerx = windowSurface.get_rect().centery

# Fill background color.
windowSurface.fill(BLUE)


# Draw a polygon onto the screen.
pygame.draw.polygon(windowSurface, GREEN, ((146,0), (291, 106), (236, 277), (56, 277), (0,106)))

# Draw lines on the screen.
pygame.draw.line(windowSurface, BLUE, (60,60), (120, 60), 4)
pygame.draw.line(windowSurface, WHITE, (75,60), (60, 75), 2)
pygame.draw.line(windowSurface, RED, (0,150), (150, 0), 1)

# Draw a circle.
pygame.draw.circle(windowSuface, BLACK, (300, 50), 20,0)

# Draw am ellipse.
pygame.draw.ellipse(windowSurface, RED, (300, 250, 40, 80), 1) 

# Draw the text rectangle.
pygame.draw.rect(windowSurface, RED, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

# Create Pixel Array
pixArray + pygame.pixelArray(windowSurface)
pixelArray[480][300] = BLUE
del pixelArray 