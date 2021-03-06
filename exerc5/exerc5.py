'''
Python function isVowel2(char) that returns True if char is a vowel ('a', 'e', 'i', 'o', or 'u'), and False otherwise. 
You can assume that char is a single letter of any case (ie, 'A' and 'a' are both valid). 
'''
def isVowel2(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    return char in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']