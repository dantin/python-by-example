
import pygame
import sys

from pygame.sprite import Group
from pygame.sprite import Sprite


class Settings():
    """A class that stores all settings."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Raindrop settings
        self.raindrop_speed_factor = 1


class Raindrop(Sprite):
    """A class to represent a single raindrop."""

    def __init__(self, settings, screen):
        """Initialize raindrop and set its starting position."""
        super().__init__()
        self.settings = settings
        self.screen = screen

        # load raindrop image and set its rect attribute.
        self.image = pygame.image.load('images/raindrops.bmp')
        self.rect = self.image.get_rect()

        # Start each new raindrop near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the raindrop's exact position.
        self.y = float(self.rect.y)

    def blitme(self):
        """Draw the start at its current location."""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Return True if raindrop is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.top >= screen_rect.bottom:
            return True
        elif self.rect.top <= 0:
            return True

    def update(self):
        """Move the raindrop down."""
        self.y += self.settings.raindrop_speed_factor
        self.rect.y = self.y


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


def update_screen(settings, screen, raindrops):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(settings.bg_color)
    # Redraw all raindrops.
    raindrops.draw(screen)

    # Make the most recently drawn screen visible.
    pygame.display.flip()


def get_number_rows(settings, raindrop_height):
    """Determine the number of rows of raindrops that fit on the screen."""
    avaiable_space_y = (settings.screen_height - raindrop_height)
    number_rows = int(avaiable_space_y / (2 * raindrop_height))
    return number_rows


def get_number_raindrops_x(settings, raindrop_width):
    """Determine the number of raindrops that fit in a row."""
    avaiable_space_x = settings.screen_width - raindrop_width
    number_raindrops_x = int(avaiable_space_x / (2 * raindrop_width))
    return number_raindrops_x


def create_raindrop(settings, screen, raindrops, raindrop_number, row_number):
    """Create a draindrop and place it in the row."""
    raindrop = Raindrop(settings, screen)
    raindrop_width = raindrop.rect.width
    raindrop_height = raindrop.rect.height
    raindrop.x = raindrop_width + 2 * raindrop_width * raindrop_number
    raindrop.rect.x = raindrop.x
    raindrop.rect.y = raindrop_height + 2 * raindrop_height * row_number
    raindrop.y = float(raindrop.rect.y)
    raindrops.add(raindrop)


def create_raindrops(settings, screen, raindrops):
    """Create a full group of raindrops."""
    # Create a raindrop and find the number of raindrops in a row.
    raindrop = Raindrop(settings, screen)
    number_raindrops_x = get_number_raindrops_x(settings, raindrop.rect.width)
    number_rows = get_number_rows(settings, raindrop.rect.height)

    # Create group of raindrops.
    for row_number in range(number_rows):
        for raindrop_number in range(number_raindrops_x):
            create_raindrop(settings, screen, raindrops, raindrop_number, row_number)


def check_raindrops_edges(raindrops):
    """Respond appropriately if raindop have reached an edge."""
    # Get rid of raindrops that have disappeared.
    for raindrop in raindrops.copy():
        if raindrop.check_edges():
            raindrops.remove(raindrop)


def update_raindrops(raindrops):
    """Update the position of all raindrops."""
    check_raindrops_edges(raindrops)
    raindrops.update()



def run():
    """Initialize pygame, settings and screen objects."""
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    pygame.display.set_caption('Raindrops')

    # Make a group to store raindrops.
    raindrops = Group()

    # Create group of raindrops.
    create_raindrops(settings, screen, raindrops)

    # Main loop
    while True:
        check_events(settings, screen)
        update_raindrops(raindrops)
        update_screen(settings, screen, raindrops)


run()
