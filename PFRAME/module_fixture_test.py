import pytest


@pytest.mark.usefixtures("setup")
class Test_Example:

    def test_m1(self):
        print("one")

    def test_m2(self):
        print("two")

    def test_m3(self):
        print("three")
