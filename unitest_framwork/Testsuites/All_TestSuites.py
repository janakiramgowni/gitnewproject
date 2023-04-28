import unittest

from Package1.Tc_loginTest import LoginTest
from Package1.TC_signupTest import signupTest

from Package2.TC_paymentTest import paymentTest
from Package2.TC_paymentreturnTest import paymentReturnTest

# get all tests from Logintest,signuptest,paymentTest,paymentreturnTest
tc1=unittest.TestLoader().loadTestsFromTestCase(loginTest)
tc2=unittest.TestLoader().loadTestsFromTestCase(signupTest)
tc3=unittest.TestLoader().loadTestsFromTestCase(paymentTest)
tc4=unittest.TestLoader().loadTestsFromTestCase(paymentReturnTest)
# creating test suites
sanityTestSuite=unittest.TestSuite([tc1,tc2])  # sanity test suite
functionalTestSuite=unittest.TestSuite([tc3,tc4])  # functional test suite
masterTestSuite=unittest.TestSuite([tc1,tc2,tc3,tc4])   # master test Suite
unittest.TextTestRunner.run(sanityTestSuite)

unittest.TextTestRunner.run(functionalTestSuite)
unittest.TextTestRunner(verbosity=2).run(masterTestsuite)


