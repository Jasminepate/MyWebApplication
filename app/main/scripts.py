#!/usr/bin/python3

from werkzeug.security import generate_password_hash, check_password_hash

class HashPass:
        """
        This class hash all passwords and verify that the user has the correct password when signing in.
        """
        def __init__(self, password, hashed=None):
                self.password = password
                self.hashed = hashed

        def hashit(self):
                return generate_password_hash(self.password)

        def verify(self):
                return check_password_hash(self.password, self.hashed)

