import pytest


@pytest.fixture
def setup():
    print("executing first")
    yield
    print("executing last")


def test_fixtureDemo(setup):
    print("i am the main line for this program")


def test_gmail():
    assert True
