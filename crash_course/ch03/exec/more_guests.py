
guests = ['weiying', 'zhenhua', 'jiayi']
print(guests)

new_one = 'zhiyuan'
print(guests[0].title() , 'can\'t make it.')
print('Invite' , new_one, 'instead.')

guests.pop(0)
guests.insert(0, new_one)
print(guests)

print('Add more...')
guests.insert(0, 'juemin')
guests.insert(len(guests)//2, 'chengjie')
guests.append('pingping')
print(guests)
