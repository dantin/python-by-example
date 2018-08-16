
from random import randint


class Die():
    """A simple Dice class."""

    def __init__(self, sides=''):
        """Initialize using attributes."""
        if sides:
            self.sides = sides
        else:
            self.sides = 6

    def roll_die(self):
        """Simulate roll dice."""
        x = randint(1, self.sides)
        print('point: ' + str(x))



def roll(sides, times):
    """Make n-sided die and roll it m times."""
    print('\nMake ' + str(sides) +'-sided die.')
    die = Die(sides)
    print('Roll it ' + str(times) + ' times.')
    for _ in range(times):
        die.roll_die()


roll(6, 10)
roll(10, 20)
