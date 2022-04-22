from numpy import int32
from users import Users, Credentials

def  create_user(username,login_password):
    """
    Function to create new user
    """
    new_user = Users(username,login_password)
    return new_user

def  add_user(user):
    """
    function to save user
    """
    user.add_user()
    
def  delete_user(user):
    """
    function to remove user
    """
    user.delete_user()
    
def  find_user(username):
    """
    function to find user by username
    """
    return Users.find_by_username(username)

def  existing_user(username, login_password):
    """
    function to authenticate user 
    """
    return Users.user_exists(username, login_password)

def  create_credentials(application_name,account_username,account_password):
    """
    function to create new credentials 
    """
    new_credentials = Credentials(application_name,account_username,account_password)

def  add_credentials(new_credentials):
    """
    function to save credentials
    """
    new_credentials.add_credentials()
    
    
def  remove_credentials(new_credentials):
    """
    function to delete credentials
    """
    new_credentials.delete_credentials
    
def display_credentials():
    """
    function that returns all saved credentials
    """
    return Credentials.display_credentials()

def  existing_credentials(application_name,account_username,account_password):
    """
    function to check that credentials for user exists
    """
    return Credentials.credentials_exist(application_name,account_username,account_password)

def  find_credentials(application_name):
    """
    Function to find credentials using the application name
    """
    return Credentials.find_by_application_name(application_name)

def  generate_a_password(passwordLength):
    """
    function that generates random password of 8 chraracters
    """
    return Credentials.generate_password(passwordLength)


def main():
    print(" "*8 + "PASSWORD LOCKER" + " "*8)
    print("--"*16)
    print("An Application that manages your password. ")
    while True:
        print("What is your name? ") 
        current_user = input().strip(' ').capitalize()
        if current_user != '':
            print(f"\nHello {current_user},")
            while True:
                print("Kindly use these short Codes to navigate through the application :\n CA - create account \n LI - login into an existing account \n DEL - delete your acount \n EX - exit the application")
                short_code = input().upper()
                
                if short_code == 'CA':
                    print("\nCREATE AN ACCOUNT")
                    print("-"*17)
                    print("Choose your username")
                    print(" "*6 +"*the username must contain alphabetical letters and no spaces*")
                    
                    while True:
                        username = input().capitalize()
                        if username.isalpha():
                            print("Choose a password")
                            print(" "*6 +"*the password must be 8 character or more characters*")
                            while True:
                                login_password = input()
                                if len(login_password) >=8:
                                    add_user(create_user(username,login_password))
                                    print(f"\nAccount for {username} has been successfully created.  \nProceed to login. \n")
                                    break
                                else:
                                    print("\nThe username entered is invalid. ")
                                    print("Please use alphabetical letters and no spaces. ")
                                    continue
                        else:
                             print("\nThe password you entered is too short.")
                             print("Please use a password of 8 characters or more.")
                             continue
                        break           
                elif short_code == 'LI':
                    print("\nLOGIN")
                    print("-"*7)
                    
                    print("Enter your username")
                    username = input().strip(' ').capitalize()
                    print("Enter your password")
                    login_password = input().strip(' ')
                    
                    if existing_user(username,login_password):
                        print("\nLog in successful")
                        print("what would like to do? ")
                        
                        while True:
                            print("\nUse these short codes for navigation: \n CC: create new credentials \n FC: find a credential \n DEL: delete a credential \n SC: see all saved credentils \n LO: log out")
                            credentials_navigation = input().upper()
                            
                            if credentials_navigation == 'CC':
                                print("\nCREATE NEW CREDENTIALS")
                                print("-"*22)
                                while True:
                                    print("Application name")
                                    print(" "*4 + "*eg. Netflix") 
                                    application_name = input().capitalize().strip(' ')
                                    if application_name != '':
                                        print(f"What is your current username on {application_name}?" )
                                        account_username = input()
                                        
                                        while True:
                                            print(f"\nDo you already have a password on {application_name}?  (Y/N")
                                            has_password = input().upper()
                                            if has_password == 'Y':
                                                print(f"Enter your {application_name} password")
                                                account_password = input()
                                                add_credentials(create_credentials(
                                                    
                                                    application_name,account_username,account_password ))
                                                print(f"\nAccount credentials for your {application_name} account have been successfully saved. ")
                                                break
                                            elif has_password == 'N':
                                                while True:
                                                    print("Would you like a generated password? (Y/N)")
                                                    gen_pass = input().upper()
                                                    if gen_pass == 'Y':
                                                        print("How long would you like your password to be? ")
                                                        print(" "*6 + "less than 8 characters: WEAK" + "\n" + " "*6 + "8 characters:STRONG" + "\n" + " "*6 + "8-20 characters:VERY STRONG") 
                                                        while True:
                                                            try:
                                                                passwordLength = int(input())
                                                                if passwordLength in range(21):
                                                                    account_password = generate_a_password(passwordLength)
                                                                    print(f"Password generated is {account_password}")
                                                                    add_credentials(create_credentials(
                                                                                                   
                                                                        application_name,account_username,account_password))
                                                                    print(f"Account credentials for your {application_name} have been successfully saved. \n")
                                                                    break
                                                            except ValueError: 
                                                                print("\nYou did not pick a valid password lenght")
                                                                print("Please pick a number between 0-20 and try again")
                                                                continue
                                                    elif gen_pass == 'N':
                                                            print(f"Choose a password you wish to use for your {application_name} account")
                                                            print(" "*6 + "*Password must be longer than 8 characters*")
                                                            while True:
                                                                account_password = input()
                                                                if len(account_password) >=8:
                                                                    add_credentials(create_credentials(
                                                                
                                                                       application_name,account_username,account_password)) 
                                                                    print(f"Account credentials for you {application_name} have been successfully saved. \n")
                                                                    break
                                                                else:
                                                                    print("\nThe password your entered is too short ")
                                                                    print("Please use a password of 8 characters or more.")
                                                                    continue 
                                                    else:
                                                        print("You did not select a valid option")
                                                        print("Please enter (Y/N) and try again")
                                                        continue
                                                    break   
                                                break 
                                            else:
                                                print("\nsorry,i did not quite get the application name. Please try again. ")
                                                continue                     
if __name__ == '__main__':
    main()            