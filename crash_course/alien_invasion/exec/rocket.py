
import pygame
import sys


class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 400
        self.screen_height = 300
        self.bg_color = (230, 230, 230)

        self.rocket_speed_factor= 1.5


class Rocket():
    """Rocket class."""

    def __init__(self, settings, screen):
        """Initialize Rocket using parameters."""
        self.settings = settings
        self.screen = screen

        # load the rocket image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new Rocket at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value to the rocket's center.
        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)

        # Movement flag
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the rocket's position based on the movement flag."""
        if self.moving_left and self.rect.left > 0:
            self.center -= self.settings.rocket_speed_factor
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.rocket_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.bottom -= self.settings.rocket_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.settings.rocket_speed_factor

        # Update rect object from self.center.
        self.rect.centerx = self.center
        self.rect.bottom = self.bottom

    def blitme(self):
        """Draw the rocket at its current location."""
        self.screen.blit(self.image, self.rect)


def check_keydown_events(event, rocket):
    """Respond to key presses."""
    if event.key == pygame.K_LEFT:
        rocket.moving_left = True
    elif event.key == pygame.K_RIGHT:
        rocket.moving_right = True
    elif event.key == pygame.K_UP:
        rocket.moving_up = True
    elif event.key == pygame.K_DOWN:
        rocket.moving_down = True


def check_keyup_events(event, rocket):
    """Respond to key releases."""
    if event.key == pygame.K_LEFT:
        rocket.moving_left = False
    elif event.key == pygame.K_RIGHT:
        rocket.moving_right = False
    elif event.key == pygame.K_UP:
        rocket.moving_up = False
    elif event.key == pygame.K_DOWN:
        rocket.moving_down = False


def check_events(rocket):
    """Respond to key presses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, rocket)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, rocket)


def update_screen(settings, screen, rocket):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(settings.bg_color)
    rocket.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()


def run():
    """Initialize pygame, settings and screen objects."""
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    pygame.display.set_caption('Rocket')

    rocket = Rocket(settings, screen)

    # Main Loop
    while True:
        check_events(rocket)
        rocket.update()
        update_screen(settings, screen, rocket)


run()
