
prompt = '\Enter a series of pizza toppings '
prompt += '\nuntil you enter \'quit\' value. '

active = True
while active:
    topping = input(prompt)

    if topping == 'quit':
        active = False
    else:
        print('I\'ll add ' + topping + ' to your pizza.')
