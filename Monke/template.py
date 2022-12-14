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

width = window.get_width()
height = window.get_height()

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
    rect_width = height
    rect_height = (height * 2/3)
    pygame.draw.rect(window, (255, 255, 255), 
    ((width - rect_width) / 2, (height - rect_height)/2, rect_width, rect_height))
    pygame.draw.circle(window, (255, 0, 0), (width / 2, height / 2), height * 2/9)
    text = font.render("Konnichi-wa!", True, (255, 255, 0))
    window.blit(text, (width - text.get_width()) / 2, (height - text.get_height()) / 2)
    

