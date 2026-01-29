import asyncio
import sys
import os
import pygame

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from game import CyberSafeGame
from constants import FPS

async def main():
    game = CyberSafeGame()
    
    # Game Loop (Replaces game.run() to allow async await)
    while game.running:
        game.handle_events()
        game.handle_input()
        game.update()
        game.draw()
        
        # Cap Key Frame Rate
        game.clock.tick(FPS)
        
        # Yield control to the browser (Critical for Web/Pygbag)
        await asyncio.sleep(0)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    asyncio.run(main())
