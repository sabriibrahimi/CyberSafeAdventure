import pygame
from constants import *


class UI:
    def __init__(self):
        self.font_large = None
        self.font_medium = None
        self.font_small = None
        self.init_fonts()

    def init_fonts(self):
        try:
            self.font_large = pygame.font.Font(None, 48)
            self.font_medium = pygame.font.Font(None, 36)
            self.font_small = pygame.font.Font(None, 24)
            self.font_huge = pygame.font.Font(None, 72)
        except:
            self.font_large = pygame.font.SysFont('arial', 48)
            self.font_medium = pygame.font.SysFont('arial', 36)
            self.font_small = pygame.font.SysFont('arial', 24)
            self.font_huge = pygame.font.SysFont('arial', 72)

    def draw_health_bar(self, screen, x, y, width, height, current, maximum):
        pygame.draw.rect(screen, DARK_GRAY, (x, y, width, height))
        health_width = int((current / maximum) * width)
        pygame.draw.rect(screen, GREEN, (x, y, health_width, height))
        pygame.draw.rect(screen, WHITE, (x, y, width, height), 2)

    def draw_text(self, screen, text, x, y, font, color=WHITE):
        text_surface = font.render(text, True, color)
        screen.blit(text_surface, (x, y))

    def wrap_text(self, text, max_width, font):
        words = text.split()
        lines = []
        current_line = []

        for word in words:
            test_line = ' '.join(current_line + [word])
            text_width = font.size(test_line)[0]

            if text_width <= max_width:
                current_line.append(word)
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                current_line = [word]

        if current_line:
            lines.append(' '.join(current_line))

        return lines if lines else [text]

    def draw_level_info(self, screen, level_num, message):
        self.draw_text(screen, f"Level {level_num}", 10, 10, self.font_medium, YELLOW)
        self.draw_text(screen, message, 10, 40, self.font_small, WHITE)
        self.draw_text(screen, "Health:", 10, 60, self.font_small, WHITE)

    def draw_score(self, screen, score, safety_tips):
        self.draw_text(screen, f"Score: {score}", SCREEN_WIDTH - 200, 10, self.font_medium, YELLOW)
        self.draw_text(screen, f"Safety Tips: {safety_tips}", SCREEN_WIDTH - 200, 50, self.font_small, GREEN)

    def draw_boss_health(self, screen, current, maximum):
        bar_width = 400
        bar_height = 30
        x = (SCREEN_WIDTH - bar_width) // 2
        y = 10

        pygame.draw.rect(screen, DARK_GRAY, (x, y, bar_width, bar_height))
        health_width = int((current / maximum) * bar_width)
        health_color = RED if current < maximum * 0.3 else ORANGE if current < maximum * 0.6 else RED
        pygame.draw.rect(screen, health_color, (x, y, health_width, bar_height))
        pygame.draw.rect(screen, WHITE, (x, y, bar_width, bar_height), 3)
        self.draw_text(screen, "BOSS", x + bar_width // 2 - 30, y + 5, self.font_medium, YELLOW)
        health_text = f"{current}/{maximum}"
        text_width = self.font_small.size(health_text)[0]
        self.draw_text(screen, health_text, x + bar_width - text_width - 10, y + 8, self.font_small, WHITE)

    def draw_warning(self, screen, text):
        text_width = self.font_medium.size(text)[0]
        x = (SCREEN_WIDTH - text_width) // 2
        y = 90

        padding = 10
        pygame.draw.rect(screen, BLACK, (x - padding, y - padding, text_width + padding * 2, 40))
        pygame.draw.rect(screen, RED, (x - padding, y - padding, text_width + padding * 2, 40), 2)

        self.draw_text(screen, text, x, y, self.font_medium, YELLOW)

    def draw_game_over(self, screen, won=False, final_score=0):
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(200)
        overlay.fill(BLACK)
        screen.blit(overlay, (0, 0))

        if won:
            victory_text = " VICTORY! "
            victory_width = self.font_huge.size(victory_text)[0]
            self.draw_text(screen, victory_text, SCREEN_WIDTH // 2 - victory_width // 2, SCREEN_HEIGHT // 2 - 150,
                           self.font_huge, GREEN)

            congrats_text = "Congratulations! You defeated the boss!"
            congrats_width = self.font_large.size(congrats_text)[0]
            self.draw_text(screen, congrats_text, SCREEN_WIDTH // 2 - congrats_width // 2, SCREEN_HEIGHT // 2 - 80,
                           self.font_large, YELLOW)

            learned_text = "You've learned how to stay safe online!"
            learned_width = self.font_medium.size(learned_text)[0]
            self.draw_text(screen, learned_text, SCREEN_WIDTH // 2 - learned_width // 2, SCREEN_HEIGHT // 2 - 30,
                           self.font_medium, WHITE)

            champion_text = "You are now a Cyber Safety Champion!"
            champion_width = self.font_medium.size(champion_text)[0]
            self.draw_text(screen, champion_text, SCREEN_WIDTH // 2 - champion_width // 2, SCREEN_HEIGHT // 2 + 20,
                           self.font_medium, GREEN)
        else:
            game_over_text = "Game Over"
            game_over_width = self.font_large.size(game_over_text)[0]
            self.draw_text(screen, game_over_text, SCREEN_WIDTH // 2 - game_over_width // 2, SCREEN_HEIGHT // 2 - 100,
                           self.font_large, RED)
            restart_text = "Press R to restart"
            restart_width = self.font_medium.size(restart_text)[0]
            self.draw_text(screen, restart_text, SCREEN_WIDTH // 2 - restart_width // 2, SCREEN_HEIGHT // 2 - 50,
                           self.font_medium, WHITE)

        score_text = f"Final Score: {final_score}"
        score_width = self.font_medium.size(score_text)[0]
        self.draw_text(screen, score_text, SCREEN_WIDTH // 2 - score_width // 2, SCREEN_HEIGHT // 2 + 80,
                       self.font_medium, YELLOW)
        exit_text = "Press R to restart | Press ESC to exit"
        exit_width = self.font_small.size(exit_text)[0]
        self.draw_text(screen, exit_text, SCREEN_WIDTH // 2 - exit_width // 2, SCREEN_HEIGHT // 2 + 130,
                       self.font_small, GRAY)

    def draw_instructions(self, screen):
        instructions = "← → Move | Space Jump | Avoid Enemies | Collect coins"
        text_width = self.font_small.size(instructions)[0]
        x_pos = (SCREEN_WIDTH - text_width) // 2
        self.draw_text(screen, instructions, x_pos, SCREEN_HEIGHT - 30, self.font_small, GRAY)

    # popup at start of each level
    def draw_level_introduction(self, screen, level_num, message):
        level_info = {
            1: {
                "title": "LEVEL 1: PROTECT YOURSELF FROM VIRUSES",
                "description": "In this level, you'll learn about computer viruses and how to avoid them.",
                "tips": [
                    "• Don't click on suspicious links or pop-ups",
                    "• Keep your antivirus software updated",
                    "• Be careful when downloading files",
                    "• Avoid opening emails from unknown senders"
                ],
                "goal": "Collect all safety tips while avoiding viruses!"
            },
            2: {
                "title": "LEVEL 2: BEWARE OF ONLINE STRANGERS",
                "description": "Learn how to protect yourself from people who might try to harm you online.",
                "tips": [
                    "• Never share personal information with strangers",
                    "• Don't meet people you only know online",
                    "• Tell a trusted adult if someone makes you uncomfortable",
                    "• Remember: not everyone online is who they say they are"
                ],
                "goal": "Stay safe and collect all the safety tips!"
            },
            3: {
                "title": "LEVEL 3: CREATE STRONG PASSWORDS",
                "description": "Learn how to create and protect your passwords.",
                "tips": [
                    "• Use a mix of letters, numbers, and symbols",
                    "• Don't use the same password everywhere",
                    "• Never share your passwords with anyone",
                    "• Change passwords regularly"
                ],
                "goal": "Collect all safety tips and keep your passwords safe!"
            },
            4: {
                "title": "LEVEL 4: AVOID DANGEROUS DOWNLOADS",
                "description": "Learn to be careful with downloads and attachments.",
                "tips": [
                    "• Only download from trusted websites",
                    "• Don't open email attachments from strangers",
                    "• Scan downloads with antivirus software",
                    "• Ask an adult before downloading anything"
                ],
                "goal": "Collect all safety tips while avoiding dangerous downloads!"
            },
            5: {
                "title": "LEVEL 5: FINAL BOSS BATTLE",
                "description": "Use everything you've learned to defeat the ultimate cyber threat!",
                "tips": [
                    "• You now have a weapon - press X or Z to shoot",
                    "• Collect safety tips to damage the boss",
                    "• Avoid all enemies and the boss",
                    "• This is your final test - you can do it!"
                ],
                "goal": "Defeat the boss and become a Cyber Safety Champion!"
            }
        }

        info = level_info.get(level_num, level_info[1])

        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(200)
        overlay.fill(BLACK)
        screen.blit(overlay, (0, 0))

        box_width = 900
        box_height = 550
        box_x = (SCREEN_WIDTH - box_width) // 2
        box_y = (SCREEN_HEIGHT - box_height) // 2

        title_text = info['title']
        title_width = self.font_large.size(title_text)[0]
        self.draw_text(screen, title_text, box_x + (box_width - title_width) // 2, box_y + 30,
                       self.font_large, YELLOW)

        desc_y = box_y + 90
        desc_lines = self.wrap_text(info['description'], box_width - 100, self.font_medium)
        for i, line in enumerate(desc_lines):
            self.draw_text(screen, line, box_x + 50, desc_y + i * 35, self.font_medium, WHITE)

        tips_y = desc_y + len(desc_lines) * 35 + 30
        self.draw_text(screen, "What you'll learn:", box_x + 50, tips_y, self.font_medium, GREEN)

        tip_start_y = tips_y + 40
        for i, tip in enumerate(info['tips']):
            self.draw_text(screen, tip, box_x + 70, tip_start_y + i * 30, self.font_small, WHITE)

        goal_y = tip_start_y + len(info['tips']) * 30 + 20
        goal_lines = self.wrap_text(info['goal'], box_width - 100, self.font_medium)
        for i, line in enumerate(goal_lines):
            self.draw_text(screen, line, box_x + 50, goal_y + i * 30, self.font_medium, YELLOW)

        continue_text = "Press SPACE to start the level..."
        continue_width = self.font_medium.size(continue_text)[0]
        self.draw_text(screen, continue_text, box_x + (box_width - continue_width) // 2,
                       box_y + box_height - 50, self.font_medium, GREEN)

    def draw_weapon_indicator(self, screen):
        pass

    def draw_enemy_introduction(self, screen, enemy_type):
        enemy_info = {
            "virus": {
                "name": "COMPUTER VIRUS",
                "description": "A malicious program that can damage your computer",
                "danger": "Trying to infect your device and steal your data",
                "action": "AVOID at all costs!",
                "color": RED
            },
            "phishing": {
                "name": "PHISHING ATTACK",
                "description": "Fake websites or messages trying to trick you",
                "danger": "Trying to steal your passwords and personal information",
                "action": "Never click suspicious links!",
                "color": BLUE
            },
            "stranger": {
                "name": "ONLINE STRANGER",
                "description": "Unknown person trying to contact you online",
                "danger": "Trying to get your personal information or meet you",
                "action": "Never share personal info with strangers!",
                "color": PURPLE
            },
            "malware": {
                "name": "MALWARE",
                "description": "Harmful software that can spy on you",
                "danger": "Trying to monitor your activity and steal your data",
                "action": "Don't download from untrusted sources!",
                "color": GREEN
            }
        }

        info = enemy_info.get(enemy_type, enemy_info["virus"])

        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(200)
        overlay.fill(BLACK)
        screen.blit(overlay, (0, 0))

        box_width = 900
        box_height = 500
        box_x = (SCREEN_WIDTH - box_width) // 2
        box_y = (SCREEN_HEIGHT - box_height) // 2

        preview_size = 60
        preview_x = box_x + box_width - 100
        preview_y = box_y + 50
        preview_surface = pygame.Surface((preview_size, preview_size), pygame.SRCALPHA)
        points = [
            (preview_size // 2, 5),
            (5, preview_size - 5),
            (preview_size - 5, preview_size - 5)
        ]
        pygame.draw.polygon(preview_surface, info['color'], points)
        pygame.draw.polygon(preview_surface, WHITE, points, 3)
        pygame.draw.line(preview_surface, WHITE, (preview_size // 2, 20), (preview_size // 2, 30), 3)
        pygame.draw.circle(preview_surface, WHITE, (preview_size // 2, 38), 3)
        screen.blit(preview_surface, (preview_x, preview_y))

        title_text = f"⚠ {info['name']} ⚠"
        title_width = self.font_large.size(title_text)[0]
        self.draw_text(screen, title_text, box_x + (box_width - title_width) // 2, box_y + 30,
                       self.font_large, info['color'])

        desc_y = box_y + 110
        self.draw_text(screen, "What is it?", box_x + 50, desc_y, self.font_medium, YELLOW)
        desc_lines = self.wrap_text(info['description'], box_width - 100, self.font_medium)
        for i, line in enumerate(desc_lines):
            self.draw_text(screen, line, box_x + 50, desc_y + 35 + i * 30, self.font_medium, WHITE)

        danger_y = desc_y + 35 + len(desc_lines) * 30 + 20
        self.draw_text(screen, "What does it want?", box_x + 50, danger_y, self.font_medium, YELLOW)
        danger_lines = self.wrap_text(info['danger'], box_width - 100, self.font_medium)
        for i, line in enumerate(danger_lines):
            self.draw_text(screen, line, box_x + 50, danger_y + 35 + i * 30, self.font_medium, WHITE)

        action_y = danger_y + 35 + len(danger_lines) * 30 + 20
        self.draw_text(screen, "What should you do?", box_x + 50, action_y, self.font_medium, YELLOW)
        action_lines = self.wrap_text(info['action'], box_width - 100, self.font_medium)
        for i, line in enumerate(action_lines):
            self.draw_text(screen, line, box_x + 50, action_y + 35 + i * 30, self.font_medium, GREEN)

        continue_text = "Press SPACE to continue..."
        continue_width = self.font_small.size(continue_text)[0]
        self.draw_text(screen, continue_text, box_x + (box_width - continue_width) // 2,
                       box_y + box_height - 40, self.font_small, GRAY)

    def draw_boss_warning(self, screen):
        flash = (pygame.time.get_ticks() // 200) % 2

        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(220 if flash else 180)
        overlay.fill(BLACK)
        screen.blit(overlay, (0, 0))

        warning_text1 = "⚠ DANGEROUS INTERNET THREAT DETECTED ⚠"
        warning_text2 = "ESCAPE IMMEDIATELY"
        warning_text3 = "MAJOR CYBER ATTACK INCOMING"

        text1_width = self.font_huge.size(warning_text1)[0]
        text2_width = self.font_large.size(warning_text2)[0]
        text3_width = self.font_medium.size(warning_text3)[0]

        center_x = SCREEN_WIDTH // 2

        color1 = RED if flash else YELLOW
        self.draw_text(screen, warning_text1, center_x - text1_width // 2,
                       SCREEN_HEIGHT // 2 - 150, self.font_huge, color1)

        self.draw_text(screen, warning_text2, center_x - text2_width // 2,
                       SCREEN_HEIGHT // 2 - 50, self.font_large, RED)

        self.draw_text(screen, warning_text3, center_x - text3_width // 2,
                       SCREEN_HEIGHT // 2 + 50, self.font_medium, ORANGE)

        border_thickness = 10
        pygame.draw.rect(screen, RED, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), border_thickness)

    def draw_trivia_popup(self, screen, question_data, selected_option=None, enemy_type=None):
        box_width = 900
        box_height = 600
        box_x = (SCREEN_WIDTH - box_width) // 2
        box_y = (SCREEN_HEIGHT - box_height) // 2

        # Draw a smaller black background area for the trivia
        pygame.draw.rect(screen, BLACK, (box_x, box_y, box_width, box_height))
        pygame.draw.rect(screen, WHITE, (box_x, box_y, box_width, box_height), 4)

        y_offset = 20
        if enemy_type:
            warn_color = RED
            warn_text = f"You touched a {enemy_type.upper()}!"
            if enemy_type == "phishing":
                warn_color = BLUE
            elif enemy_type == "malware":
                warn_color = GREEN
            elif enemy_type == "stranger":
                warn_color = PURPLE

            warn_width = self.font_large.size(warn_text)[0]
            self.draw_text(screen, warn_text, box_x + (box_width - warn_width) // 2, box_y + y_offset, self.font_large,
                           warn_color)

            y_offset += 50
            sub_text = "Answer correctly to defend yourself!"
            sub_width = self.font_small.size(sub_text)[0]
            self.draw_text(screen, sub_text, box_x + (box_width - sub_width) // 2, box_y + y_offset, self.font_small,
                           WHITE)
            y_offset += 40
        else:
            self.draw_text(screen, "CYBER SAFETY QUIZ", box_x + box_width // 2 - 100, box_y + y_offset, self.font_large,
                           CYAN)
            y_offset += 60

        question_lines = self.wrap_text(question_data["question"], box_width - 40, self.font_medium)
        for i, line in enumerate(question_lines):
            self.draw_text(screen, line, box_x + 20, box_y + y_offset + i * 30, self.font_medium, WHITE)

        option_start_y = box_y + y_offset + len(question_lines) * 30 + 30
        option_rects = []

        labels = ["a", "b", "c"]
        for i, option in enumerate(question_data["options"]):
            color = WHITE
            if i == selected_option:
                color = YELLOW

            option_text = f"{labels[i]}) {option}"
            y_pos = option_start_y + i * 80

            if i == selected_option:
                pygame.draw.rect(screen, BLACK, (box_x + 10, y_pos - 10, box_width - 20, 60))
                pygame.draw.rect(screen, GREEN, (box_x + 10, y_pos - 10, box_width - 20, 60), 2)

            self.draw_text(screen, option_text, box_x + 20, y_pos, self.font_small, color)

            rect = pygame.Rect(box_x + 10, y_pos - 10, box_width - 20, 60)
            option_rects.append(rect)

        self.draw_text(screen, "Select answer with UP/DOWN keys and press ENTER", box_x + 20, box_y + box_height - 40,
                       self.font_small, GRAY)

        return option_rects

    def draw_main_menu(self, screen):
        screen.fill(BLACK)

        title_text = "CYBER SAFE ADVENTURE"
        title_width = self.font_huge.size(title_text)[0]
        self.draw_text(screen, title_text, (SCREEN_WIDTH - title_width) // 2, 150, self.font_huge, CYAN)

        subtitle_text = "Learn to navigate the internet safely!"
        subtitle_width = self.font_medium.size(subtitle_text)[0]
        self.draw_text(screen, subtitle_text, (SCREEN_WIDTH - subtitle_width) // 2, 220, self.font_medium, WHITE)

        button_width = 300
        button_height = 60
        start_x = (SCREEN_WIDTH - button_width) // 2
        start_y = 350
        tips_y = 450

        start_rect = pygame.Rect(start_x, start_y, button_width, button_height)
        pygame.draw.rect(screen, GREEN, start_rect)
        pygame.draw.rect(screen, WHITE, start_rect, 3)

        start_text = "START GAME"
        text_width = self.font_large.size(start_text)[0]
        self.draw_text(screen, start_text, start_x + (button_width - text_width) // 2, start_y + 15, self.font_large,
                       BLACK)

        tips_rect = pygame.Rect(start_x, tips_y, button_width, button_height)
        pygame.draw.rect(screen, BLACK, tips_rect)
        pygame.draw.rect(screen, WHITE, tips_rect, 3)

        tips_text = "HOW TO PLAY & TIPS"
        text_width = self.font_medium.size(tips_text)[0]
        self.draw_text(screen, tips_text, start_x + (button_width - text_width) // 2, tips_y + 18, self.font_medium,
                       WHITE)

        return {'start': start_rect, 'tips': tips_rect}

    def draw_tips_screen(self, screen):
        screen.fill(BLACK)

        title_text = "GAME GUIDE & LEARNING GOALS"
        title_width = self.font_large.size(title_text)[0]
        self.draw_text(screen, title_text, (SCREEN_WIDTH - title_width) // 2, 50, self.font_large, YELLOW)

        content = [
            ("GOAL OF THE GAME:", YELLOW),
            ("Navigate through 5 levels representing different aspects of internet safety.", WHITE),
            ("Collect 'Safety Tips' (scrolls) to heal and earn points.", WHITE),
            ("Avoid enemies like Viruses, Phishing attacks, and Malware.", WHITE),
            ("", WHITE),
            ("CONTROLS:", YELLOW),
            ("Arrow Keys : Move Left/Right", WHITE),
            ("Space Bar : Jump", WHITE),
            ("", WHITE),
            ("WHAT YOU WILL LEARN:", GREEN),
            ("1. Avoiding suspicious links and viruses.", WHITE),
            ("2. The importance of not sharing personal info with strangers.", WHITE),
            ("3. Creating strong, secure passwords.", WHITE),
            ("4. Identifying dangerous downloads and attachments.", WHITE),
            ("5. Fighting back against cyber threats with knowledge!", WHITE)
        ]

        start_y = 120
        for text, color in content:
            if text == "":
                start_y += 20
                continue
            self.draw_text(screen, text, 100, start_y, self.font_medium if color != WHITE else self.font_small, color)
            start_y += 35

        back_width = 200
        back_height = 50
        back_x = (SCREEN_WIDTH - back_width) // 2
        back_y = SCREEN_HEIGHT - 100

        back_rect = pygame.Rect(back_x, back_y, back_width, back_height)
        pygame.draw.rect(screen, RED, back_rect)
        pygame.draw.rect(screen, WHITE, back_rect, 3)

        back_text = "BACK TO MENU"
        text_width = self.font_medium.size(back_text)[0]
        self.draw_text(screen, back_text, back_x + (back_width - text_width) // 2, back_y + 12, self.font_medium, BLACK)

        return {'back': back_rect}

    def draw_password_challenge(self, screen, input_text, feedback_text, strength_level):
        screen.fill((10, 10, 20))

        title_text = "LEVEL 1 SECURITY CHECK"
        title_width = self.font_huge.size(title_text)[0]
        self.draw_text(screen, title_text, (SCREEN_WIDTH - title_width) // 2, 40, self.font_huge, GREEN)

        panel_rect = pygame.Rect(100, 100, SCREEN_WIDTH - 200, 280)
        pygame.draw.rect(screen, BLACK, panel_rect, border_radius=10)
        pygame.draw.rect(screen, GREEN, panel_rect, 2, border_radius=10)

        info_lines = [
            ("PASSWORD SECURITY TRAINING", CYAN),
            ("", WHITE),
            ("WEAK: '123456', 'password', 'sabri' (Instantly hackable)", RED),
            ("MEDIUM: 'MyDogRex1', 'Soccer20' (Cracked in minutes)", ORANGE),
            ("STRONG: 'Trov!8#Z2', 'K$m9Lp@1' (Takes centuries to crack)", GREEN),
            ("", WHITE),
            ("MISSION: Create a STRONG password (8+ chars, mix case, numbers, symbols)", YELLOW)
        ]

        start_y = 120
        for text, color in info_lines:
            text_width = self.font_medium.size(text)[0]
            self.draw_text(screen, text, (SCREEN_WIDTH - text_width) // 2, start_y, self.font_medium, color)
            start_y += 35

        input_box_width = 500
        input_box_height = 60
        input_x = (SCREEN_WIDTH - input_box_width) // 2
        input_y = 420

        border_color = WHITE
        status_icon = "..."
        if strength_level == "STRONG":
            border_color = GREEN
            status_icon = "✔ SECURE"
        elif strength_level == "MEDIUM":
            border_color = ORANGE
            status_icon = "⚠ WEAK"
        elif strength_level == "WEAK":
            border_color = RED
            status_icon = "❌ VULNERABLE"

        pygame.draw.rect(screen, (0, 0, 0), (input_x, input_y, input_box_width, input_box_height))
        pygame.draw.rect(screen, border_color, (input_x, input_y, input_box_width, input_box_height), 3)

        text_surface = self.font_large.render(input_text, True, WHITE)
        screen.blit(text_surface, (input_x + 15, input_y + 12))

        if (pygame.time.get_ticks() // 500) % 2 == 0:
            cursor_x = input_x + 15 + text_surface.get_width()
            pygame.draw.line(screen, WHITE, (cursor_x, input_y + 10), (cursor_x, input_y + 50), 2)

        if feedback_text:
            feed_text = f"ANALYSIS: {feedback_text}"
            feed_width = self.font_medium.size(feed_text)[0]

            feed_color = WHITE
            if strength_level == "WEAK":
                feed_color = RED
            elif strength_level == "MEDIUM":
                feed_color = ORANGE
            elif strength_level == "STRONG":
                feed_color = GREEN

            self.draw_text(screen, feed_text, (SCREEN_WIDTH - feed_width) // 2, input_y + 80, self.font_medium,
                           feed_color)

        strength_text = f"STATUS: {status_icon}"
        strength_width = self.font_medium.size(strength_text)[0]
        self.draw_text(screen, strength_text, (SCREEN_WIDTH - strength_width) // 2, input_y - 40, self.font_medium,
                       border_color)

        if strength_level == "STRONG":
            cont_text = "ACCESS GRANTED - PRESS ENTER TO PROCEED"
            cont_bg = pygame.Rect(0, 550, SCREEN_WIDTH, 50)
            pygame.draw.rect(screen, BLACK, cont_bg)

            cont_width = self.font_large.size(cont_text)[0]
            self.draw_text(screen, cont_text, (SCREEN_WIDTH - cont_width) // 2, 560, self.font_large, GREEN)

    def draw_email_sorting(self, screen, email_data, progress, feedback):
        screen.fill(BLACK)

        title = "INBOX CLEANER: SORT THE EMAILS"
        title_w = self.font_large.size(title)[0]
        self.draw_text(screen, title, (SCREEN_WIDTH - title_w) // 2, 50, self.font_large, CYAN)

        card_w, card_h = 600, 350
        card_x = (SCREEN_WIDTH - card_w) // 2
        card_y = 150

        pygame.draw.rect(screen, WHITE, (card_x, card_y, card_w, card_h), border_radius=15)
        pygame.draw.rect(screen, LIGHT_GRAY, (card_x, card_y, card_w, 60), border_radius=15)
        pygame.draw.rect(screen, LIGHT_GRAY, (card_x, card_y + 30, card_w, 30))  # Fill rounded corners bottom

        self.draw_text(screen, f"FROM: {email_data['sender']}", card_x + 20, card_y + 15, self.font_medium, BLACK)
        self.draw_text(screen, f"SUBJECT:", card_x + 20, card_y + 80, self.font_small, GRAY)
        self.draw_text(screen, f"{email_data['subject']}", card_x + 20, card_y + 110, self.font_large, BLACK)

        pygame.draw.circle(screen, RED, (card_x - 60, card_y + card_h // 2), 40)
        self.draw_text(screen, "<", card_x - 70, card_y + card_h // 2 - 15, self.font_large, WHITE)
        self.draw_text(screen, "PHISHING", card_x - 90, card_y + card_h // 2 + 50, self.font_small, RED)

        pygame.draw.circle(screen, GREEN, (card_x + card_w + 60, card_y + card_h // 2), 40)
        self.draw_text(screen, ">", card_x + card_w + 50, card_y + card_h // 2 - 15, self.font_large, WHITE)
        self.draw_text(screen, "SAFE", card_x + card_w + 40, card_y + card_h // 2 + 50, self.font_small, GREEN)

        self.draw_text(screen, f"EMAILS LEFT: {progress}", (SCREEN_WIDTH - 200) // 2, 550, self.font_medium, WHITE)

        if feedback:
            color = GREEN if feedback == "CORRECT!" else RED
            fb_w = self.font_huge.size(feedback)[0]
            self.draw_text(screen, feedback, (SCREEN_WIDTH - fb_w) // 2, card_y + card_h - 60, self.font_huge, color)