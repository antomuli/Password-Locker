#!/usr/bin/env python3.6
from user import User
from credential import Credential

def create_user(account_name,user_name,password,email):
   
    new_user = User(account_name,user_name,password,email)
    return new_user

def save_user(user):
    
    user.save_user()    

def del_user(user):
    
    user.delete_user()    


def find_user(name):
    
    return User.find_by_user_name(name)    

def check_existing_user(name):
    
    return User.user_exist(name)    

def display_user():
    
    return User.display_user_name()  
 


def create_credential(credential_name,user_name,password,email):
    
    new_credential = Credential(credential_name,user_name,password,email)
    return new_credential

def save_credential(credential):
   
    credential.save_credential()    

def del_credential(credential):
   
    credential.delete_credential()    


def find_credential(name):
    
    return Credential.find_by_name(name)    

def check_existing_credential(name):
   
    return Credential.credential_exist(name)    

def display_credential():  
    
    return Credential.display_credential() 




def main():
    print("Hello! Welcome to your Password Locker application. Kindly tell me your name")
    user_name = input()
    print(f"Hello {user_name}, sign up to Password Locker to create an account.")
    print('\n')
    while True:
        print("Use these known short codes to operate :\n SU -> SIGN UP.\n DA -> Display your account.\n LN ->LOGIN.\n ex ->exit Password Locker. ")
        short_code = input().lower()
        if short_code == 'su':
            print("Create a Password Locker Account")
            print("_"*100)
            account_name = input('Account name:')
            print ('\n')
            u_name = input('Username:')
            print ('\n')
            pwd = input('Password : ')
            print ('\n')
            e_address = input('Email address:')
            save_user(create_user(account_name,user_name,pwd,e_address)) 
            print ('\n')
            print(f"A New {account_name} Account with the username  {u_name} has been created.")
            print(f"You can now login to your {account_name} account using your password.")
            print ('\n')
        elif short_code == 'da':
             if display_user():
                 print("Here is your account and your details")
                 print('\n')
                 for user in display_user():
                     print(f"Account name:{user.user_name}  User name: {user.user_name} Password:{user.password}")
                     print('\n')
             else:
                 print('\n')
                 print("You don't seem to have created an account.Sign up to create a new account.")
                 print('\n')
        elif short_code == 'ln':
            print("Enter your password to login.")
            search_user = input()
            if check_existing_user(search_user):
                search_credential = find_user(search_user)
                print("\033[1;32;1m   \n")
                print(f"You are now logged in to your {account_name} account")
                print("\033[1;37;1m   \n")
                
                while True:
                    print('''
                    Use these short codes:
                    CA -> Create new credential.
                    DC -> Display your credential list
                    ex ->Log out your credential account.''')
                    short_code = input().lower()
                    if short_code == "ca":
                        print("Create new credential")
                        print('_' * 20)
                        credential_name = input('Credential name:')
                        print('\n')
                        user_name = input(f"{credential_name} username:")
                        print('\n')
                        print('*' * 20)
                        pwd = input(f"{credential_name} password:")
                        save_credential(create_credential(credential_name,user_name,pwd,e_address))
                        print('\n')
                        print(f"A New {credential_name} Account with the user name  {usr_name} has been created.")
                        print ('\n')
                    elif short_code == 'dc':
                         if display_credential():
                             print("Here is your credential")
                             print('\n')
                             for credential in display_credential():
                                 print(f"Credential name:{credential.credential_name}  User name: {credential.user_name} Password:{credential.password}")
                                 print('\n')
                         else:
                              print('\n')
                              print("You don't seem to have created any account yet")
                              print('\n')
                    elif short_code == "ex":
                        print('\n')
                        print(f"You have logged out your {account_name} account")
                        print('\n')
                        break
                        
            else:
                print('\n')
                print("WRONG PASSWORD!! PLEASE ENTER CORRECT PASSWORD TO LOGIN")
                print('\n')
                print('\n')
                    
        elif short_code == "ex":
                    print(f"Thanks {user_name} for your time.I hope you enjoyed my service.Bye...")
                    break
        else:
                    print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':
    main()                            