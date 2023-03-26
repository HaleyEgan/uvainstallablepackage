import pytest

import sys
#sys.path.append("/uvainstallablepackage/shared")
sys.path.append(".")

import shared as sh
sh.afunction()

def space_compress(input_string):
    if not isinstance(input_string, str):
        return "Expected string but got {}".format(type(input_string))

    compressed_string = " ".join(input_string.split())
    return compressed_string.replace("\n", " ")


@pytest.mark.xfail(reason="This test is expected to fail")
def test_fail_example():
    assert 1 + 1 == 3

@pytest.mark.skip(reason="This tests is temporarily skipped")
def test_skip_example():
    print("Skip")

@pytest.mark.skipif(sys.platform!='darwin', reason="Test is only meant to run on your platform")
def test_skipif_example():
    print("My platform is", sys.platform)
    assert False, "This test is expected to fail"

@pytest.mark.parametrize("input_value, expected_output", [
    (2, 4),
    (3, 9),
    (4, 16),
    (5, 25)
])
def test_square(input_value, expected_output):
    assert input_value**2 == expected_output
