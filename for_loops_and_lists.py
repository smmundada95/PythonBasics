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

