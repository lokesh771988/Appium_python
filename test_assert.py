import pytest


def test_validate_title():
    expect_result = "google"
    actual_result = "gmail"

    if actual_result == expect_result:
        print("test pass")
        # assert True, "Test case pass"
        # assert actual_result == expect_result
        assert expect_result in actual_result
    else:
        print("test faile")
        assert False, "Test case Fail"
