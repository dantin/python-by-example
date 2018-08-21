
import pygame
import sys

from pygame.sprite import Group
from pygame.sprite import Sprite
from random import randint


class Settings():
    """A class that stores all the settings for the game."""

    def __init__(self):
        """Initialize the game's settings."""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Catcher settings
        self.catcher_speed_factor = 5
        self.catcher_width = 100
        self.catcher_height = 3
        self.catcher_color = (60, 60, 60)

        # Ball settings
        self.ball_drop_speed = 3


class Catcher(Sprite):
    """Catcher class."""

    def __init__(self, settings, screen):
        """Initialize the catcher and set its starting position."""
        super().__init__()
        self.settings = settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.color = settings.catcher_color

        # Create a catcher rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, settings.catcher_width,
                                settings.catcher_height)

        # Start catcher at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the catcher's center.
        self.center = float(self.rect.centerx)

        # Movement flag
        self.moving_left = False
        self.moving_right = False

    def update(self):
        """Move the catcher's position based on the movement flag."""
        # Update the catcher's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.catcher_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.settings.catcher_speed_factor

        # Update rect object from self.center.
        self.rect.centerx = self.center

    def draw_catcher(self):
        """Draw the catcher at its current location."""
        pygame.draw.rect(self.screen, self.color, self.rect)


class Ball(Sprite):
    """A class to represent a ball."""

    def __init__(self, settings, screen):
        """Initialize ball and set its starting position."""
        super().__init__()
        self.settings = settings
        self.screen = screen

        # Load the ball image and set its attribute.
        self.image = pygame.image.load('images/ball.bmp')
        self.rect = self.image.get_rect()

        screen_rect = screen.get_rect()
        self.rect.x = randint(0, screen_rect.width - self.rect.width)
        self.rect.y = 0

        self.y = float(self.rect.y)

    def blitme(self):
        """Draw the ball at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Move the ball down."""
        self.y += self.settings.ball_drop_speed
        self.rect.y = self.y


def check_keydown_events(event, settings, screen, catcher):
    """Respond to key presses."""
    if event.key == pygame.K_RIGHT:
        catcher.moving_right = True
    elif event.key == pygame.K_LEFT:
        catcher.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, catcher):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        catcher.moving_right = False
    elif event.key == pygame.K_LEFT:
        catcher.moving_left = False


def check_event(settings, screen, catchers):
    """Respond to key presses and mouse event."""
    # Get the only catcher.
    catcher = catchers.sprites()[0]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, catcher)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, catcher)


def update_screen(settings, screen, catchers, balls):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(settings.bg_color)
    for catcher in catchers.sprites():
        catcher.draw_catcher()
    balls.draw(screen)
    # Make the most recently drawn screen visible.
    pygame.display.flip()


def create_catcher(settings, screen, catchers):
    """Create a cathcer."""
    catcher = Catcher(settings, screen)
    catchers.add(catcher)


def create_ball(settings, screen, balls):
    """Create a ball."""
    ball = Ball(settings, screen)
    balls.add(ball)


def update_catcher(catchers):
    """Update positions of catcher."""
    catchers.update()


def update_ball(balls):
    """Update positions of balls."""
    # Update ball positions.
    balls.update()


def run():
    """Initialize pygame, settings, and screen object."""
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Catcher")

    # Make a group of catcher and a group of balls.
    catchers = Group()
    balls = Group()

    # Create ball and catcher.
    create_ball(settings, screen, balls)
    create_catcher(settings, screen, catchers)

    # Start the main loop for game.
    while True:
        check_event(settings, screen, catchers)
        update_catcher(catchers)
        update_ball(balls)
        update_screen(settings, screen, catchers, balls)


run()
