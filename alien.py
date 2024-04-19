import pygame
from pygame.transform import scale


class AlienSprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.alive = True
        self.original = pygame.image.load(
            "assets/alien.png",
        )
        self.image = scale(self.original, (48, 48))
        self.rect = self.image.get_rect(center=(x, y))

        self.explosion_image = pygame.image.load('assets/missile.png')
        
