# Simple Animation with PyGame, Tarita Brown, 1/11/22, 2:42PM, v0.6

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

# Setup the box data.
b1 = {'rect':pygame.Rect(300, 80, 50, 100), 'color':RED, 'dir':UPRIGHT}
b2 = {'rect':pygame.Rect(200,200,20,20), 'color':GREEN, 'dir':UPLEFT}
b3 = {'rect':pygame.Rect(100, 150, 60, 60), 'color':BLUE, 'dir':DOWNLEFT}
boxes = [b1, b2, b3] 

# Run the game loop.
while True:
    # Check for QUIT event.
    for event in pygame.event.get():
       if event.type == QUIT:
        pygame.quit()
        sys.exit()

       windowSurface.fill(WHITE)  

    for b in boxes: 
          # Move the box data strucure.
          if b['dir'] == DOWNLEFT:
              b['rect'].left -= MOVESPEED
              b['rect'].top += MOVESPEED
          if b['dir'] == DOWNRIGHT :
              b['rect'].left += MOVESPEED
              b['rect'].top += MOVESPEED
          if b['dir'] == UPLEFT:
              b['rect'].left -= MOVESPEED
              b['rect'].top -= MOVESPEED
          if b['dir'] == UPRIGHT: 
              b['rect'].left += MOVESPEED
              b['rect'].top -= MOVESPEED 

          if b['rect'].top < 0:
              # The box has moved past the top. 
              if b['dir'] == UPLEFT:
                  b['dir'] = DOWNLEFT
              if   


