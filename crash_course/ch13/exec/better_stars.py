
import pygame
import sys

from pygame.sprite import Group
from pygame.sprite import Sprite
from random import randint


class Settings():
    """A class that stores all settings."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)


class Star(Sprite):
    """A class to represent a single star."""

    def __init__(self, settings, screen):
        """Initialize star and set its starting position."""
        super().__init__()
        self.settings = settings
        self.screen = screen

        # load star image and set its rect attribute.
        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()

        # Start each new star near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def blitme(self):
        """Draw the start at its current location."""
        self.screen.blit(self.image, self.rect)


def check_keydown_events(event, settings, screen):
    """Respond to key presses."""
    if event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event):
    """Respond to key releases."""
    pass


def check_events(settings, screen):
    """Respond to key presses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event)


def update_screen(settings, screen, stars):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(settings.bg_color)
    # Redraw all stars.
    stars.draw(screen)

    # Make the most recently drawn screen visible.
    pygame.display.flip()


def get_number_rows(settings, star_height):
    """Determine the number of rows of stars that fit on the screen."""
    avaiable_space_y = (settings.screen_height - star_height)
    number_rows = int(avaiable_space_y / (2 * star_height))
    return number_rows


def get_number_stars_x(settings, star_width):
    """Determine the number of stars that fit in a row."""
    avaiable_space_x = settings.screen_width - star_width
    number_stars_x = int(avaiable_space_x / (2 * star_width))
    return number_stars_x


def create_star(settings, screen, stars, star_number, row_number):
    """Create a star and place it in the row."""
    star = Star(settings, screen)
    star_width = star.rect.width
    star_height = star.rect.height
    half_width = int(star_width / 2)
    random_number = randint(-half_width, half_width)
    star.x = star_width + 2 * star_width * star_number
    star.rect.x = star.x + random_number
    star.rect.y = star_height + 2 * star_height * row_number
    stars.add(star)


def create_stars(settings, screen, stars):
    """Create a full group of stars."""
    # Create a star and find the number of stars in a row.
    star = Star(settings, screen)
    number_stars_x = get_number_stars_x(settings, star.rect.width)
    number_rows = get_number_rows(settings, star.rect.height)

    # Create group of stars.
    for row_number in range(number_rows):
        for star_number in range(number_stars_x):
            create_star(settings, screen, stars, star_number, row_number)


def run():
    """Initialize pygame, settings and screen objects."""
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    pygame.display.set_caption('Stars')

    # Make a group to store stars.
    stars = Group()

    # Create group of start.
    create_stars(settings, screen, stars)

    # Main loop
    while True:
        check_events(settings, screen)
        update_screen(settings, screen, stars)


run()
