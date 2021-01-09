import pytest

def sum2nums(n1, n2):
    types_allowed = (int, float)
    assert type(n1) in types_allowed, 'only int/float allowed'
    assert type(n2) in types_allowed, 'only int/float allowed'
    return n1 + n2

def test_valid_values():
    assert sum2nums(3, -2) == 1
    # see https://stackoverflow.com/q/5595425
    from math import isclose
    assert isclose(sum2nums(-3.14, 2), -1.14)

def test_exception():
    with pytest.raises(AssertionError) as e:
        sum2nums('hi', 3)
    assert 'only int/float allowed' in str(e.value)

    with pytest.raises(AssertionError) as e:
        sum2nums(3.14, 'a')
    assert 'only int/float allowed' in str(e.value)

