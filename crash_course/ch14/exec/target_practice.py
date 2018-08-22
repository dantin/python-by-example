
import pygame
import sys

from pygame.sprite import Sprite
from pygame.sprite import Group


class Settings():
    """A class to store all settings."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 400
        self.screen_height = 300
        self.bg_color = (255, 255, 255)

        self.rocket_speed_factor= 1.5

        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_limit = 3


class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, settings, screen, ship):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        self.rect.centery = ship.rect.centery
        self.rect.right = ship.rect.right

        # Store the bullet's position as a decimal value.
        self.x = float(self.rect.x)

        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed_factor

    def update(self):
        """Move the bullet right the screen."""
        # Update the decimal position of the bullet.
        self.x += self.speed_factor
        # Update the rect position.
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)


class Airplane():
    """Airplane class."""

    def __init__(self, settings, screen):
        """Initialize Airplane using parameters."""
        self.settings = settings
        self.screen = screen

        # load the airplane image and get its rect.
        self.image = pygame.image.load('images/airplane.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new airplane at the left center of the screen.
        self.rect.left = 0
        self.rect.centery= self.screen_rect.centery

        # Store a decimal value to the airplane's center.
        self.y = float(self.rect.y)

        # Movement flag
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the airplane's position based on the movement flag."""
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed_factor

        # Update rect object from self.center.
        self.rect.y = self.y

    def blitme(self):
        """Draw the airplane at its current location."""
        self.screen.blit(self.image, self.rect)


def fire_bullet(settings, screen, airplane, bullets):
    """Fire a bullet if limit not reached yet."""
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < settings.bullets_limit:
        new_bullet = Bullet(settings, screen, airplane)
        bullets.add(new_bullet)


def check_keydown_events(event, settings, screen, airplane, bullets):
    """Respond to key presses."""
    if event.key == pygame.K_UP:
        airplane.moving_up = True
    elif event.key == pygame.K_DOWN:
        airplane.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(settings, screen, airplane, bullets)


def check_keyup_events(event, airplane):
    """Respond to key releases."""
    if event.key == pygame.K_UP:
        airplane.moving_up = False
    elif event.key == pygame.K_DOWN:
        airplane.moving_down = False


def check_events(settings, screen, airplane, bullets):
    """Respond to key presses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, airplane, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, airplane)


def update_screen(settings, screen, airplane, bullets):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(settings.bg_color)
    airplane.blitme()

    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Make the most recently drawn screen visible.
    pygame.display.flip()


def update_bullets(bullets):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet position.
    bullets.update()

    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.left > bullet.screen_rect.right:
            bullets.remove(bullet)


def run():
    """Initialize pygame, settings and screen objects."""
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    pygame.display.set_caption('Airplane')

    airplane = Airplane(settings, screen)
    # Make a group to store bullets in.
    bullets = Group()

    # Main Loop
    while True:
        check_events(settings, screen, airplane, bullets)
        airplane.update()
        update_bullets(bullets)
        update_screen(settings, screen, airplane, bullets)


run()
