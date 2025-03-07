import pygame
# Because this is a smaller project, and we don't risk conflicting import names, 
# we're going to use a wildcard import for convenience. 
# In a larger project, you'd want to import only the constants you need
from constants import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Create the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        pygame.display.flip()
    
    # Quit Pygame properly
    pygame.quit()

if __name__ == "__main__":
    main()