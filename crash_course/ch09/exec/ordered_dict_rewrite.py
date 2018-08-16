
from collections import OrderedDict


glossary = OrderedDict()
glossary['for'] = 'for statement'
glossary['list'] = 'list function'
glossary['*'] = 'multiply operator'

for k, v in glossary.items():
    print(k + ': ' + v)
