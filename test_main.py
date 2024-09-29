from main import mul


def test_mul():
    assert mul(1, 2) == 2
    assert mul(2, 2) == 4
    assert mul(3, 2) == 6
    assert mul(4, 2) == 8


if __name__ == "__main__":
    test_mul()
