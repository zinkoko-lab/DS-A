from src import sum


def test_sum_numbers():
    result1, result2 = sum.sum_numbers(1, 2)
    assert result1 == 3
    assert result2 == 1
