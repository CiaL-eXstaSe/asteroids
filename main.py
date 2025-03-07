import pygame
# Because this is a smaller project, and we don't risk conflicting import names, 
# we're going to use a wildcard import for convenience. 
# In a larger project, you'd want to import only the constants you need
from constants import *
from player import Player
def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Create the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Create a clock object to control FPS
    clock = pygame.time.Clock()
    dt = 0  # Delta time between frames
    
    # Game loop
    running = True
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  # Create player outside the loop
    
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        player1.update(dt)  # Update player position before drawing
        player1.draw(screen)
        pygame.display.flip()
        
        # Control the frame rate
        dt = clock.tick(60) / 1000.0  # Convert milliseconds to seconds

if __name__ == "__main__":
    main()