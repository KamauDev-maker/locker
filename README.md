# Password Locker
## Description
A Python CLI application that allows users to save application credentials such  as their username and password.2022-04-24 20:51:04 Sunday
By [Oscar Kamau](https://github.com/KamauDev-maker "Oscar Kamau")

## User Stories
The user would like to....:
- Create new credentials.
Here users are required to [provide an application name,their username for the account they and a password of the said account. Users are also provided with the option of a generated password.
- Find Credentials.
Here users can find credentials by using the application name.
- See all credentials.
Users are able to view a list of all credential saved.
- Delete a credential.
Here user can remove credentials they don't need.
***users can also delete an active account.***
## Installation/Setup instruction
The application requires the following installations to operate:
- python
- pyperclip
- pip
#### Cloning
- Open Terminal (Ctrl+Alt+T)
- git clone
- code .
## Behaviour Driven Development
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
|Open the application on the terminal | Run the command ```$ ./credentials.py```|What is your name.|Hello "name" kindly use the short codes<br>* CA ---  Create New Account * LI ---  login into an existing account |
|Select  CA| input username and password| Hello ```username```, Your account has been created succesfully! Your password is: ```password```|
|Select LI  | Enter your password and username you signed up with| Short-codes menu to help you navigate through the application|
|Store a new credential in the application| Enter ```CC```|Enter Account, username, password<br>choose ```Yes``` to enter your password or ```No``` for the application to generate a password for you |
|Display all stored credentials | Enter ```SC```|A list of all credentials that has been stored or ```You don't have any credentials saved yet``` |
|Find a stored credential based on account name|Enter ```FC```| Enter the Account Name you want to search for and returns the account details|
|Delete an existing credential that you don't want anymore|Enter ```DEL```|Enter the account name of the Credentials you want to delete and returns true if the account has been deleted and false if the account doesn't exixt|
|Exit the application| Enter ```EX```| The application exits|

## Contact Information
Please email me at [oscarnjenga@gmail.com](https://mail.google.com/ "oscarnjenga@gmail.com")
## License
- *MIT License:*
- Copyright &copy;2022 Oscar Kamau
