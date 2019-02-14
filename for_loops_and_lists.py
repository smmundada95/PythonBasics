def count_adjacent_repeats(s):
    '''(str) -> int

    Return the number of occurrences of a character
    and an adjacent character being the same.'''

    repeats = 0
    
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            repeats = repeats + 1

    return repeats
        
        
def shift_left(L):
    ''' (list) -> NoneType

    Shift each item in L one position to the left
    and shift the first item to the last position.

    '''
    temp = L[0]
    for i in range(1, len(L)):
        L[i - 1] = L[i] 

    L[-1] = temp

def shift_right(L):
    last_item = L[-1]

    for i in range(1, len(L)):
        L[len(L) - i] = L[len(L) - i - 1]

    L[0] = last_item
    
    

def add_lists(list1, list2):
    ''' (list of number, list of number) -> list of number

    Return a new list in which each item is the sum of the
    corresponding position of list1 + list2.

    '''

    len_of_list1 = len(list1)
    len_of_list2 = len(list2) 
    len_of_list3 = len_of_list1 + len_of_list2
    list3 = []

    if len_of_list1 > len_of_list2:
        for i in range(len_of_list2):
            list3.append(list1[i] + list2[i])
        for j in range(len_of_list2, len_of_list1):
            list3.append(list1[j])
    elif len_of_list2 > len_of_list1:
        for i in range(len_of_list1):
            list3.append(list1[i] + list2[i])
        for j in range(len_of_list1, len_of_list2):
            list3.append(list2[j])
    else:
        for i in range(len_of_list1):
            list3.append(list1[i] + list2[i])

    return list3

def count_matches(s1, s2):
    num_matches = 0
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            num_matches = num_matches + 1

    return num_matches

def make_pairs(list1, list2):
    pairs = []
    for i in range(len(list1)):
        inner_list = []
        inner_list.append(list1[i])
        inner_list.append(list2[i])
    pairs.append(inner_list)

    return pairs


def smaller_of_largest(L1, L2):
    '''(list of int, list of int) -> int

    Return the smaller of the largest value in L1 and the large    st value inL2.

    Precondition: L1 and L2 are not empty.

    >>> smaller_of_largest([1, 4, 0], [3, 2])
    3
    >>> smaller_of_largest([4], [9, 6, 3])
    4
    '''

    return min(max(L1), max(L2))

def gather_every_nth(L, n):
    '''(list, int) -> list

    Return a new list containing every n'th element in L, starting at index 0.

    Precondition: n >= 1

    >>> gather_every_nth([0, 1, 2, 3, 4, 5], 3)

    [0, 3]
    >>> gather_every_nth(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'], 2)
   ['a', 'c', 'e', 'g', 'i']
   '''
    result = []
    i = 0
    while i < len(L):
        result.append(L[i])
        i = i + n 

    return result

def add_to_letter_counts(d, s):
    '''(dict of {str: int}, str) -> NoneType

    d is a dictionary where the keys are single-letter strings and the values
    are counts.

    For each letter in s, add to that letter's count in d.

    Precondition: all the letters in s are keys in d.

    >>> letter_counts = {'i': 0, 'r': 5, 'e': 1}
    >>> add_to_letter_counts(letter_counts, 'eerie')
    >>> letter_counts
    {'i': 1, 'r': 6, 'e': 4}
    '''
    for c in s:
        d[c] = d[c] + 1

