import re
import pytest

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


def space_compress(input_string):
    assert isinstance(input_string, str), "Expected str but got {} instead".format(type(input_string))
    compressed_string = re.sub(r'\s+', ' ', input_string)
    return compressed_string.strip()


@pytest.mark.xfail(reason="This test is expected to fail")
def test_example():
    assert 1 + 1 == 3


@pytest.mark.parametrize("input_value, expected_output", [
    (2, 4),
    (3, 9),
    (4, 16),
    (5, 25)
])
def test_square(input_value, expected_output):
    assert input_value**2 == expected_output
