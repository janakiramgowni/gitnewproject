import unittest
class paymentTest(unittest.TestCase):
    def test_paymentindollar(self):
        print("this is payment in dollar")
        self.assertTrue(True)

    def test_paymentinrupees(self):
        print("this is payment in rupees")
        self.assertTrue(True)


if __name__=="__main__":
    unittest.main()