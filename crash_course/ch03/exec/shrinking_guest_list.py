
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

print('new dinner table won\'t arrive in time.')

while(len(guests) > 2):
    p = guests.pop()
    print('sorry letter to', p)

print(guests)

# can't work
#
#for _ in guests:
#    del guests[0]

while(len(guests) > 0):
    del guests[0]

print('clean up', guests)
