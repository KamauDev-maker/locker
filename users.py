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
    def  save_credentials(self):
        """method that adds credentials into credentials_list
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
       
    
         
        