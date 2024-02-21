#!/usr/bin/python3
"""
 User Model
"""
import hashlib
import uuid


class User:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self._password = None

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, pwd):
        if isinstance(pwd, str):
            self._password = hashlib.md5(pwd.encode()).hexdigest().lower()

    def is_valid_password(self, pwd):
        return isinstance(pwd, str) and self.password is not None and \
               hashlib.md5(pwd.encode()).hexdigest().lower() == self.password


if __name__ == '__main__':
    print("Test User")

    user_1 = User()
    assert user_1.id is not None, "New User should have an id"

    user_2 = User()
    assert user_1.id != user_2.id, "User.id should be unique"

    u_pwd = "myPassword"
    user_1.password = u_pwd
    assert user_1.password is not None, "User.password should be hashed"

    assert user_2.password is None, "User.password should be None by default"

    user_2.password = None
    assert user_2.password is None, "User.password should be None if set to None"

    user_2.password = 89
    assert user_2.password is None, "User.password should be None if set to an integer"

    assert user_1.is_valid_password(u_pwd), "is_valid_password should return True if it's the right password"
    assert not user_1.is_valid_password("Fakepwd"), "is_valid_password should return False if it's not the right password"
    assert not user_1.is_valid_password(None), "is_valid_password should return False if compared with None"
    assert not user_1.is_valid_password(89), "is_valid_password should return False if compared with an integer"
    assert not user_2.is_valid_password("No pwd"), "is_valid_password should return False if no password set before"

