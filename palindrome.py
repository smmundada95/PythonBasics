def reverse_string(s):
    ''' (str) -> str

    >>>'abc'
    'cba'

    Returns the reverse of string s.

    '''
    reversed_s = ''
    for i in range(len(s)):
        reversed_s = reversed_s + s[len(s) - 1 - i]
   
    return reversed_s

def is_palindrome_a1(s):
    ''' (str) -> bool

    Returns true if and only if s is a palindrome.
    '''
    reversed_s = reverse_string(s)
       
    return reversed_s == s

def is_palindrom_a2(s):
    ''' (str) -> bool

    Returns true if and only if s is a palindrome.
    '''
    length = len(s)
    first_half = ''
    second_half = ''
    if(length % 2 == 0):
        first_half = s[:length//2]
        second_half = s[length//2:]
    else:
        first_half = s[:length//2]
        second_half = s[length//2 + 1:]

    reversed_second_half = reverse_string(second_half)
    return reversed_second_half == first_half

def is_palindrome_a3(s):
    ''' (str) -> bool

    Returns true if and only if s is a palindrome.
    '''
    length = len(s)
    for i in range(len(s)//2):
        if s[i] != s[len(s) - 1 - i]:
            return False

    return True

def is_panlindrome_a3v2(s):
    ''' (str) -> bool

    Returns true if and only if s is a palindrome.
    '''
    # s[i] and s[j] are the next pair of characters to compare.
    i = 0
    j = len(s) - 1

    while i < j and s[i] == s[j]:
        i = i + 1
        j = j - 1

    # If we exited because we successfully compared all pairs of characters,
    # then j <= i.
    return j <= i
    
