
import pygal

from die import Die


def get_max_result(dices):
    """Get max result of dices list."""
    max_result = 1
    for die in dices:
        max_result *= die.num_sides
    return max_result


def get_roll_result(dices):
    """Get roll results."""
    result = 1
    for die in dices:
        result *= die.roll()
    return result


# Create two D6s.
dices = [Die(), Die()]

max_result = get_max_result(dices)

# Make some rolls, and store results in a list.
results = []
for roll_num in range(50000):
    result = get_roll_result(dices)
    results.append(result)

# Analyze the results.
frequencies = []
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
hist = pygal.Bar()

hist.title = 'Results of rolling two D6 1000 times.'
hist.x_labels = [str(x) for x in range(1, max_result+1)]
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('Two D6', frequencies)
hist.render_to_file('die_visual.svg')
