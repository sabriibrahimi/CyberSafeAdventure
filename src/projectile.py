import pygame
from constants import *

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.width = 10
        self.height = 10
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        
        pygame.draw.circle(self.image, YELLOW, (self.width // 2, self.height // 2), 5)
        pygame.draw.circle(self.image, ORANGE, (self.width // 2, self.height // 2), 3)
        pygame.draw.circle(self.image, WHITE, (self.width // 2, self.height // 2), 1)
        
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        
        self.speed = 10
        self.direction = direction
        self.damage = 15
        
    def update(self):
        self.rect.x += self.speed * self.direction
        
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH:
            self.kill()
