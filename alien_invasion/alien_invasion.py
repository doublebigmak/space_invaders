# alien_invasion
# alien_invasion
# AUTHOR: Maln
# TIME: 21/03/2017

import sys

import pygame

from settings import Settings
from ship import Ship


def run_game():
    # Initialize game and create screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(screen)

    # Start main loop
    while True:

        # Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # Redraw screen during each pass through loop
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # Make most recently drawn screen visible
        pygame.display.flip()

run_game()