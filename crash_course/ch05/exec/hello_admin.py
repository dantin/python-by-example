
users = ['eric', 'david', 'admin']


for u in users:
    if u == 'admin':
        print('Hello ' + u + ', would you like to see a status report?')
    else:
        print('Hello ' + u + ', thank you for logging in again.')
