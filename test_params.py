import pytest


def getData():
    return [
        ('lokesh', '12345'),
        ('loki', '1234')
    ]


@pytest.mark.parametrize("username, password", getData())
def test_login(username, password):
    print("userName====", username, "------", "password====", password)
