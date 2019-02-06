# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 09:29:04 2019

@author: 612436112
"""
### Task 1 #### 
#age = input("what is your age?")
#print(type(age))
#
#### task 2 ####
#
#age = int(input("what is your age?"))
#print(type(age))
#
#age = input("What’s your age? ")
#age_int = int(age)
#
#print(type(age_int))
#
#### task 3 ### 

#option = input("please input yes or no ")
#
#print(option[0])
#
#if option[0] == "y" or option[0] == "n":
#    print("good job. you know how to read!")
#else:
#    print("please try again")
#
#### task 4 ### 
#    
#threeLetter = input("what is a three letter word? ")
#
#if len(threeLetter) == 3:
#    print("yay")
#else:
#    print("that is not a three letter word")

### take 5 #### 
#choice = 0
#print("***choice****")
#print("1. Display my name")
#print("2. Display my age")
#print("3. Display my city")
#
#choice = input(‘What is your choice? ’)
#While choice < 1 or choice > 3:
#choice = int(input(‘What is your choice? ’))
#
#If choice == 1:
#print(‘Ms Wu’)
#Elif choice == 2:
#print(‘5 years old’)
#Elfi choice == 3:
#print(‘London’)

### take 6 #### 
print("***choice****")
print("1. Display my name")
print("2. Display my age")
print("3. Display my city")

choice = 0 

while True:
    try:
        while choice < 1 or choice > 3:
            choice = int(input("What is your choice? "))
        break
            
    except ValueError:
            print("please type a number!")
if choice == 1:
    print("Ms Wu")

elif choice == 2:
    print("5 years old")
   
elif choice == 3:
    print("London")
   
### take 7 #### 
#class Spam(object): 
#    def __init__(self, description, value):
#        if not description or value <=0:
#            raise ValueError
#        self.description = description
#        self.value = value
#        
#s = Spam("s", 0)
#print(s.value)