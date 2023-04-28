import pytest

# for execting before once after onece @pytest.fixture(scope='class')
@pytest.fixture()
def setup():
    print("first")
    yield
    print("last")