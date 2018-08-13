
favorite_numbers = {
    'david': [43, 2],
    'jiayi': [17],
    'zhiyuan': [5, 7, 11],
    'zhenhua': [3],
}

for name, numbers in favorite_numbers.items():
    print('\n' + name.title() + ' likes:')
    for num in numbers:
        print('\t' + str(num))
