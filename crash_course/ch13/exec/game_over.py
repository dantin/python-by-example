
import pygame
import sys

from pygame.sprite import Group
from pygame.sprite import Sprite
from random import randint
from time import sleep


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
        self.catcher_limit = 3

        # Ball settings
        self.ball_drop_speed = 3


class Catcher():
    """Catcher class."""

    def __init__(self, settings, screen):
        """Initialize the catcher and set its starting position."""
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
        self.screen_rect = screen.get_rect()

        # Load the ball image and set its attribute.
        self.image = pygame.image.load('images/ball.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = randint(0, self.screen_rect.width - self.rect.width)
        self.rect.y = 0

        self.y = float(self.rect.y)

    def blitme(self):
        """Draw the ball at its current location."""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Return True if ball is at the edge of screen."""
        if self.rect.bottom >= self.screen_rect.bottom:
            return True

    def update(self):
        """Move the ball down."""
        self.y += self.settings.ball_drop_speed
        self.rect.y = self.y


class GameStats():
    """Track statistics for the game."""

    def __init__(self, settings):
        """Initialize statistics."""
        self.settings = settings
        self.catchers_left = settings.catcher_limit
        # Start catcher game in an active state.
        self.game_active = True


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


def check_event(settings, screen, catcher):
    """Respond to key presses and mouse event."""
    # Get the only catcher.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, catcher)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, catcher)


def update_screen(settings, screen, balls, catcher):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(settings.bg_color)
    catcher.draw_catcher()
    balls.draw(screen)
    # Make the most recently drawn screen visible.
    pygame.display.flip()


def create_ball(settings, screen, balls):
    """Create a ball."""
    ball = Ball(settings, screen)
    balls.add(ball)


def update_catcher(catcher):
    """Update positions of catcher."""
    catcher.update()


def ball_missing(settings, screen, stats, balls):
    """Respond to ball hit the bottom."""
    if stats.catchers_left > 0:
        # Decrement catchers_left.
        stats.catchers_left -= 1

        # Empty balls.
        balls.empty()

        # Create a new ball.
        create_ball(settings, screen, balls)

        # Pause
        sleep(0.5)
    else:
        stats.game_active = False


def check_ball_missing(settings, screen, stats, balls):
    """Check if ball have reached the bottom of the screen."""
    for ball in balls.sprites():
        if ball.check_edges():
            ball_missing(settings, screen, stats, balls)
            break


def update_ball(settings, screen, stats, balls, catcher):
    """Update positions of balls."""
    # Update ball positions.
    balls.update()

    check_ball_missing(settings, screen, stats, balls)

    check_ball_catcher_collisions(settings, screen, balls, catcher)


def check_ball_catcher_collisions(settings, screen, balls, catcher):
    """Respond to ball-catcher collisions."""
    if pygame.sprite.spritecollideany(catcher, balls):
        balls.empty()
        create_ball(settings, screen, balls)


def run():
    """Initialize pygame, settings, and screen object."""
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Catcher")

    # Create an instance to store game statistics.
    stats = GameStats(settings)

    # Make a catcher and a group of balls.
    catcher = Catcher(settings, screen)
    balls = Group()

    # Create ball and catcher.
    create_ball(settings, screen, balls)

    # Start the main loop for game.
    while True:
        check_event(settings, screen, catcher)

        if stats.game_active:
            update_catcher(catcher)
            update_ball(settings, screen, stats, balls, catcher)

        update_screen(settings, screen, balls, catcher)


run()
