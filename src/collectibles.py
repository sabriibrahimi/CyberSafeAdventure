import pygame
from constants import *


class Collectible(pygame.sprite.Sprite):
    def __init__(self, x, y, collectible_type="safety_tip"):
        super().__init__()
        self.collectible_type = collectible_type
        self.width = 30
        self.height = 30

        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        center_x, center_y = self.width // 2, self.height // 2
        pygame.draw.circle(self.image, YELLOW, (center_x, center_y), 12)
        pygame.draw.circle(self.image, WHITE, (center_x, center_y), 12, 2)
        pygame.draw.circle(self.image, WHITE, (center_x, center_y), 8, 1)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.animation_counter = 0

    def update(self):
        self.animation_counter += 0.1
        self.rect.y += int(0.5 * (1 if int(self.animation_counter) % 2 == 0 else -1))