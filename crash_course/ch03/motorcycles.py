
motocycles = ['honda', 'yamaha', 'suzuki']
print('# original list')
print(motocycles)

# modify element in a list
# motocycles[0] = 'ducati'
# print(motocycles)

# appending element to the end of a list
print('# append element at the end')
motocycles.append('ducati')
print(motocycles)

# insert element into a list
print('# insert element ahead')
motocycles.insert(0, 'ducati')
print(motocycles)

print('# removing an item')
del motocycles[0]
print(motocycles)

print('# pop an item at the end')
popped_motorcycle = motocycles.pop()
print(motocycles)
print('popped motorcycle:', popped_motorcycle)
