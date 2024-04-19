import pygame
from pygame.transform import scale
from config import *


class PlayerSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original = pygame.image.load("assets/ship.png")
        self.image = scale(self.original, (64, 64))
        self.rect = self.image.get_rect(center=PL_START_POS)
    
