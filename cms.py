import hashlib
import os
from register import *


clear = lambda : os.system('cls')
user_choice = ' '
def main():
    clear()
    print(" Main menu ")
    print("------------")
    print()
    print("1. Register")
    print("2. Exit")


    user_choice = ' '
    while user_choice != '2':
        while True:
            print()
            user_choice = input(" Enter your choice: ")
            if user_choice not in ['1','2']:
                print(" Not a valid option ")

            elif user_choice in ['1','2']:
                break

        while True:
            if user_choice == '1':
                register()
                break
            if user_choice == '2':
                print("Bye")
                exit()


def register():
    clear()

    while True:
        name = input(" Enter name: ")
        set_name(name)
        name = get_name()
        if name!= '':
            break

    while True:
        email_address = input("Enter email address: ")
        set_email(email_address)
        email_address = get_email()
        if email_address!= '':
            break

    while True:
        password = input("Enter password: ")
        set_password(password)
        password = get_password()
        if password!= '':
            break

    while True:
        highest_qualification = input("Enter highest qualification: ")
        set_qualification(highest_qualification)
        highest_qualification = get_qualification()
        if highest_qualification!= '':
            break

    while True:
        occupation = input("Enter Occupation: ")
        set_occupation(occupation)
        occupation = get_occupation()
        if occupation!= '':
            break

    while True:
        employer_details = input("Enter Employer Details: ")
        set_empDetails(employer_details)
        employer_details = get_empDetails()
        if employer_details!= '':
            break

    while True:
        mobile_number = input("Enter Mobile Number: ")
        set_mobile(mobile_number)
        mobile_number = get_mobile()
        if mobile_number!= '':
            break

    while True:
        interest_area = input("Enter Interest Area: ")
        set_interest(interest_area)
        interest_area = get_interest()
        if interest_area!= '':
            break

    while True:
        choose_role = input("Enter Choose Role (""Chair,Author,Reviewer""): ")
        set_chooseRole(choose_role)
        choose_role = get_chooseRole()
        if choose_role in ['Chair','Author','Reviewer']:
            break
        else:
            print("Role choose do not match according to the option given")

    addUserInfo([name, email_address, password, highest_qualification, occupation, employer_details, mobile_number, interest_area, choose_role])


def addUserInfo(userinfo: list):
    with open('userInfo.txt','a') as file:
        for info in userinfo:
            file.write(info)
            file.write(' ')
        file.write('\n')

main()
"""
def login():
    pass
def userAlreadyExists():
    pass
def sanitizeName():
    pass
def hashPassword(password):
    return hashlib.sha256(str.encode(password)).hexdigest()
def checkPassword(password, hash):
    return hashPassword(password) == hash
"""
