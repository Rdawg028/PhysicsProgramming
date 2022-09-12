import pygame
from pygame.locals import *
import random
from pygame.math import Vector2, Vector3

# Constants
BG_COLOR = (0,0,0)

# Timing
FPS = 60
dt = 1/FPS
clock = pygame.time.Clock()

# Initialize
pygame.init()
pygame.font.init()
#print(pygame.font.get_fonts())



# Create window
window = pygame.display.set_mode(flags=FULLSCREEN)

width = window.get_width()
height = window.get_height()

RADIUS = 100
COLOR = Vector3(0, 255, 255)

coords = []
for i in range(10):
    coords.append(Vector2(RADIUS + random.randrange(width - 2 * RADIUS), 
                   RADIUS + random.randrange(height - 2 * RADIUS)))

# fontpath = pygame.font.match_font("baskervilleoldface")
font = pygame.font.SysFont("baskervilleoldface", round(width / 25))

# MAIN LOOP
running = True
clock.tick() # start the clock
while running:
    # Update the display
    pygame.display.update()
    # Delay to limit frame rate
    dt = clock.tick(FPS)/1000
    # Clear the graphics window
    window.fill(BG_COLOR)
    
    # EVENTS
    while event := pygame.event.poll():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False
    
    # DRAW
    mouse_pos = Vector2(pygame.mouse.get_pos())
    for center in coords:
        if (center - mouse_pos).magnitude() < RADIUS: #mouse is inside circle
            color = (255, 255, 0)
        else:
            color = COLOR
        pygame.draw.circle(window, color, center, RADIUS)
    

