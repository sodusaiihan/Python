import sys

import pygame

from settings import Settings
from ship import Ship

class AlianInvasion:
    """Overall class to manage the game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alian Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouses events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # Make the most recently draw screen visible.
            pygame.display.flip()

if __name__ == 'main':
    # Make a game instance, and run the game.
    ai = AlianInvasion()
    ai.run_game()