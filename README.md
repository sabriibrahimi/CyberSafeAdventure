#  Cyber Safe Adventure

**Cyber Safe Adventure** is an educational 2D platformer game designed to teach players, especially children, about internet safety, cybersecurity threats, and best practices. Players navigate through various digital worlds, battling viruses, avoiding scams, and solving security puzzles to defeat the "Master Virus".

---

## How to Play

### **Installation**
1.  Ensure you have **Python 3** installed.
2.  Install the required library:
    ```bash
    pip install pygame
    ```
3.  Run the game:
    ```bash
    python main.py
    or
    py main.py
    ```

### **Controls**
*   **⬅️ Left Arrow / ➡️ Right Arrow**: Move the player.
*   **SPACE**: Jump (Double jump for higher platforms).
*   **⬆️ Up / ⬇️ Down**: Navigate menus and trivia options.
*   **ENTER**: Select menu options / Confirm Answer.
*   **Left Click**: Interact with menus.

---

##  Game Levels & Features

### **Level 1: The Infected Network**
*   **Goal:** Collect 7 "Safety Coins" to cleanse the network.
*   **Enemies:** **Viruses** (Red Spikes).
*   **Challenge:** Basic platforming and enemy avoidance.
*   **End Challenge:** **Password Security Gate**. You must create a **STRONG** password (mix of Upper/Lower case, Numbers, Symbols, >8 chars) to unlock Level 2.

### **Level 2: Phishing Waters**
*   **New Enemies:**
    *   **Phishing** (Blue): Represent fake emails/websites.
    *   **Malware** (Green): Harmful software downloads.
    *   **Online Stranger** (Purple): Unknown dangerous contacts.
*   **Feature:** **Threat Intelligence**. When you touch a new enemy type, the game Pauses and displays an **Info Card** explaining exactly what that threat is and how to avoid it. After learning, you face a quick Trivia Question.

### **Level 3: Stranger Danger**
*   **Goal:** Navigate a complex layout filled with "Online Strangers" and fast-moving Viruses.
*   **Mechanic:** Enemies are faster and patrol tricky platforms.

### **Level 4: Malware Maze**
*   **Goal:** Survive the intense "Malware" infestation.
*   **End Challenge:** **Inbox Cleaner**. Before reaching the boss, you must prove you can spot fake emails.
    *   Sort 5 incoming emails as **SAFE** (Right Arrow) or **PHISHING** (Left Arrow).
    *   Get them right to proceed!

### **Level 5: The Master Virus (Boss Battle)**
*   **The Boss:** A giant, intelligent Virus that chases you and shoots corruption projectiles.
*   **Mechanic:** You cannot hurt the boss with weapons!
*   **How to Win:**
    1.  Find **"?" Question Blocks** scattered around the arena.
    2.  Hit them to trigger a "Firewall Quiz".
    3.  Answer correctly to launch a massive **Counter-Attack** on the boss.
    4.  Survive until the Boss's health reaches 0!

---

##  Educational Mechanics

*   **Trivia Combat:** Touching an enemy doesn't just hurt you; it triggers a **Cybersecurity Quiz**.
    *   **Correct Answer:** You take NO damage (invincible shield) and sometimes Heal.
    *   **Wrong Answer:** You take damage (`-15 HP`).
*   **Visual Feedback:** Floating text (`+5 HP`, `-15 HP`) gives instant feedback on your actions.
*   **Real-world Lessons:** The game teaches about 2FA, Strong Passwords, Phishing detection, and blocking strangers.

---

##  Credits
Developed for the **Faculty Project (PNVI)** to promote digital literacy and safety.

**Enjoy the adventure and stay safe online!** 
**With all respect**
**Sabri Ibrahimi 221554**
**Hamdi Ademi 221589**
