SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
FPS = 60

BLACK = (26, 26, 26)   # Deep Dark Gray
WHITE = (255, 255, 255) # Pure White
GREEN = (0, 255, 0)     # Neon Green (Success/Safe)
RED = (255, 68, 68)     # Vivid Red (Danger/Threat)
YELLOW = (255, 215, 0)  # Gold/Yellow for coins
GRAY = (120, 120, 120)  # Gray for obstacles
DARK_GRAY = (60, 60, 60) # Dark Gray for obstacle volume

# Aliases for mapping old colors to the simplified palette
BLUE = RED      # Phishing (Danger)
PURPLE = RED    # Stranger (Danger)
ORANGE = RED    # Boss/Hazard (Danger)
CYAN = GREEN    # UI/Positive (Safe)
LIGHT_GRAY = WHITE

PLAYER_SPEED = 5
PLAYER_JUMP_STRENGTH = -18
GRAVITY = 0.9
GROUND_TOLERANCE = 5

ENEMY_SPAWN_RATE = 0.02
COLLECTIBLE_SPAWN_RATE = 0.01
EMAIL_DATA = [
    {"sender": "Mom", "subject": "Dinner at 7?", "is_phishing": False},
    {"sender": "Bank Security", "subject": "URGENT: Verify Account Now!", "is_phishing": True},
    {"sender": "Lottery Corp", "subject": "YOU WON $1,000,000!!!", "is_phishing": True},
    {"sender": "Netflix Support", "subject": "Payment Declined", "is_phishing": True},
    {"sender": "Boss", "subject": "Meeting rescheduled", "is_phishing": False},
    {"sender": "Amazon", "subject": "Your package has shipped", "is_phishing": False},
    {"sender": "Unknown", "subject": "Click this link for free iPhone", "is_phishing": True},
    {"sender": "Grandma", "subject": "Cookie recipe", "is_phishing": False},
    {"sender": "IT Dept", "subject": "Password Expiry Notice", "is_phishing": True},
    {"sender": "School", "subject": "Grade Report", "is_phishing": False}
]

DAMAGE_REDUCTION = 0.85