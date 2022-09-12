import pygame
from pygame.locals import *

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
    

