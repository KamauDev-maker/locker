import random
import string
import pyperclip

class Credentials:
    """class that generate new instances of credentials
    """
    credentials__list = []
    
    def __init__(self,application_name,account_username,account_password):
        """method that helps us define properties for our objects_summary_

        Args:
            application_name (_type_): _description_
            account_username (_type_): _description_
            account_password (_type_): _description_
        """
        self.application_name = application_name
        self.account_username = account_username
        self.account_password = account_password
    def  add_credentials(self):
        """method that saves credentials into credentials_list
        """
        Credentials.credentials__list.append(self)
    
    def  delete_credentials(self):
        '''
        delete_credentials method that deletes credentials from credential_list
        ''' 
        Credentials.credentials__list.remove(self)
        
    @classmethod
    def  find_by_application_name(cls,application_name):
        """method  that takes in application name and returns the credentials for the said application

        Args:
            application_name: name of application to be found
        """
        for credential in Credentials.credentials__list:
            if credential.application_name == application_name:
                return credential

    @classmethod
    def credentials_exists(cls,application_name):
        """method that checks if a credential exist from credential_list

        Args:
            application_name:name to search if an account exist
        """
        for credential in Credentials.credentials__list:
            if credential.application_name == application_name:
                return True
        return False
    
    @classmethod
    def  display_credentials(cls):
        """ method that returns a list of all credentials
        """
        return Credentials.credentials__list
    
    def  generate_password(passwordLenght):
        """
        method that generates a random password for the account user
        Args:
            passwordLenght: password lenght for the account user
        """
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits
        return "".join(random.choice(password)for i in range(passwordLenght))
    @classmethod
    def  copy_password(cls,account):
         found_credentials = Credentials.find_credential(account)
         pyperclip.copy(found_credentials.password)


class Users:
    """class that generates new instances of users
    """
    users_list = []
    
    def  __init__(self,username,login_password):
        """
         method that helps us define properties for our object
        Args:
            username :New username
            login_password:New user password
        """
        self.username = username
        self.login_password = login_password
             
    def  add_user(self):
        """
        add user details method saves user objects
        """
        Users.users_list.append(self)
    
    def  delete_user(self):
        """
        method removes user details
        """  
        Users.users_list.remove(self) 
        
    @classmethod
    def  find_by_username(cls,username):
        """
        authenticate user 

        Args:
            username:name used by user to login in
        """
        for user in Users.users_list:
            if user.username == username:
                return user
            
    @classmethod
    def  user_exists(cls,username,login_password):
        """
        authenticate user password by checking if the user exist

        Args:
            username :username used to login
            login_password:password for the user
        """
        for user in Users.user_list:
            if user.username == username and user.login_password == login_password:
                return True
        return False   