
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

users = ['david', 'jen']
for user in users:
    if user in favorite_languages.keys():
        print('Thanks ' + user.title() + ' for taking the poll.')
    else:
        print(user.title() + ', please to take the poll.')
