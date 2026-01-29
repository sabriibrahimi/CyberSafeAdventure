import pygame
import random
import math
from constants import *

class Boss(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.width = 80
        self.height = 80
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        

        pygame.draw.circle(self.image, RED, (self.width // 2, self.height // 2), 35)
        pygame.draw.circle(self.image, WHITE, (self.width // 2, self.height // 2), 35, 3)
        

        pygame.draw.circle(self.image, BLACK, (self.width // 2 - 12, self.height // 2 - 5), 8)
        pygame.draw.circle(self.image, BLACK, (self.width // 2 + 12, self.height // 2 - 5), 8)
        

        pygame.draw.arc(self.image, BLACK, (self.width // 2 - 15, self.height // 2, 30, 20), 0, 3.14, 3)
        

        import math
        for i in range(8):
            angle = (i * math.pi * 2) / 8
            x1 = self.width // 2 + int(30 * math.cos(angle))
            y1 = self.height // 2 + int(30 * math.sin(angle))
            x2 = self.width // 2 + int(40 * math.cos(angle))
            y2 = self.height // 2 + int(40 * math.sin(angle))
            pygame.draw.line(self.image, YELLOW, (x1, y1), (x2, y2), 3)
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # Boss stats
        self.health = 100
        self.max_health = 100
        self.speed = 1.2
        self.direction = random.choice([-1, 1])
        self.velocity_y = 0
        self.damage = 20
        try:
            self.damage = int(self.damage * DAMAGE_REDUCTION)
        except NameError:
            pass
        self.animation_counter = 0
        
    def update(self, platforms, player_pos=None):
        self.animation_counter += 0.1
        

        if player_pos:
            dx = player_pos[0] - self.rect.centerx
            dy = player_pos[1] - self.rect.centery
            
            if abs(dx) > 5:
                self.rect.x += self.speed if dx > 0 else -self.speed
            if abs(dy) > 5:
                self.rect.y += self.speed if dy > 0 else -self.speed
        else:
            self.rect.x += self.speed * self.direction
        

        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.direction *= -1


        
        for platform in platforms:

             pass
    
    def take_damage(self, amount):
        prev = self.health
        self.health -= amount
        if self.health < 0:
            self.health = 0
        if prev - self.health >= (self.max_health / 3):
            self.speed += 0.5
    
    def is_defeated(self):
        return self.health <= 0
