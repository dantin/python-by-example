
alien_o = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print('Original x-position: ' + str(alien_o['x_position']))

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_o['speed'] == 'slow':
    x_increment = 1
elif alien_o['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_o['x_position'] = alien_o['x_position'] + x_increment

print('New x-position: ' + str(alien_o['x_position']))
