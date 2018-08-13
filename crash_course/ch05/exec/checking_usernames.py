
current_users = ['david', 'john', 'bob', 'alice', 'zoe']
new_users = ['jeff', 'bob', 'frank']

for user in new_users:
    if user.lower() in current_users:
        print(user + ' need to enter a new username')
    else:
        print(user + ' is available')
