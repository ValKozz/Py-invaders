import pygame

class Missile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/missile.png")
        self.rect = self.image.get_rect(center=(x, y))

    def move_self(self):
        self.rect.move_ip(0, -5)

