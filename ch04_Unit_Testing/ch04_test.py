# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 10:00:22 2019

@author: 612436112
"""

import unittest
from ch04_mandy import is_prime

class prime_test(unittest.TestCase):
    def  test_prime(self):
        self.assertTrue(is_prime(5.3))
    
if __name__ == "__main__":
    unittest.main()
        
        
#unittest.TestCase.assertTrue(is_prime(5))
        
        