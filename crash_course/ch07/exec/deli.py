
sandwich_orders = ['tuna', 'beef', 'pork', 'chicken', 'egg']
finished_sandwiches = []

while sandwich_orders:
    current_order = sandwich_orders.pop()

    print('I made you ' + current_order + ' sandwich.')
    finished_sandwiches.append(current_order)

print('\nSandwiches that have been made:')
for sandwich in finished_sandwiches:
    print(sandwich + ' sandwich')
