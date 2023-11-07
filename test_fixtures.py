import pytest


@pytest.fixture(scope="module")
def setup():
    print("setup module level")
    yield
    print("teardown module level")


@pytest.fixture(scope="function")
def before():
    print("setup function level")
    yield
    print("teardown function level")


@pytest.mark.usefixtures("setup", "before")
@pytest.mark.sanity
def test_addUser():
    print("user is added")


@pytest.mark.usefixtures("setup", "before")
@pytest.mark.regression
def test_addUser1():
    print("user is added1")