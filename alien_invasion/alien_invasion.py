# alien_invasion
# alien_invasion
# AUTHOR: Maln
# TIME: 21/03/2017

import sys

import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    # Initialize game and create screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make play button
    play_button = Button(ai_settings, screen, "Play")

    # Make a ship
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings,screen,ship, aliens)

    # Create an instance to store game statistics
    stats = GameStats(ai_settings)
    #Create an instance to store game statistics and create scoreboard
    sb = Scoreboard(ai_settings,screen,stats)

    # Start main loop
    while True:
        # Watch for keyboard and mouse events
        gf.check_events(ai_settings,screen,stats,sb, play_button,ship,aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens, bullets)
            gf.update_aliens(ai_settings,stats,sb,screen,ship, aliens, bullets)
            # Redraw screen during each pass through loop

        gf.update_screen(ai_settings, screen, stats,sb, ship,aliens,bullets,play_button)



run_game()
