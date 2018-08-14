
sandwich_orders = ['pastrami', 'tuna', 'pastrami', 'beef', 'pork', 'pastrami', 'chicken', 'egg']
finished_sandwiches = []

print('deli has run out of pastrami')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_order = sandwich_orders.pop()

    print('I made you ' + current_order + ' sandwich.')
    finished_sandwiches.append(current_order)

print('\nSandwiches that have been made:')
for sandwich in finished_sandwiches:
    print(sandwich + ' sandwich')
