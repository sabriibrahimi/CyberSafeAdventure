import pygame
import random
from constants import *

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(DARK_GRAY)
        pygame.draw.rect(self.image, GRAY, (0, 0, width, height), 2)
        for i in range(0, width, 20):
            pygame.draw.line(self.image, (50, 50, 50), (i, 0), (i, height), 1)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class MovingPlatform(Platform):
    def __init__(self, x, y, width, height, dist, axis='x', speed=2):
        super().__init__(x, y, width, height)
        self.start_pos = x if axis == 'x' else y
        self.dist = dist
        self.axis = axis
        self.speed = speed
        self.direction = 1
        
        # Distinct look for moving platforms (Yellowish border)
        pygame.draw.rect(self.image, YELLOW, (0, 0, width, height), 2)
    
    def update(self):
        if self.axis == 'x':
            self.rect.x += self.speed * self.direction
            if abs(self.rect.x - self.start_pos) > self.dist:
                self.direction *= -1
        else:
            self.rect.y += self.speed * self.direction
            if abs(self.rect.y - self.start_pos) > self.dist:
                self.direction *= -1

class QuestionBlock(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.width = 40
        self.height = 40
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        # Gold-ish block with question mark
        pygame.draw.rect(self.image, YELLOW, (0, 0, self.width, self.height))
        pygame.draw.rect(self.image, GRAY, (0, 0, self.width, self.height), 2)
        font = pygame.font.Font(None, 28)
        text_surf = font.render("?", True, BLACK)
        text_rect = text_surf.get_rect(center=(self.width//2, self.height//2))
        self.image.blit(text_surf, text_rect)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.active = False
        try:
            self.image.set_alpha(0)
        except Exception:
            pass

    def activate(self):
        self.active = True
        try:
            self.image.set_alpha(255)
        except Exception:
            pass

    def deactivate(self):
        self.active = False
        try:
            self.image.set_alpha(0)
        except Exception:
            pass

class Level:
    def __init__(self, level_num):
        self.level_num = level_num
        self.platforms = pygame.sprite.Group()
        self.create_level()
        
        self.messages = {
            1: "Level 1: Avoid suspicious links and viruses!",
            2: "Level 2: Don't share personal information with strangers!",
            3: "Level 3: Use strong passwords and keep them safe!",
            4: "Level 4: Be careful with downloads and attachments!",
            5: "Level 5: Final Challenge - Use all your knowledge!"
        }
        
    def create_level(self):
        self.platforms.add(Platform(0, SCREEN_HEIGHT - 50, SCREEN_WIDTH, 50))
        
        if self.level_num == 1:

            self.platforms.add(Platform(50, 600, 180, 20))
            self.platforms.add(Platform(350, 600, 180, 20))
            self.platforms.add(Platform(700, 600, 180, 20))
            
            self.platforms.add(Platform(200, 500, 160, 20))
            self.platforms.add(Platform(550, 500, 160, 20))
            
            self.platforms.add(Platform(50, 400, 140, 20))
            self.platforms.add(Platform(400, 350, 140, 20))
            self.platforms.add(Platform(750, 400, 140, 20))
            
        elif self.level_num == 2:

            self.platforms.add(Platform(50, 550, 150, 20))
            
            self.platforms.add(Platform(350, 400, 150, 20))
            
            self.platforms.add(Platform(650, 500, 150, 20))
            
            # Moving Bridge!
            self.platforms.add(MovingPlatform(220, 480, 80, 20, 100, 'x', 2)) 
            
            self.platforms.add(Platform(270, 620, 60, 20))
            self.platforms.add(Platform(530, 620, 60, 20))
            self.platforms.add(Platform(240, 320, 50, 20))
            self.platforms.add(Platform(530, 320, 50, 20))
            self.platforms.add(MovingPlatform(820, 350, 60, 20, 80, 'y', 1))
            
        elif self.level_num == 3:
            self.platforms.add(Platform(100, 600, 150, 20))
            self.platforms.add(Platform(300, 500, 150, 20))
            self.platforms.add(Platform(500, 400, 150, 20))
            self.platforms.add(Platform(700, 300, 150, 20))
            
            # Vertical movers
            self.platforms.add(MovingPlatform(900, 200, 80, 20, 100, 'y', 2))
            self.platforms.add(Platform(600, 150, 80, 20))
            self.platforms.add(Platform(300, 150, 80, 20))
            
            self.platforms.add(MovingPlatform(600, 600, 80, 20, 150, 'x', 3))
            self.platforms.add(Platform(900, 500, 80, 20))
            
        elif self.level_num == 4:

            self.platforms.add(Platform(50, 600, 140, 20))
            self.platforms.add(Platform(200, 500, 140, 20))
            
            self.platforms.add(MovingPlatform(350, 400, 120, 20, 100, 'x', 2))
            self.platforms.add(Platform(500, 350, 100, 20))
            self.platforms.add(MovingPlatform(650, 400, 120, 20, 100, 'x', 2))
            
            self.platforms.add(Platform(800, 500, 140, 20))
            self.platforms.add(Platform(950, 600, 140, 20))
            
            self.platforms.add(Platform(500, 200, 160, 20))
            self.platforms.add(Platform(100, 300, 100, 20))
            self.platforms.add(Platform(900, 300, 100, 20))

        else:
            # Level 5: The Maze - Final Challenge
            
            # --- TIER 1 & 2: DANGER ZONES (Enemies will be here) ---
            # Wide platforms for enemies to patrol
            self.platforms.add(Platform(50, 650, 300, 20))
            self.platforms.add(Platform(450, 650, 300, 20))
            self.platforms.add(Platform(850, 650, 300, 20))
            
            self.platforms.add(MovingPlatform(350, 500, 150, 20, 100, 'x', 2))
            self.platforms.add(MovingPlatform(700, 500, 150, 20, 100, 'x', 2))
            
            self.platforms.add(Platform(100, 350, 250, 20))
            self.platforms.add(Platform(850, 350, 250, 20))
            
            # --- TIER 3: SAFE ZONES (For Boxes) ---
            # Small, high platforms reachable by jumping, where boxes will be placed
            # Enemies won't spawn here.
            self.platforms.add(Platform(500, 250, 200, 20))  # Central safe hub
            
            self.platforms.add(Platform(50, 200, 100, 20))   # Top Left
            self.platforms.add(Platform(1050, 200, 100, 20)) # Top Right
            
            self.platforms.add(Platform(300, 150, 100, 20))  # High Left
            self.platforms.add(Platform(800, 150, 100, 20))  # High Right

            # Explicit Question Block Positions (Above the safe platforms)
            # We place them at specific coordinates so they align perfectly with the safe pads
            # Adjusted relative to platforms: Platform Y - 100 (reachable jump)
            self.question_block_positions = [
                (580, 150),  # Above Central hub (500, 250) (250-100=150)
                (90, 100),   # Above Top Left (50, 200) (200-100=100)
                (1090, 100), # Above Top Right (1050, 200) (200-100=100)
                (340, 50),   # Above High Left (300, 150) (150-100=50)
                (840, 50)    # Above High Right (800, 150) (150-100=50)
            ]
        
        # Apply deterministic variations per level so each level differs
        # slightly from the previous one (positions, widths, moving speeds).
        # Skip for Level 5 to preserve precise design.
        if self.level_num != 5:
            self.apply_variations()

    def apply_variations(self):
        """
        Make small, deterministic changes to platforms per level:
        - Slightly shift platform positions
        - Slightly vary widths (except the ground)
        - Increase moving platform speed with level number
        Uses a Random seeded by level_num for repeatable variations.
        """
        rand = random.Random(self.level_num)
        # Maximum horizontal shift grows a bit with level (but capped)
        max_shift_x = min(40, 8 * self.level_num)
        max_shift_y = min(25, 5 * self.level_num)

        for platform in list(self.platforms):
            # Save old to reapply after possible image resize
            old_x, old_y = platform.rect.x, platform.rect.y
            # Random small shifts
            shift_x = rand.randint(-max_shift_x, max_shift_x)
            shift_y = rand.randint(-max_shift_y, max_shift_y)
            new_x = max(0, min(old_x + shift_x, SCREEN_WIDTH - platform.rect.width))
            new_y = max(0, min(old_y + shift_y, SCREEN_HEIGHT - 100))

            platform.rect.x = new_x
            platform.rect.y = new_y

            # If it's a moving platform, slightly increase its speed based on level
            if isinstance(platform, MovingPlatform):
                platform.speed = max(0.5, platform.speed + (self.level_num * 0.15))

            # Don't resize the main ground platform
            if platform.rect.width < SCREEN_WIDTH - 10:
                # Slight width variation for more layout diversity
                delta_w = rand.randint(-20, 20)
                new_width = max(40, min(platform.rect.width + delta_w, SCREEN_WIDTH - platform.rect.x))
                if new_width != platform.rect.width:
                    height = platform.rect.height
                    # Recreate the image with the new width and redraw visuals
                    platform.image = pygame.Surface((new_width, height))
                    platform.image.fill(DARK_GRAY)
                    pygame.draw.rect(platform.image, GRAY, (0, 0, new_width, height), 2)
                    for i in range(0, new_width, 20):
                        pygame.draw.line(platform.image, (50, 50, 50), (i, 0), (i, height), 1)
                    if isinstance(platform, MovingPlatform):
                        pygame.draw.rect(platform.image, YELLOW, (0, 0, new_width, height), 2)
                    # Reset rect while preserving topleft
                    platform.rect = platform.image.get_rect()
                    platform.rect.x = new_x
                    platform.rect.y = new_y