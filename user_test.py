import unittest
import pyperclip
from user import User

class TestUser(unittest.TestCase):
    
     def setUp(self):
         
         
          self.new_user = User("Anthony","Muli","antomuli","anto254")
          
          
          
     def test_init(self):
          '''
          test to initialize and instantiate the methods
          '''
        self.assertEqual(self.new_user.first_name,"Anthony")
        self.assertEqual(self.new_user.last_name,"Muli")
        self.assertEqual(self.new_user.user_name,"antomuli")
        self.assertEqual(self.new_user.password,"anto254")
     
               
         
     def test_save_user(self):
       '''
       to show whether the user's details can be saved
       '''
        self.new_user.save_user() 
        self.assertEqual(len(User.user_list),1)
        
     def test_save_multiple_user(self):
       '''
       test to enable save for multiple users
       '''
        self.new_user.save_user()
        test_user = User("Facebook","Anthony","antomuli","anto254") 
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)
    
     def tearDown(self):
         '''
         cleans up the user_list after each test is run
         '''
         User.user_list = []

     def test_delete_user(self):
        '''
        test to delete_user
        '''
         self.new_user.save_user()
         test_user = User("Facebook","Anthony","antomuli","anto254") 
         test_user.save_user()

         self.new_user.delete_user()
         self.assertEqual(len(User.user_list),1)
     def test_find_user_by_username(self):
         '''
         to find user by username
         '''

         self.new_user.save_user()
         test_user = User("Facebook","Anthony","antomuli","anto254")
         test_user.save_user()

         found_user = User.find_by_user_name("antomuli")

         self.assertEqual(found_user.user_name,test_user.user_name)
     def test_user_exists(self):
         '''
         test to affirm that the user exists
         '''

         self.new_user.save_user()
         test_user = User("Facebook","Anthony","antomuli","anto254") 
         test_user.save_user()

         user_exists = User.user_exist("antomuli")

         self.assertTrue(user_exists)
     def test_display_all_users(self):
       '''
       test to display all current users
       '''

         self.assertEqual(User.display_user(),User.user_list)
   
     def test_copy_password(self):
         '''
         test to allow copy and paste of user's details to the clipboard
         '''

         self.new_user.save_user()
         User.copy_password("")

         self.assertEqual(self.new_user.password,pyperclip.paste())

if __name__ ==  '__main__':
 unittest.main()