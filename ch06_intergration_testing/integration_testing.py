# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 10:44:46 2019

@author: Katharina
"""
from business_phonebook_functions import *
import sqlite3



class test_phonebook_functions():
    
    def test_getdb(self):
        self.connected = getdb()
        
        if self.connected:
            self.connected = True
            return self.connected
        else:
            self.connected = False
            print('Database not connecting')
            return self.connected
        
        
    def test_create_business_name_list(self):
        self.results = create_business_name_list()
        
        if self.results:
            self.results = True
            return self.results
        else:
            self.results = False
            return self.results
        
        
    def run_tests(self):
        print(self.test_getdb())
        print(self.test_create_business_name_list())

if __name__ == "__main__":
    newTest = test_phonebook_functions()
    newTest.run_tests()