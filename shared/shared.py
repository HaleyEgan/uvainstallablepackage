import re

def afunction():
    print("This is the installed function")

def clean_string(str_word):
    """
    INPUTS:
    str_word     string string contining several words to clean
    RETURNS:
    string       the string after removal of extra spaces, punctuation and lowercasing
    """
    str_word = re.sub(r'\W+', ' ', str_word)
    assert isinstance(str_word, str), "String expected but recieved type {} instead".format(type(str_word))

    return str_word.strip()

import re
def space_compress(input_string):
    assert isinstance(input_string, str), "Expected str but got {} instead".format(type(input_string))
    compressed_string = re.sub(r'\s+', ' ', input_string)
    return compressed_string.strip()
