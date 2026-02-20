# Cyber Safe Adventure

Cyber Safe Adventure is an educational 2D platformer game built with Python and Pygame. It is designed to teach players, especially children and young students, about internet safety, cybersecurity threats, and best practices in a fun and interactive way. Players navigate through five progressively challenging digital worlds, collecting safety coins, battling viruses, avoiding scams, answering cybersecurity trivia questions, and ultimately defeating the "Master Virus" boss to complete the game.

---

## Git Repository Page

[https://sabriibrahimi.github.io/CyberSafeAdventure/](https://sabriibrahimi.github.io/CyberSafeAdventure/)

## Video Demonstration

[https://drive.google.com/file/d/1sGdJfmwCGrGhcuXSCGfjDa0A_EOE_WA2/view?usp=sharing](https://drive.google.com/file/d/1sGdJfmwCGrGhcuXSCGfjDa0A_EOE_WA2/view?usp=sharing)

---

## Installation and How to Run

1. Make sure you have **Python 3** installed on your system.
2. Install the required library by running the following command in your terminal:
   ```bash
   pip install pygame
   ```
3. Start the game by running:
   ```bash
   python main.py
   ```
   or
   ```bash
   py main.py
   ```

---

## Controls

- **Left Arrow / Right Arrow**: Move the player left or right.
- **SPACE**: Jump. Pressing SPACE again while in the air performs a double jump, allowing the player to reach higher platforms.
- **Up Arrow / Down Arrow**: Navigate through menus and select trivia answer options.
- **ENTER**: Confirm a menu selection or submit a trivia answer.
- **Left Click**: Interact with on-screen buttons and menus.

---

## Game Overview and Start Screen

When the game launches, players are presented with the main menu where they can start a new game, view instructions, or exit. The start screen sets the tone for the adventure with a clear visual introduction to the game world.

![Start Screen](images/Preview_start_game.png)

The start screen shows the game title, available menu options, and an initial preview of the game environment. From here the player begins their journey through the five levels.

---

## Game Levels and Features

### Level 1: The Infected Network

The first level introduces the player to the core mechanics of the game. The goal is to collect 7 "Safety Coins" scattered across the platforms while avoiding red spike enemies that represent computer Viruses.

- **Goal:** Collect 7 Safety Coins to cleanse the infected network.
- **Enemies:** Viruses represented as red spiked obstacles that patrol the platforms.
- **Challenge:** Basic platforming movement and enemy avoidance.
- **End Challenge:** At the end of the level, the player encounters a Password Security Gate. To unlock Level 2, the player must create a strong password that meets all security requirements: a mix of uppercase and lowercase letters, numbers, symbols, and a minimum of 8 characters.

![Creating a Strong Password](images/learning_to_create_strong_psw.png)

The password creation screen teaches players what makes a password secure. Visual feedback is given in real time, highlighting which criteria have been met and which are still missing, reinforcing good password habits in an interactive way.

---

### Level 2: Phishing Waters

Level 2 introduces three new enemy types, each representing a different real-world digital threat. This level is designed to educate players about the variety of dangers they may encounter online.

- **Phishing enemies (Blue):** Represent fake emails and fraudulent websites attempting to steal personal information.
- **Malware enemies (Green):** Represent harmful software that can damage a device or steal data when accidentally downloaded.
- **Online Stranger enemies (Purple):** Represent unknown and potentially dangerous contacts online.

A key educational feature introduced in this level is Threat Intelligence. The first time a player touches a new enemy type, the game pauses and displays an Info Card explaining exactly what that type of threat is, how it works in real life, and how to avoid it. After reading the card, the player faces a short trivia question to confirm their understanding before continuing.

![Enemy Info Card - What is This Enemy?](images/level_2_whats_the_enemy.png)

The info card screen pauses gameplay and presents a clear explanation of the new threat type encountered. This approach ensures players learn about each threat in the context of encountering it, making the lesson more memorable and impactful.

---

### Level 3: Stranger Danger

Level 3 increases the difficulty by filling the level with Online Stranger enemies and faster-moving Virus enemies. The platform layout becomes more complex, requiring precise jumping and planning.

- **Goal:** Navigate the level from start to checkpoint while avoiding all enemies.
- **Mechanic:** Enemies patrol faster and cover more dangerous platform combinations, demanding greater player awareness and reflexes.

---

### Level 4: Malware Maze

Level 4 presents the most intense enemy infestation before the final boss. Malware enemies fill the level and move at higher speeds. At the end of this level, before the player can proceed, they must complete the Inbox Cleaner challenge.

- **End Challenge - Inbox Cleaner:** The player is shown 5 incoming emails one by one. For each email, they must decide whether it is a safe legitimate email (press Right Arrow) or a phishing attempt (press Left Arrow). All 5 emails must be sorted correctly to unlock the path to the final level.

![Inbox Cleaner - Learning to Spot Emails and Spam](images/learning_emails_and_spams.png)

The inbox cleaner challenge simulates a real-world scenario where the player must evaluate email content for signs of phishing, such as suspicious sender addresses, urgent language, or requests for personal information. This directly trains a critical skill for safe internet use.

---

### Level 5: The Master Virus (Boss Battle)

The final level is a boss arena where the player faces the Master Virus, a large and intelligent enemy that actively chases the player and launches corruption projectiles. Traditional combat does not work against this boss; the player must use knowledge to defeat it.

- **How to Win:**
  1. Find Question Blocks scattered around the arena and jump into them from below.
  2. Each Question Block triggers a Firewall Quiz with a cybersecurity question.
  3. Answering correctly launches a Counter-Attack that reduces the boss's health.
  4. Survive the boss's attacks while answering enough questions correctly to bring its health to zero.

![Final Boss Battle](images/final_boss.png)

The boss battle combines all the skills and knowledge the player has gathered throughout the game. The player must stay mobile to avoid projectiles while actively seeking out Question Blocks to trigger quiz challenges. This level reinforces that knowledge and awareness are the most powerful tools against digital threats.

---

## Educational Mechanics

### Trivia Combat System

Throughout every level, touching an enemy triggers a cybersecurity quiz question instead of immediate damage. This system transforms every enemy encounter into a learning opportunity.

![Trivia Question After Touching an Enemy](images/questions_after_touching_enemy.png)

When the player touches an enemy, the game pauses and presents a multiple-choice trivia question related to cybersecurity. The player uses the Up and Down arrows to select an answer and presses ENTER to confirm.

- **Correct Answer:** The player takes no damage and receives a temporary invincibility shield. In some cases, the player also regains a small amount of health.
- **Wrong Answer:** The player takes 15 HP of damage and must continue the level more carefully.

Floating text indicators appear on screen to give instant visual feedback, showing messages such as "+5 HP" for healing or "-15 HP" for damage taken.

### Real-World Lessons Covered

The game covers the following cybersecurity topics across all its levels and challenges:

- Creating and using strong passwords.
- Recognizing and avoiding phishing emails and fraudulent websites.
- Understanding what malware is and how it spreads.
- Staying safe when communicating with strangers online.
- Understanding two-factor authentication (2FA).
- Identifying safe versus suspicious email content.
- Using firewalls and security tools as a defense against cyber threats.

---

## Technical Details

The game is built entirely in Python using the Pygame library. All game logic, level design, enemy behavior, UI rendering, and educational content are managed through Python scripts organized inside the `src` directory. The main entry point is `main.py` located in the project root. No additional game engine is required beyond a standard Python 3 installation and the Pygame package.

---

## Team: Cyber Avangers

**Members:**

Sabri Ibrahimi 221554

Hamdi Ademi 221589
