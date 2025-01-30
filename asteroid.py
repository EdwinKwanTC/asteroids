import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
from random import uniform

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        return pygame.draw.circle(screen, 'white', self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = uniform(20, 50)

        angle_top = self.velocity.rotate(random_angle)
        angle_bottom = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_a.velocity.rotate(random_angle)

        asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_b.velocity.rotate(-random_angle)

        asteroid_a.velocity = angle_top * 1.2
        asteroid_b.velocity = angle_bottom * 1.2
