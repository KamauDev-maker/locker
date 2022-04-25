import unittest
from users import Users

class TestUsers(unittest.TestCase):
    """
    class that defines test casesfor the user class behaviour

    Args:
        unittest TestCase: TestCase class that helps in creating test cases
    """
    
    def setUp(self):
        """
        set up method to run before each test cases
        """
        
        self.new_user = Users("Oscar", "90")
        
    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """    
        self.assertEqual(self.new_user.username, "Oscar")
        self.assertEqual(self.new_user.login_password, "90")
    
    def test_add_user(self):
        """
        test_add_user case to test if the user object is saved into the users list 
        """
        self.new_user.add_user()
        self.assertEqual(len(Users.users_list),1)
        
    def tearDown(self):
        """
        method that does clean up after each test case has run
        """
        Users.users_list = []
        
    def test_add_multiple_users(self):
        """
        to check if we can save multiple users object to our users list
        """    
        self.new_user.add_user()
        test_user = Users("Sekani","0101")
        test_user.add_user()
        self.assertEqual(len(Users.users_list),2)
    
    def test_remove_users(self):
        """
        to test if we can remove a users from our users list
        """ 
        self.new_user.add_user()
        test_user = Users("Sekani","0101")
        test_user.add_user()
        test_user1 =Users("Natalie","02")
        test_user1.add_user()
        
        test_user.delete_user()
        self.assertEqual(len(Users.users_list),2)

if __name__ ==  '__main__':
    unittest.main()