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