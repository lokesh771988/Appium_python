import pytest


@pytest.mark.skip
def test_skip():
    print("skip this function")


def test_add():
    print("add user")