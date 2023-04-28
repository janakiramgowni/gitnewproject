import unittest

class Test(unittest.TestCase):
    def testname(self):
        list=["python","java","selenium"]
        #self.assertIn("python",list) #passed
        #self.assertIn("rubby", list) #failed
        #self.assertNotIn("python",list)  #failed
        self.assertNotIn("Rubby",list) #pass

if __name__=="__main__":
    unittest.main()