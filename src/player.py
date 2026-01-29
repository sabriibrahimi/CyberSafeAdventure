import pygame
from constants import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.width = 40
        self.height = 50
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        pygame.draw.circle(self.image, BLUE, (self.width // 2, 12), 10)
        pygame.draw.rect(self.image, BLUE, (self.width // 2 - 8, 20, 16, 25))
        pygame.draw.circle(self.image, WHITE, (self.width // 2 - 4, 10), 2)
        pygame.draw.circle(self.image, WHITE, (self.width // 2 + 4, 10), 2)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.velocity_x = 0
        self.velocity_y = 0
        self.on_ground = False
        self.jump_buffer = 0
        self.facing_left = False
        
        self.health = 100
        self.max_health = 100
        self.invincible = False
        self.invincible_timer = 0
        
    def update(self, platforms):
        if self.jump_buffer > 0:
            self.jump_buffer -= 1
        
        if self.invincible_timer > 0:
            self.invincible_timer -= 1
            if self.invincible_timer == 0:
                self.invincible = False
        
        if not self.on_ground:
            self.velocity_y += GRAVITY
        
        self.rect.x += self.velocity_x
        
        self.check_platform_collisions(platforms, horizontal=True)
        
        self.rect.y += self.velocity_y
        was_on_ground = self.on_ground
        self.on_ground = False
        
        self.check_platform_collisions(platforms, horizontal=False)
        
        self.check_ground(platforms)
        
        if was_on_ground and not self.on_ground and self.velocity_y >= 0:
            self.jump_buffer = 5  # 5 frames of jump buffer
        
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.on_ground = True
            self.velocity_y = 0
    
    def check_platform_collisions(self, platforms, horizontal):
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if horizontal:
                    if self.velocity_x > 0:  # Moving right
                        self.rect.right = platform.rect.left
                    elif self.velocity_x < 0:  # Moving left
                        self.rect.left = platform.rect.right
                else:
                    if self.velocity_y > 0:  # Falling
                        self.rect.bottom = platform.rect.top
                        self.on_ground = True
                        self.velocity_y = 0
                        # Move with platform if it's moving
                        if hasattr(platform, 'direction'): # Check if it's a moving platform
                             if platform.axis == 'x':
                                 self.rect.x += platform.speed * platform.direction
                             elif platform.axis == 'y':
                                 self.rect.y += platform.speed * platform.direction
                                 
                    elif self.velocity_y < 0:  # Jumping
                        self.rect.top = platform.rect.bottom
                        self.velocity_y = 0
    
    def check_ground(self, platforms):
        ground_check = pygame.Rect(self.rect.left, self.rect.bottom, self.rect.width, GROUND_TOLERANCE)
        for platform in platforms:
            if ground_check.colliderect(platform.rect):
                if abs(self.rect.bottom - platform.rect.top) <= GROUND_TOLERANCE:
                    self.on_ground = True
                    if self.velocity_y > 0:
                        self.velocity_y = 0
                    break
    
    def jump(self):
        if self.on_ground or self.jump_buffer > 0:
            self.velocity_y = PLAYER_JUMP_STRENGTH
            self.on_ground = False
            self.jump_buffer = 0
    
    def move_left(self):
        self.velocity_x = -PLAYER_SPEED
        self.facing_left = True
    
    def move_right(self):
        self.velocity_x = PLAYER_SPEED
        self.facing_left = False
    
    def stop(self):
        self.velocity_x = 0
    
    def take_damage(self, amount):
        if not self.invincible:
            self.health -= amount
            if self.health < 0:
                self.health = 0
            self.invincible = True
            self.invincible_timer = 60
    
    def heal(self, amount):
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health
