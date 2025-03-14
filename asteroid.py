from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
            
        # Generate random split angle between 20 and 50 degrees
        random_angle = random.uniform(20, 50)
        
        # Calculate new radius for smaller asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        # Create rotated velocity vectors
        vel1 = self.velocity.rotate(random_angle)
        vel2 = self.velocity.rotate(-random_angle)
        
        # Create two new smaller asteroids
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = vel1 * 1.2
        
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = vel2 * 1.2
        
        