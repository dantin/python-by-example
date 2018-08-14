
prompt = '\nHow old are you? (Enter \'quit\' to quit the loop) '

active = True
while active:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        ticket = 0
    elif age <= 12:
        ticket = 10
    elif age > 12:
        ticket = 15

    print('The cost of your movie ticket is $' + str(ticket) + '.')
