import unittest 
from credential import Credential


class TestCredential(unittest.TestCase):
    def setUp(self):
       
        self.new_credential = Credential("anthony","muli","123456","mulianthony561@@gmail.com") # create Account object

    
    def test_init(self):
        

        self.assertEqual(self.new_credential.credential_name,"anthony")
        self.assertEqual(self.new_credential.user_name,"muli")
        self.assertEqual(self.new_credential.password,"123456")
        self.assertEqual(self.new_credential.email,"mulianthony561@gmail.com")

    def test_save_credential(self):
       
        self.new_credential.save_credential() # saving the new account
        self.assertEqual(len(Credential.credential_list),1)  


    def tearDown(self):
            
            Credential.credential_list = []    


    def test_save_multiple_credential(self):
            
            self.new_credential.save_credential()
            test_credential = Credential("Test","user","0712345678","test@user.com") 
            test_credential.save_credential()
            self.assertEqual(len(Credential.credential_list),2)


    def test_delete_credential(self):
            
            self.new_credential.save_credential()
            test_credential = Credential("Test","user","0712345678","test@user.com") 
            test_credential.save_credential()

            self.new_credential.delete_credential()
            self.assertEqual(len(Credential.credential_list),1) 

    def test_find_credential_by_credential_name(self):
       

        self.new_credential.save_credential()
        test_credential = Credential("Test","user","0711223344","test@user.com") 
        test_credential.save_credential()

        found_credential = Credential.find_by_name("Test")

        self.assertEqual(found_credential.email,test_credential.email)  



    def test_credential_exists(self):
        

        self.new_credential.save_credential()
        test_credential = Credential("Test","user","0711223344","test@user.com") # new account
        test_credential.save_credential()

        credential_exists = Credential.credential_exist("0711223344")
        self.assertTrue(credential_exists)    
        
                       


if __name__ == '__main__':
    unittest.main()    