import pygame
import random
from constants import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, enemy_type="virus", behavior="chase", speed=None):
        super().__init__()
        self.enemy_type = enemy_type
        self.behavior = behavior
        self.width = 35
        self.height = 35
        
        colors = {
            "virus": RED,           # Red Spikes
            "phishing": BLUE,       # Blue Spikes
            "stranger": PURPLE,     # Purple Spikes
            "malware": GREEN        # Green Spikes
        }
        
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        color = colors.get(enemy_type, RED)
        
        points = [
            (self.width // 2, 5),
            (5, self.height - 5),
            (self.width - 5, self.height - 5)
        ]
        pygame.draw.polygon(self.image, color, points)
        pygame.draw.polygon(self.image, WHITE, points, 2)
        pygame.draw.line(self.image, WHITE, (self.width // 2, 12), (self.width // 2, 20), 2)
        pygame.draw.circle(self.image, WHITE, (self.width // 2, 26), 2)
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.rect.y = y
        
        if speed is not None:
             self.speed = speed
        else:
             self.speed = random.uniform(1, 3)
        
        self.direction = random.choice([-1, 1])
        self.velocity_y = 0
        
        self.damage = 10
        try:
            self.damage = int(self.damage * DAMAGE_REDUCTION)
        except NameError:
            pass
        
    def update(self, platforms, player_pos=None):
        move_x = True
        
        if self.behavior == "chase" and player_pos:
            dx = player_pos[0] - self.rect.centerx
            distance = abs(dx)
            
            if distance < 10:
                move_x = False
            elif distance < 400:
                if dx > 0:
                    self.direction = 1
                elif dx < 0:
                    self.direction = -1
        
        if self.rect.left <= 0:
            self.rect.left = 0
            if self.behavior == "patrol": 
                self.direction = 1
        elif self.rect.right >= SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            if self.behavior == "patrol":
                self.direction = -1
        
        self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y
        
        on_ground = False
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.velocity_y > 0:  # Falling
                    self.rect.bottom = platform.rect.top
                    self.velocity_y = 0
                    on_ground = True
                    
                    if self.behavior == "patrol":
                        look_ahead_x = self.rect.right + 5 if self.direction > 0 else self.rect.left - 5
                        
                        if look_ahead_x > platform.rect.right or look_ahead_x < platform.rect.left:
                            self.direction *= -1
                            self.rect.x += self.speed * self.direction * 2

        if move_x:
            self.rect.x += self.speed * self.direction
