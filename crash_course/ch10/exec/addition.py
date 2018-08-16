import sys

def parse_int(text):
    """Pare input 'text' into numerical int number."""
    try:
        num = int(text)
    except (TypeError, ValueError):
        return '', False
    else:
        return num, True


def get_number(message, flag='q'):
    """Get input number until success."""
    ok = False
    while not ok:
        text = input(message)
        if text == flag:
            return '', True
        num, ok = parse_int(text)
        if not ok:
            print('Wrong input, please enter again!')
    return num, False


print('Give me two numbers and I\'ll sum them for you.')
lhs, exit = get_number('First Number: ')
if exit:
    sys.exit(0)
rhs, exit = get_number('Second Number: ')
if exit:
    sys.exit(0)

result = lhs + rhs
print('sum: ' + str(result))
