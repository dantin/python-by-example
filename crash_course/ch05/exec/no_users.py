
# users = ['eric', 'david', 'admin']
users = []


if users:
    for u in users:
        if u == 'admin':
            print('Hello ' + u + ', would you like to see a status report?')
        else:
            print('Hello ' + u + ', thank you for logging in again.')
else:
    print('We need to find some users!')
