import unittest

class signupTest(unittest.TestCase):
    def test_signupbyemail(self):
        print("this is login by signupemail test")
        self.assertTrue(True)
    def test_signupbyfacebook(self):
        print("this is login by signupfacebook test")
        self.assertTrue(True)
    def test_signupbytwitter(self):
        print("this is login by signupTwitter test")
        self.assertTrue(True)
if __name__=="__main__":
    unittest.main()