import pyperclip


class User:

    user_list = []

    def __init__(self, first_name, last_name, user_name, password):

        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password

    user_list = []
    def save_user(self):

        User.user_list.append(self)

    def delete_user(self):

        User.user_list.remove(self)

    @classmethod
    def find_by_user_name(cls, user_name):

        for user in cls.user_list:
            if user.user_name == user_name:
                return user_name

    @classmethod
    def user_exist(cls, user_name):

        for user in cls.user_list:
            if user.user_name == user_name:
                return True

        return False

    @classmethod
    def display_user_name(cls):

        return cls.user_list

    @classmethod
    def copy_password(cls, password):
        user_found = User.find_by_password(password)
        pyperclip.copy(user_found.password)