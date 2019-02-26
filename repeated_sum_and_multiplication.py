def dig_sum(n):
    total = 0
    while n:
        total = total + n%10
        n = n // 10
    return total
    
def dig_mult(n):
    mult = 1
    while n:
        mult = mult * (n%10)
        n = n // 10
    return mult

def repeated_sum_and_multiply(num):
    """ (int) -> int

    This function repeatedly sums the digits of num till it reaches a single digit sum.
    Upon reaching the single digit sum it multiplies the digits of the previous sum.

    Lets take 846930887 as example ,846930887 breaks into 8+4+6+9+3+0+8+8+7=53 then 53 breaks into 5+3=8. 8 is a single digit sum.
    But we have to multiply the at last step before  so 5*3=15
    So , output Becomes 15

    >>> repeated_sum_and_multiply(846930887)
    15
    >>> repeated_sum_and_multiply(19)
    0
    >>> repeated_sum_and_multiply(129)
    2
    """
    
    digit_sum = dig_sum(num)
    previous_sum = digit_sum
    while digit_sum > 9:
        previous_sum = digit_sum
        digit_sum = dig_sum(digit_sum)
        num = num // 10
    final = dig_mult(previous_sum)
    return final

import doctest
doctest.testmod()
