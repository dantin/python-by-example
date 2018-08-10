
places = ['shiyan', 'shanghai', 'chicago', 'paris', 'berlin']

print('original list')
print(places)
print('alphabetical order')
print(sorted(places))
print('original list')
print(places)
print('reverse alphabetical order')
print(sorted(places, reverse=True))
print('original list')
print(places)

# reversed list
places.reverse()
print('reversed list')
print(places)
# roll back
places.reverse()
print('original list')
print(places)

# sorted list
places.sort()
print('sorted list')
print(places)

places.sort(reverse=True)
print('reverse sorted list')
print(places)
