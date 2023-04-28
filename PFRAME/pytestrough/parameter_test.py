import pytest


@pytest.mark.parametrize("num,result", [(1, 10), (2, 20), (3, 30), (4, 40), (5, 50)])
def test_calculation(num, result):
    assert 10 * num == result
