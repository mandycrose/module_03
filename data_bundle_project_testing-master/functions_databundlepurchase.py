# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 13:53:49 2018

@author: 612383461
"""

#####################################################
"""Creating a Mobile Data Bundle Purchase Program"""
#####################################################

#-----------------------------------------------------#
"""Use of subfunctions to make code cleaner
Adding three password attempts"""
#-----------------------------------------------------#

def DataBundlePurchase(truePasscode, balance):
    if passwordCheck(truePasscode): #means if it is True
        count = 0
        while count < 3:
            try:
                transactionType = int(input('''\nWhat would you like to do next?
    \nPlease choose a number from the following options:
            1. Credit balance request
            2. Purchase data bundle
            3. Exit\n'''))
                count += 1
                if transactionType ==1:
                    print('Your balance is £{}'.format(balance))
                    second_option = chooseAgain(balance)
                    break
                elif transactionType ==2:
                    stepsForDataBundlePurchase(balance)
                    break
                elif transactionType ==3:
                    return 'Thank you for using our online system.'
                else:
                    print('Your request has not been recognised and the service cannot proceed. Please only choose 1, 2 or 3.')
            except ValueError:
                print('Please only type in numbers.')
                count += 1
    return 'Thank you for using our online system.'

#---Conducting password checks---#
def passwordCheck(truePasscode):
    count = 0
    while True:
        while count < 3:
            attempt = input('Please enter your password ')
            if attempt == truePasscode:
                return True
                break
            else:
                count += 1
                print('You have entered your password incorrectly. Please try again.')
        print('You have entered your password incorrectly three times. Please reset your password.')
        return False
 
#---Checking Balance---#
def checkBalance(balance):
    if balance > 0:
        return True
    else:
        return False
        
#---Choosing option again---#
def chooseAgain(balance):
    count_2 = 0
    while count_2 < 3:
        try:
            nextChoice = int(input("""What would you like to do next?
    1. Purchase data bundle 
    2. Exit\n"""))
            count_2 += 1
            if nextChoice == 1:
                stepsForDataBundlePurchase(balance)
            elif nextChoice ==2:
                return 'Thank you for using our online system.'
            else:
                print('TWOYour request has not been recognised and the service cannot proceed. Please only choose 1 or 2.')
        except ValueError:
            print('Please only type in numbers.')
            count_2 += 1
    print('You have incorrectly selected an option three times.')
    return False

#---Steps for purchasing Data Bundle---#
def stepsForDataBundlePurchase(balance):
    if choosingPhoneNumber():
        if purchaseDataBundle(balance):
            return 'Thank you for purchasing a data bundle!'
        else:
            return 'Data bundle purchase was unsuccessful, please try logging in again.'

#---Supplying phone number for purchases---#
def choosingPhoneNumber():
    count = 0
    while count < 3:
        phoneNumber1= (input ("Please enter your phone number "))
        phoneNumber2= (input("Please enter your phone number again so we can be really sure "))
        count += 1
        try:
            if len(phoneNumber1) == 11 and len(phoneNumber2) == 11:
                phoneNumber1 = int(phoneNumber1)
                phoneNumber2 = int(phoneNumber2)
                if phoneNumber1 == phoneNumber2:
                    return True
                    break
                else:
                    print('Your phone numbers do not match. Please try again.')
            else:
                print('\nYour phone number must be 11 digits long. Please do not include the country code. Please try logging in again.')
        except ValueError:
            print('You can only input numbers.')
    return False

#---Purchasing a data bundle---#
def purchaseDataBundle(balance):
    count = 0
    while count < 3:
        try:
            purchaseAmount = int(input('''\nYou may purchase a data bundle up to the value of the balance which you have in your account and up to a maximum of £50. The purchase amount must be a multiple of £5.
        \nHow much would you like to spend to purchase a data bundle?'''))
            count += 1
            if (balance - purchaseAmount) >= 0:
                if checkMaxPurchaseAmount(purchaseAmount):
                    if multipleof5PurchaseAmount(purchaseAmount):
                        print('\nThank you for purchasing a data bundle with a value of £{}. Your new bundle has been added to your phone!'.format(purchaseAmount))
                        return True
                        break
                    else:
                        print('\nYou can only purchase a data bundle with a value which is a multiple of £5.')
                else:
                    print('\nYou cannot purchase a data bundle with a value which exceeds £50.')
            else:
                print('\nYou do not have enough credit to make this purchase. Your balance is £{}.'.format(balance))
                break
        except ValueError:
            print('You may only input numbers.')
            count += 1
    return False
    
def checkMaxPurchaseAmount(purchaseAmount):
    if purchaseAmount <= int(50):
        return True
    else:
        return False

def multipleof5PurchaseAmount(purchaseAmount):
    if purchaseAmount % 5 == 0:
        return True
    else:
        return False