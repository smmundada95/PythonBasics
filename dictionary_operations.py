def invert_dictionary(d):
    ''' (dict of str:str)-> dict of str:list of str

    Takes a dictionary as a parameter and
    Returns an inverted dictionary.

    To make sure no items are missed, maps values of the dictionary
    paramter to a list of keys.

    >>>d = {'watermelon': 'green', 'pomegranate': 'red',
    'peach': 'orange', 'cherry': 'red', 'pear': 'green',
    'banana': 'yellow', 'plum': 'purple', 'orange': 'orange'}
    >>>invert = invert_dictionary(d)
    >>>invert
    {'orange': ['peach', 'orange'], 'purple': ['plum'],
    'green': ['watermelon', 'pear'],'yellow': ['banana'],
    'red': ['cherry', 'pomegranate']}
    '''
    inverted_d = {}
    for key in d:
        value = d[key]
        if value in inverted_d:
            inverted_d[value].append(key)
        else:
            inverted_d[value] = []
            inverted_d[value].append(key)

    return inverted_d
