import pygame
import random
import sys
from constants import *
from player import Player
from enemies import Enemy
from collectibles import Collectible
from levels import Level, QuestionBlock
from ui import UI
from boss import Boss
from projectile import Projectile
from questions import TRIVIA_QUESTIONS

class CyberSafeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption("Cyber Safe Adventure")
        self.clock = pygame.time.Clock()
        
        self.running = True
        self.game_over = False
        self.won = False
        
        self.in_menu = True
        self.in_tips = False
        self.menu_buttons = {}
        
        self.current_level = 1

        self.max_levels = 5
        self.score = 0
        self.safety_tips_collected = 0
        self.coins_for_heal = 0
        
        self.enemy_spawn_timer = 0
        self.enemy_spawn_interval = 180
        self.boss = None
        self.boss_spawned = False
        self.warning_timer = 0
        self.warning_text = ""
        
        self.introduced_enemies = set()
        self.current_enemy_warning = None
        self.enemy_warning_timer = 0
        
        self.boss_warning_active = False
        self.boss_warning_timer = 0
        
        self.trivia_active = False
        self.current_question = None
        self.selected_option = 0
        self.question_blocks = pygame.sprite.Group()
        self.active_question_block = None
        self.block_respawn_timer = 0
        self.block_respawn_delay = 0
        self.question_sequence_active = False
        self.question_sequence = []
        self.question_sequence_index = 0
        self.question_sequence_correct = 0

        self.level_intro_active = False
        
        self.game_paused = False
        
        self.in_password_challenge = False
        self.password_input = ""
        self.password_feedback = ""
        self.password_strength = ""
        
        self.collided_enemy_type = None
        self.enemy_info_active = False
        self.floating_texts = []
        
        self.in_email_sorting = False
        self.email_list = []
        self.current_email_index = 0
        self.emails_sorted_correctly = 0
        self.email_feedback = ""
        self.email_feedback_timer = 0
        
        self.ui = UI()
        
        self.init_level()
        
    def init_level(self):
        self.level = Level(self.current_level)
        
        current_health = 100
        if hasattr(self, 'player'):
            current_health = self.player.health
            
        self.player = Player(50, SCREEN_HEIGHT - 150)
        
        if self.current_level > 1:
            self.player.health = current_health
            
        self.player.invincible = True
        self.player.invincible_timer = 180
        self.all_sprites = pygame.sprite.Group(self.player)
        
        self.current_enemy_warning = None
        self.enemy_warning_timer = 0
        
        self.enemies = pygame.sprite.Group()
        self.spawn_enemies()
        
        self.collectibles = pygame.sprite.Group()
        self.spawn_collectibles()
        
        self.projectiles = pygame.sprite.Group()
        self.has_weapon = False
        
        self.level_intro_active = False
        self.game_paused = False
        
        self.boss = None
        self.boss_spawned = False
        if self.current_level == 5:
            self.boss_warning_active = False
            self.boss_warning_timer = 0
        
        self.enemy_spawn_timer = 0
        
        self.all_sprites.add(self.enemies)
        self.all_sprites.add(self.collectibles)
        self.all_sprites.add(self.projectiles)

        self.all_sprites.add(self.question_blocks)
        
        if self.current_level == 5:
            self.question_blocks.empty()
            
            if hasattr(self.level, 'question_block_positions') and self.level.question_block_positions:
                for pos in self.level.question_block_positions:
                    qb = QuestionBlock(pos[0], pos[1])
                    self.question_blocks.add(qb)
                    self.all_sprites.add(qb)
            else:
                platform_candidates = []
                for plat in self.level.platforms:
                    if plat.rect.width < 60: continue
                    if plat.rect.top < SCREEN_HEIGHT - 120:
                        platform_candidates.append(plat)

                chosen = random.sample(platform_candidates, min(len(platform_candidates), 8)) if platform_candidates else []
                for plat in chosen:
                    qb_x = plat.rect.centerx - 20
                    qb_y = plat.rect.top - 120 
                    qb = QuestionBlock(qb_x, qb_y)
                    self.question_blocks.add(qb)
                    self.all_sprites.add(qb)

            if len(self.question_blocks) > 0:
                active = random.choice(self.question_blocks.sprites())
                active.activate()
                self.active_question_block = active
                self.block_respawn_timer = 0
                self.block_respawn_delay = random.randint(120, 240)

            if not self.boss_spawned:
                self.boss = Boss(SCREEN_WIDTH // 2, 100)
                self.boss_spawned = True
                self.all_sprites.add(self.boss)
        
        
    def spawn_enemies(self):
        enemies_to_introduce = []
        
        SPEED_SLOW = 1.0
        SPEED_NORMAL = 1.5
        SPEED_FAST_L4 = 2.0
        SPEED_FAST_L5 = 2.2

        if self.current_level == 1:

            self.enemies.add(Enemy(220, 465, "virus", behavior="patrol", speed=SPEED_SLOW))
            self.enemies.add(Enemy(590, 465, "virus", behavior="patrol", speed=SPEED_SLOW))
            
            # Ground (3)
            self.enemies.add(Enemy(350, SCREEN_HEIGHT - 90, "virus", behavior="chase", speed=SPEED_NORMAL))
            self.enemies.add(Enemy(600, SCREEN_HEIGHT - 90, "virus", behavior="chase", speed=SPEED_NORMAL))
            self.enemies.add(Enemy(900, SCREEN_HEIGHT - 90, "virus", behavior="chase", speed=SPEED_NORMAL))
            
        elif self.current_level == 2:

            self.enemies.add(Enemy(125, 515, "virus", behavior="patrol", speed=SPEED_SLOW))
            self.enemies.add(Enemy(425, 365, "phishing", behavior="patrol", speed=SPEED_SLOW))
            self.enemies.add(Enemy(725, 465, "malware", behavior="patrol", speed=SPEED_SLOW))
            
            # Ground (4)
            self.enemies.add(Enemy(200, SCREEN_HEIGHT - 90, "stranger", behavior="chase", speed=SPEED_NORMAL))
            self.enemies.add(Enemy(400, SCREEN_HEIGHT - 90, "phishing", behavior="chase", speed=SPEED_NORMAL))
            self.enemies.add(Enemy(600, SCREEN_HEIGHT - 90, "virus", behavior="chase", speed=SPEED_NORMAL))
            self.enemies.add(Enemy(800, SCREEN_HEIGHT - 90, "stranger", behavior="chase", speed=SPEED_NORMAL))

        elif self.current_level == 3:

            self.enemies.add(Enemy(150, 565, "stranger", behavior="patrol", speed=SPEED_SLOW))
            self.enemies.add(Enemy(350, 465, "stranger", behavior="patrol", speed=SPEED_SLOW))
            self.enemies.add(Enemy(550, 365, "stranger", behavior="patrol", speed=SPEED_SLOW))
            self.enemies.add(Enemy(750, 265, "stranger", behavior="patrol", speed=SPEED_SLOW))
            
            self.enemies.add(Enemy(300, SCREEN_HEIGHT - 90, "virus", behavior="chase", speed=SPEED_NORMAL))
            self.enemies.add(Enemy(500, SCREEN_HEIGHT - 90, "virus", behavior="chase", speed=SPEED_NORMAL))
            self.enemies.add(Enemy(700, SCREEN_HEIGHT - 90, "virus", behavior="chase", speed=SPEED_NORMAL))
            self.enemies.add(Enemy(900, SCREEN_HEIGHT - 90, "virus", behavior="chase", speed=SPEED_NORMAL))
            
        elif self.current_level == 4:
            self.enemies.add(Enemy(100, 565, "malware", behavior="patrol", speed=SPEED_FAST_L4))
            self.enemies.add(Enemy(250, 465, "malware", behavior="patrol", speed=SPEED_FAST_L4))
            self.enemies.add(Enemy(690, 365, "malware", behavior="patrol", speed=SPEED_FAST_L4))
            self.enemies.add(Enemy(850, 465, "malware", behavior="patrol", speed=SPEED_FAST_L4))
            self.enemies.add(Enemy(980, 565, "malware", behavior="patrol", speed=SPEED_FAST_L4))
            
            self.enemies.add(Enemy(200, SCREEN_HEIGHT - 90, "malware", behavior="chase", speed=SPEED_FAST_L4))
            self.enemies.add(Enemy(400, SCREEN_HEIGHT - 90, "malware", behavior="chase", speed=SPEED_FAST_L4))
            self.enemies.add(Enemy(600, SCREEN_HEIGHT - 90, "malware", behavior="chase", speed=SPEED_FAST_L4))
            self.enemies.add(Enemy(800, SCREEN_HEIGHT - 90, "malware", behavior="chase", speed=SPEED_FAST_L4))
            
        elif self.current_level == 5:
            self.enemies.add(Enemy(100, 615, "malware", behavior="patrol", speed=SPEED_FAST_L5))
            self.enemies.add(Enemy(600, 615, "malware", behavior="patrol", speed=SPEED_FAST_L5))
            self.enemies.add(Enemy(1000, 615, "malware", behavior="patrol", speed=SPEED_FAST_L5))
            
            self.enemies.add(Enemy(200, 315, "malware", behavior="patrol", speed=SPEED_FAST_L5))
            self.enemies.add(Enemy(950, 315, "malware", behavior="patrol", speed=SPEED_FAST_L5))
            
            self.enemies.add(Enemy(200, SCREEN_HEIGHT - 90, "malware", behavior="chase", speed=SPEED_FAST_L5))
            self.enemies.add(Enemy(550, SCREEN_HEIGHT - 90, "malware", behavior="chase", speed=SPEED_FAST_L5))
            self.enemies.add(Enemy(900, SCREEN_HEIGHT - 90, "malware", behavior="chase", speed=SPEED_FAST_L5))
            
        else:

            num_enemies = 3 + self.current_level * 2
            enemy_types = ["virus", "phishing", "stranger", "malware"]
            
            enemies_to_introduce = []
            
            for _ in range(num_enemies):
                x = random.randint(350, SCREEN_WIDTH - 100)
                y = random.randint(100, SCREEN_HEIGHT - 200)
                enemy_type = random.choice(enemy_types)
                enemy = Enemy(x, y, enemy_type)
                self.enemies.add(enemy)
                
                if enemy_type not in self.introduced_enemies:
                    if enemy_type not in enemies_to_introduce:
                        enemies_to_introduce.append(enemy_type)
        

        level_enemy_map = {
            1: "virus",
            2: "phishing", 
            3: "stranger",
            4: "malware"
        }
        
        enemy_to_introduce = None
        if self.current_level in level_enemy_map:
            enemy_to_introduce = level_enemy_map[self.current_level]
            if enemy_to_introduce not in self.introduced_enemies:
                self.introduced_enemies.add(enemy_to_introduce)

        elif enemies_to_introduce:
            first_new_enemy = enemies_to_introduce[0]
            self.introduced_enemies.add(first_new_enemy)

    
    def shoot(self):
        direction = 1
        if hasattr(self.player, 'facing_left') and self.player.facing_left:
            direction = -1
        
        projectile = Projectile(
            self.player.rect.centerx,
            self.player.rect.centery,
            direction
        )
        self.projectiles.add(projectile)
        self.all_sprites.add(projectile)
    
    def spawn_collectibles(self):

        num_collectibles = 8 + self.current_level * 2
        
        if self.current_level == 1:
            for platform in self.level.platforms:
                if platform.rect.width < SCREEN_WIDTH:
                     if random.random() < 0.7:
                        x = platform.rect.centerx
                        y = platform.rect.top - 30
                        self.collectibles.add(Collectible(x, y))

        attempts = 0
        max_attempts = num_collectibles * 20
        
        player_start_x = self.player.rect.centerx
        player_start_y = self.player.rect.centery
        
        while len(self.collectibles) < num_collectibles and attempts < max_attempts:
            attempts += 1
            x = random.randint(50, SCREEN_WIDTH - 50)
            y = random.randint(100, SCREEN_HEIGHT - 200)
            
            distance_from_start = ((x - player_start_x)**2 + (y - player_start_y)**2)**0.5
            if distance_from_start < 150:
                continue
            
            on_platform = False
            for platform in self.level.platforms:
                if (platform.rect.left <= x <= platform.rect.right and 
                    abs(y - platform.rect.top) < 40):
                    y = platform.rect.top - 30
                    on_platform = True
                    break
            
            if y >= SCREEN_HEIGHT - 100 and distance_from_start > 200:
                on_platform = True
                y = SCREEN_HEIGHT - 80
                y = SCREEN_HEIGHT - 80
            
            if on_platform:
                collectible = Collectible(x, y)
                self.collectibles.add(collectible)
    
    
    def handle_events(self):
        for event in pygame.event.get():
            if self.in_password_challenge:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if self.password_strength == "STRONG":
                            # Proceed to Level 2
                            self.in_password_challenge = False
                            self.current_level = 2
                            self.score += 100
                            self.init_level()
                    elif event.key == pygame.K_BACKSPACE:
                        self.password_input = self.password_input[:-1]
                    else:
                        if len(self.password_input) < 20:
                            if event.unicode.isprintable():
                                self.password_input += event.unicode
                    
                    self.check_password_strength()
                continue

            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.VIDEORESIZE:
                width = max(event.w, 800)
                height = max(event.h, 600)
                self.screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    
                    if self.in_menu:
                        if 'start' in self.menu_buttons and self.menu_buttons['start'].collidepoint(mouse_pos):
                            self.in_menu = False
                            self.init_level()
                        elif 'tips' in self.menu_buttons and self.menu_buttons['tips'].collidepoint(mouse_pos):
                            self.in_menu = False
                            self.in_tips = True
                            
                            self.in_tips = False
                            self.in_menu = True

                            self.check_password_strength()
                continue
            
            if self.in_email_sorting:
                if event.type == pygame.KEYDOWN:
                    if self.email_feedback_timer > 0:
                        pass
                    else:
                        current_email = self.email_list[self.current_email_index]
                        is_phishing = current_email['is_phishing']
                        correct = False
                        
                        if event.key == pygame.K_LEFT:
                            if is_phishing: correct = True
                        elif event.key == pygame.K_RIGHT:
                            if not is_phishing: correct = True
                        
                        if correct:
                            self.emails_sorted_correctly += 1
                            self.email_feedback = "CORRECT!"
                            self.spawn_floating_text("CORRECT!", SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 50, GREEN)
                        else:
                            self.email_feedback = "WRONG!"
                            self.spawn_floating_text("WRONG!", SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 50, RED)
                            self.score -= 50
                        
                        self.email_feedback_timer = 30
                        self.current_email_index += 1
                        
                        if self.current_email_index >= len(self.email_list):
                            pygame.time.delay(500)
                            self.in_email_sorting = False
                            self.current_level = 5
                            self.init_level()
                continue

            if self.trivia_active:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected_option = (self.selected_option - 1) % 3
                    elif event.key == pygame.K_DOWN:
                        self.selected_option = (self.selected_option + 1) % 3
                    elif event.key == pygame.K_RETURN:
                        if self.question_sequence_active:
                            if self.selected_option == self.current_question["correct"]:
                                self.question_sequence_correct += 1
                            self.question_sequence_index += 1
                            if self.question_sequence_index < len(self.question_sequence):
                                self.current_question = self.question_sequence[self.question_sequence_index]
                                self.selected_option = 0
                            else:
                              
                                self.trivia_active = False
                                self.game_paused = False
                                self.question_sequence_active = False
                                correct = self.question_sequence_correct
                               
                                if correct == 3:
                                    if self.boss and self.boss_spawned:
                                        self.boss.take_damage(34)
                                    self.player.heal(15)
                                    self.spawn_floating_text("+15 HP", self.player.rect.centerx, self.player.rect.top - 20, GREEN)
                              
                                if correct <= 1:
                                   
                                    try:
                                        self.player.take_damage(5)
                                        self.spawn_floating_text("-5 HP", self.player.rect.centerx, self.player.rect.top - 20, RED)
                                    except Exception:
                                        pass
                                self.active_question_block = None
                                self.block_respawn_timer = random.randint(120, 240)
                                self.block_respawn_delay = random.randint(120, 240)
                        else:
                            if self.selected_option == self.current_question["correct"]:
                                self.trivia_active = False
                                self.game_paused = False
                                self.player.invincible = True
                                self.player.invincible_timer = 120 # 2 seconds
                            else:

                                self.trivia_active = False
                                self.game_paused = False
                                damage_amount = 15
                                self.player.take_damage(damage_amount)
                                self.spawn_floating_text(f"-{damage_amount} HP", self.player.rect.centerx, self.player.rect.top - 20, RED)
                                self.player.invincible = True
                                self.player.invincible_timer = 120
                                if self.player.health <= 0:
                                    self.game_over = True
                                    self.won = False
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.in_tips:
                        self.in_tips = False
                        self.in_menu = True
                    elif not self.in_menu:
                        self.running = False
                    else:
                        self.running = False
                
                if self.in_menu or self.in_tips:
                    return

                if self.enemy_info_active:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                        self.enemy_info_active = False
                        self.trivia_active = True
                        self.current_question = random.choice(TRIVIA_QUESTIONS)
                        self.selected_option = 0
                    return

                if event.key == pygame.K_SPACE:
                    if self.level_intro_active:
                        self.level_intro_active = False
                        if self.current_enemy_warning:
                            self.game_paused = True
                        elif self.current_level == 5:
                            self.boss_warning_active = True
                            self.boss_warning_timer = 480
                            self.game_paused = True
                        else:
                            self.game_paused = False
                    elif self.current_enemy_warning:
                        self.current_enemy_warning = None
                        self.enemy_warning_timer = 0
                        self.game_paused = False
                    elif self.boss_warning_active:
                        if not self.boss_spawned and self.current_level == 5:
                            self.boss = Boss(SCREEN_WIDTH // 2, 100)
                            self.boss_spawned = True
                            self.all_sprites.add(self.boss)
                        self.boss_warning_active = False
                        self.boss_warning_timer = 0
                        self.game_paused = False
                    elif not self.game_over and not self.game_paused:
                        self.player.jump()
                
                if (event.key == pygame.K_x or event.key == pygame.K_z) and not self.game_over and not self.game_paused:
                    if self.has_weapon:
                        self.shoot()
                
                if event.key == pygame.K_r and self.game_over:
                    self.restart_game()
    
    def handle_input(self):
        if not self.game_over and not self.game_paused and not self.trivia_active:
            keys = pygame.key.get_pressed()
            
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.player.move_left()
            elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.player.move_right()
            else:
                self.player.stop()
        elif not self.game_over and (self.game_paused or self.trivia_active):
            self.player.stop()
    
    def update(self):
        if self.email_feedback_timer > 0:
            self.email_feedback_timer -= 1
            if self.email_feedback_timer == 0:
                self.email_feedback = ""
                
        if self.in_menu or self.in_tips or self.in_password_challenge or self.enemy_info_active or self.in_email_sorting:
            return

        if not self.game_over:
            self.update_floating_texts()

            if self.trivia_active:
                return

            if not self.game_paused:
                self.level.platforms.update()
                self.player.update(self.level.platforms)
            
                if self.current_level == 5:
                    if self.active_question_block is None:
                        if self.block_respawn_timer > 0:
                            self.block_respawn_timer -= 1
                        elif self.block_respawn_timer == 0:
                            inactive_blocks = [b for b in self.question_blocks if not b.active]
                            if inactive_blocks:
                                nb = random.choice(inactive_blocks)
                                nb.activate()
                                self.active_question_block = nb
                    if not self.question_sequence_active:
                        hit_blocks = pygame.sprite.spritecollide(self.player, self.question_blocks, False)
                        for block in hit_blocks:
                            if block.active:
                                is_below = self.player.rect.top > block.rect.top
                                is_moving_up = getattr(self.player, "velocity_y", 0) <= 2
                                
                                if is_below and is_moving_up:
                                    block.deactivate()
                                    self.active_question_block = None
                                    self.question_sequence_active = True
                                    self.question_sequence = random.sample(TRIVIA_QUESTIONS, min(3, len(TRIVIA_QUESTIONS)))
                                    self.question_sequence_index = 0
                                    self.question_sequence_correct = 0
                                    self.current_question = self.question_sequence[0]
                                    self.selected_option = 0
                                    self.trivia_active = True
                                    self.game_paused = True
                                    self.block_respawn_delay = random.randint(120, 240)
                                    break
            
            # self.enemy_spawn_timer += 1
            # if self.enemy_spawn_timer >= self.enemy_spawn_interval and not self.game_paused:
            #     self.enemy_spawn_timer = 0
            #     side = random.choice(['left', 'right'])
            #     x = -50 if side == 'left' else SCREEN_WIDTH + 50
            #     y = random.randint(100, SCREEN_HEIGHT - 200)
            #     enemy_type = random.choice(["virus", "phishing", "stranger", "malware"])
            #     enemy = Enemy(x, y, enemy_type)
            #     self.enemies.add(enemy)
            #     self.all_sprites.add(enemy)
                
            #     if enemy_type not in self.introduced_enemies:
            #         self.introduced_enemies.add(enemy_type)
                

            if self.boss_warning_timer > 0:
                self.boss_warning_timer -= 1
                if self.boss_warning_timer == 240 and not self.boss_spawned and self.current_level == 5:
                    self.boss = Boss(SCREEN_WIDTH // 2, 100)
                    self.boss_spawned = True
                    self.all_sprites.add(self.boss)
                if self.boss_warning_timer == 0:
                    self.boss_warning_active = False
                    self.game_paused = False
            

            if not self.game_paused:
                for enemy in self.enemies:
                    enemy.update(self.level.platforms, (self.player.rect.centerx, self.player.rect.centery))
                    if enemy.rect.right < -100 or enemy.rect.left > SCREEN_WIDTH + 100:
                        enemy.kill()
                
                if self.boss and self.boss_spawned:
                    self.boss.update(self.level.platforms, (self.player.rect.centerx, self.player.rect.centery))
                
                self.collectibles.update()
                
                self.projectiles.update()
            
            if not self.game_paused and self.boss and self.boss_spawned:
                boss_hits = pygame.sprite.spritecollide(self.boss, self.projectiles, True)
                for projectile in boss_hits:
                    self.boss.take_damage(projectile.damage)
                    if self.boss.is_defeated():
                        pass
            
            if not self.game_paused and not self.player.invincible:
                enemy_hits = pygame.sprite.spritecollide(self.player, self.enemies, False)
                if enemy_hits:
                    hit_enemy = enemy_hits[0]
                    self.collided_enemy_type = hit_enemy.enemy_type
                    
                    if self.current_level == 2:
                        self.enemy_info_active = True
                        self.game_paused = True
                    else:
                        self.trivia_active = True
                        self.current_question = random.choice(TRIVIA_QUESTIONS)
                        self.selected_option = 0
                        self.game_paused = True
                
                if self.boss and self.boss_spawned and self.player.rect.colliderect(self.boss.rect):

                    self.player.take_damage(self.boss.damage)
                    if self.player.health <= 0:
                        self.game_over = True
                        self.won = False
            
            if not self.game_paused:
                collectible_hits = pygame.sprite.spritecollide(self.player, self.collectibles, True)
                for collectible in collectible_hits:
                    self.score += 10
                    self.safety_tips_collected += 1
                    
                    self.coins_for_heal += 1
                    if self.coins_for_heal >= 7:
                        self.player.heal(5)
                        self.spawn_floating_text("+5 HP", self.player.rect.centerx, self.player.rect.top - 20, GREEN)
                        self.coins_for_heal = 0

            
            level_complete = False
            if self.current_level == 5:
                if self.boss and self.boss.is_defeated():
                    self.game_over = True
                    self.won = True
                    self.score += 500
                elif len(self.collectibles) == 0:
                     self.spawn_collectibles()
            else:
                if len(self.collectibles) == 0:
                    level_complete = True
            
            if level_complete:
                if self.current_level == 1 and not self.in_password_challenge:
                     self.in_password_challenge = True
                     self.password_input = ""
                     self.password_feedback = "Type a password..."
                     self.password_strength = ""
                elif self.current_level == 4 and not self.in_email_sorting:
                     self.in_email_sorting = True
                     self.email_list = random.sample(EMAIL_DATA, 5)
                     self.current_email_index = 0
                     self.emails_sorted_correctly = 0
                     self.email_feedback = ""
                elif self.current_level < self.max_levels and not self.in_password_challenge and not self.in_email_sorting:
                    self.current_level += 1
                    self.score += 100 * self.current_level
                    self.init_level()
                else:
                    self.game_over = True
                    self.won = True
    
    def draw(self):
        if self.in_menu:
            self.menu_buttons = self.ui.draw_main_menu(self.screen)
            pygame.display.flip()
            return
        elif self.in_tips:
            self.menu_buttons = self.ui.draw_tips_screen(self.screen)
            pygame.display.flip()
            return
        elif self.enemy_info_active:
            self.ui.draw_enemy_introduction(self.screen, self.collided_enemy_type)
            pygame.display.flip()
            return
        elif self.in_password_challenge:
            self.ui.draw_password_challenge(self.screen, self.password_input, self.password_feedback, self.password_strength)
            pygame.display.flip()
            return
        elif self.in_email_sorting:
            if self.current_email_index < len(self.email_list):
                self.ui.draw_email_sorting(self.screen, self.email_list[self.current_email_index], len(self.email_list) - self.current_email_index, self.email_feedback)
            pygame.display.flip()
            return

        base_color = (30, 30, 60) # Default Blue-ish
        if self.current_level == 2:
            base_color = (30, 60, 30) # Green-ish
        elif self.current_level == 3:
            base_color = (50, 20, 50) # Purple-ish
        elif self.current_level == 4:
            base_color = (60, 30, 20) # Red-ish
        elif self.current_level == 5:
            base_color = (20, 20, 20) # Dark Gray/Black for Boss

        for y in range(SCREEN_HEIGHT):
            color_ratio = y / SCREEN_HEIGHT
            r = int(base_color[0] + color_ratio * 20)
            g = int(base_color[1] + color_ratio * 20)
            b = int(base_color[2] + color_ratio * 20)
            pygame.draw.line(self.screen, (r, g, b), (0, y), (SCREEN_WIDTH, y))
        
        if not self.game_over:
            self.level.platforms.draw(self.screen)
            
            if self.player.invincible and (self.player.invincible_timer // 5) % 2 == 0:
                temp_sprites = pygame.sprite.Group()
                for sprite in self.all_sprites:
                    if sprite != self.player:
                        temp_sprites.add(sprite)
                temp_sprites.draw(self.screen)
            else:
                self.all_sprites.draw(self.screen)
            
            self.ui.draw_health_bar(self.screen, 10, 80, 200, 20,
                                   self.player.health, self.player.max_health)
            self.ui.draw_level_info(self.screen, self.current_level, 
                                   self.level.messages[self.current_level])
            self.ui.draw_score(self.screen, self.score, self.safety_tips_collected)
            self.ui.draw_instructions(self.screen)
            
            # if self.has_weapon:
            #     self.ui.draw_weapon_indicator(self.screen)
            
            if self.boss and self.boss_spawned:
                self.ui.draw_boss_health(self.screen, self.boss.health, self.boss.max_health)
            
            # Draw Floating Texts
            self.draw_floating_texts()

            if self.level_intro_active:
                self.ui.draw_level_introduction(self.screen, self.current_level, self.level.messages[self.current_level])
            
            elif self.current_enemy_warning:
                self.ui.draw_enemy_introduction(self.screen, self.current_enemy_warning)
            
            elif self.boss_warning_active:
                self.ui.draw_boss_warning(self.screen)

            if self.trivia_active:
                self.ui.draw_trivia_popup(self.screen, self.current_question, self.selected_option)

        else:
            self.ui.draw_game_over(self.screen, self.won, self.score)
        
        pygame.display.flip()
    
    def check_password_strength(self):
        pwd = self.password_input
        length = len(pwd)
        has_upper = any(c.isupper() for c in pwd)
        has_lower = any(c.islower() for c in pwd)
        has_digit = any(c.isdigit() for c in pwd)
        has_special = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?/" for c in pwd)
        
        strength = 0
        if length >= 8: strength += 1
        if has_upper: strength += 1
        if has_lower: strength += 1
        if has_digit: strength += 1
        if has_special: strength += 1
        
        if length < 5:
            self.password_strength = "WEAK"
            self.password_feedback = "Too short!"
        elif strength < 3:
            self.password_strength = "WEAK"
            self.password_feedback = "Weak: Use numbers, symbols, and mix case."
        elif strength < 5:
            self.password_strength = "MEDIUM"
            self.password_feedback = "Medium: Almost there! Add special chars."
        else:
            self.password_strength = "STRONG"
            self.password_feedback = "Excellent! Strong Password."

    def restart_game(self):
        self.game_over = False
        self.won = False
        self.current_level = 1
        self.score = 0
        self.safety_tips_collected = 0
        self.coins_for_heal = 0
        self.introduced_enemies = set()
        self.current_enemy_warning = None
        self.enemy_warning_timer = 0
        self.boss_warning_active = False
        self.boss_warning_timer = 0
        self.level_intro_active = False
        self.game_paused = False
        self.all_sprites.empty()
        self.enemies.empty()
        self.collectibles.empty()
        self.projectiles.empty()
        self.init_level()
    
    
    def spawn_floating_text(self, text, x, y, color):
        self.floating_texts.append({
            'text': text,
            'x': x,
            'y': y,
            'color': color,
            'timer': 60
        })

    def draw_floating_texts(self):
        for ft in self.floating_texts:
            text_surf = self.ui.font_medium.render(ft['text'], True, ft['color'])
            outline_surf = self.ui.font_medium.render(ft['text'], True, BLACK)
            self.screen.blit(outline_surf, (ft['x'] - 1, ft['y'] - 1))
            self.screen.blit(outline_surf, (ft['x'] + 1, ft['y'] + 1))
            self.screen.blit(text_surf, (ft['x'], ft['y']))
            
    def update_floating_texts(self):
        for ft in self.floating_texts:
            ft['y'] -= 1 # Float upwards
            ft['timer'] -= 1
        self.floating_texts = [ft for ft in self.floating_texts if ft['timer'] > 0]

    def run(self):
        while self.running:
            self.handle_events()
            self.handle_input()
            self.update()
            self.draw()
            try:
                self.clock.tick(FPS)
            except KeyboardInterrupt:
                self.running = False
        
        pygame.quit()
        sys.exit()
