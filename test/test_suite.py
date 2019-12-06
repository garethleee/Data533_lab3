import unittest
import os
import sys
if os.path.dirname(os.getcwd()) not in sys.path:
    sys.path.append(os.path.dirname(os.getcwd()))

from account_module_test import TestAccount
from cnaccount_module_test import TestCnAccount
from usaccount_module_test import TestUsAccount



def testSuite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestAccount))
    suite.addTest(unittest.makeSuite(TestCnAccount))
    suite.addTest(unittest.makeSuite(TestUsAccount))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))

if __name__=='__main__':
    testSuite()
