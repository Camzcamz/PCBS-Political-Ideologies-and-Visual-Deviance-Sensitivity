
import pygame
# Color codes from: https://www.htmlcsscolor.com/hex/00FF6D

## Define color parameters ##

Colors = {'Green Perfect 0':(0, 255, 0), 'Green Ambiguous 0': (0, 255, 176), 'Green Ambiguous 1': (195, 255, 0), 'Green Ambiguous 2': (218, 255, 0), 'Green Ambiguous 3': (0, 255, 109), 'Red Perfect 0':(255,0, 0), 'Red Ambiguous 0':(255,79, 0), 'Red Ambiguous 1':(255,70, 0), 'Red Ambiguous 2':(255,0, 68), 'Red Ambiguous 3':(255,0, 79), 'Blue Perfect 0':(0, 0, 255), 'Blue Ambiguous 0':(0, 255, 244), 'Blue Ambiguous 1':(0, 255, 199), 'Blue Ambiguous 2':(49, 0, 255), 'Blue Ambiguous 3':(82, 0, 255)}

## Define Screen parameters##
W, H = 600, 600

## Define Square parameters ##
width, height = 600, 600
left, top = (W-width)/2, (H-height)/2
SQUARE = pygame.Rect(left, top, width, height) #takes four parameters even if you want a square

# start
pygame.init()
screen = pygame.display.set_mode((W, H), pygame.DOUBLEBUF)
# no need her to define BG color or screen.fill( )

for c,v in Colors.items():
    print (c,v)
    pygame.draw.rect(screen, v, SQUARE)# v = color value of specific key
    pygame.image.save(screen, "Stimuli_Colors/%s.jpg" %c) # adds c instead of %s, a dictionary key for a specific v, value

pygame.display.flip() # allows for update of contents of the entire display
