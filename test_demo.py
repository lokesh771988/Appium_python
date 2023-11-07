import pytest

from readData import ReadConfig


def setup_function(function):
    print("running in functional level")


def teardown_function(function):
    print("closing tear down in function")


def setup_module(module):
    print("module level")


def teardown_module(module):
    print("closing tear down in module")


def test_demo1():
    print("Demo pytest", ReadConfig.getUrl())


def test_demo2():
    print("Demo pytest2")
