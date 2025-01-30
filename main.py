import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot
from random import uniform

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Shot.containers = (shots, updatable, drawable)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        updatable.update(dt)

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.detect_collision(shot):
                    asteroid.split()
                    shot.kill()

            if player.detect_collision(asteroid):
                print("Game Over")
                sys.exit()

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000.0

if __name__ == "__main__":
    main()
