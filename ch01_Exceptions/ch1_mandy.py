# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 09:58:18 2019

@author: 612436112
"""

#### Task 1 ###### 
try: 
    f=open("testfile.txt")
except Exception:
    print("ERROR")
        
try: 
    f=open("testfile.txt")
    s1 = not_exist
except Exception:
    print("sorry this file does not exist")
    
#### Task 2 ###### 
try: 
    f=open("testfile.txt")
    s1 = not_exist
except FileNotFoundError:
    print("sorry this file does not exist")
except Exception: 
    print("sorry something went wrong")

#### Task 3 ######

try: 
    f = open("testfile.txt")
    s1 = not_exist 
except Exception as e:
    print(e)

#### Task 4 ######
try: 
    f = open("testfile.txt")
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()

#### Task 5 ######
try: 
    f = open("testfile.txt")
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("this is the finally printing")
    
#### Task 6 ######
try: 
    f = open("testfile.txt")
    if f.name == "testfile.txt":
        raise Exception
except Exception:
    print("file name is the same")
    


