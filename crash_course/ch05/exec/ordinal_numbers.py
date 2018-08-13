
numbers = [x for x in range(1, 10)]
for n in numbers:
    if n == 1:
        suffix = 'st'
    elif n == 2:
        suffix = 'nd'
    elif n == 3:
        suffix = 'rd'
    else:
        suffix = 'th'
    print(str(n) + suffix)
