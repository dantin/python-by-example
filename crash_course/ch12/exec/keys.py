
import pygame
import sys


def run():
    """Initialize pygame, settings, and screen object."""
    pygame.init()
    screen = pygame.display.set_mode((300, 200))
    pygame.display.set_caption('Keyboard Test')

    # main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print('KEY pressed is ' + str(event.key) + '.')

        # Make the most recently drawn screen visible.
        pygame.display.flip()


run()
