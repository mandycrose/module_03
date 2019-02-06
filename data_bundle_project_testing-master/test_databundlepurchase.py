# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 13:53:18 2018

@author: 612383461
"""

from functions_databundlepurchase import DataBundlePurchase

#Test call to programme:
print ('TEST EXAMPLE 1')
#database input, you will still need to check user pin
result = DataBundlePurchase('1234', 60.55,)
print ('-----\nResult:', result)
print ('-' * 50, '\n')

print ('TEST EXAMPLE 2')
result = DataBundlePurchase('2345', -22.00)
print ('-----\nRESULT:', result)
print ('-' * 50, '\n')

print ('TEST EXAMPLE 3')
result = DataBundlePurchase('3456', 17.55)
print ('-----\nRESULT:', result)
print ('-' * 50, '\n')