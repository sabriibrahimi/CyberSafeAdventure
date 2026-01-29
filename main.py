import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from game import CyberSafeGame

if __name__ == "__main__":
    game = CyberSafeGame()
    game.run()
