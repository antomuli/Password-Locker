class Credential:
    """
    Class that generates new instances of users.
    """
    credential_list = []

    def __init__(self,credential_name,user_name,password,email):
        self.credential_name = credential_name
        self.user_name = user_name
        self.password = password
        self.email = email

    def save_credential(self):

      

        Credential.credential_list.append(self)    


    def delete_credential(self):

      

        Credential.credential_list.remove(self)   


    @classmethod
    def find_by_name(cls,name):
        for credential in cls.credential_list:
            if credential.credential_name == name:
                return credential  


    @classmethod
    def credential_exist(cls,name):
       
        for credential in cls.credential_list:
            if credential.password == name:
                    return credential

        return False      


    @classmethod
    def display_credential(cls):  
       
        return cls.credential_list            
                      