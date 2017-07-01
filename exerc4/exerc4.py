'''
Python function, odd, that takes in one number and returns True when the number is odd and False otherwise. 
'''
def odd(x):
    '''
    x: int or float.

    returns: True if x is odd, False otherwise
    '''
    return not (x % 2 == 0)