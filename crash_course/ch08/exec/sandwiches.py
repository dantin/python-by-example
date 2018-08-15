
def show_sandwiche(*items):
    """Print a summary of sandwich that is being ordered."""
    print('\nSummary of ordered sandwich:')
    for item in items:
        print('- ' + item)


show_sandwiche('mushrooms')
show_sandwiche('pepperoni', 'extra cheese')
show_sandwiche('beef', 'green peppers', 'mushrooms')
