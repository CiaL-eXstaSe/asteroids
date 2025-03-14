import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot

def main():
    pygame.init()
    
    # Create the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Create a clock object to control FPS
    clock = pygame.time.Clock()
    dt = 0  # Delta time between frames
    
    # Game loop
    running = True

    # Create Groups
    updateables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # Setting Groups as containers for the asteroids
    Asteroid.containers = (asteroids, updateables, drawables)
    AsteroidField.containers = updateables
    asteroidField = AsteroidField()

    # Setting Groups as containers for the shots
    Shot.containers = (shots, updateables, drawables)

    # Setting Groups as containers for the player
    Player.containers = (updateables, drawables)
    
    # Create player AFTER setting up containers
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        
        updateables.update(dt)  # Update player position before drawing

        # Check for collisions between player and asteroids
        for asteroid in asteroids:
            if player1.check_collision(asteroid):
                print("Game Over!")
                running = False

            # Check for collisions between shots and asteroids
            for shot in shots:
                if asteroid.check_collision(shot):
                    shot.kill()
                    asteroid.split()

        for drawable in drawables:
            drawable.draw(screen)
            
        pygame.display.flip()
        
        # Control the frame rate
        dt = clock.tick(60) / 1000.0  # Convert milliseconds to seconds

if __name__ == "__main__":
    main()