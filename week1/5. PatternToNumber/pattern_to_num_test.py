from PatternToNumber.pattern_to_num import letter_to_num


def test_letter_to_num():
    assert letter_to_num('a') == 0, "A should be 0"


if __name__ == "__main__":
    test_letter_to_num()
    print("Everything passed")
