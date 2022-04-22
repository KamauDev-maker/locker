from users import Users
from credentials import Credentials

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
    