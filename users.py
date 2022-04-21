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