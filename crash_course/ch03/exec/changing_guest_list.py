
def show(items):
    for item in items:
        print('invitation to', item)

guests = ['weiying', 'zhenhua', 'jiayi']
show(guests)

new_one = 'zhiyuan'
print(guests[0].title() , 'can\'t make it.')
print('Invite' , new_one, 'instead.')

guests.pop(0)
guests.insert(0, new_one)
show(guests)
