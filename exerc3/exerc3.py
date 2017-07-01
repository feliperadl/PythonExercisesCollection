'''
Python function, clip(lo, x, hi) that returns lo if x is less than lo; hi if x is greater than hi; and x otherwise. 
'''
def clip(lo, x, hi):
    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise
    '''
    return min(max(x, lo), hi)