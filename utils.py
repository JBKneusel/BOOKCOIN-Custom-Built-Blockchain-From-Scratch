import hashlib
import json

class Utils:
    @staticmethod
    def get_token_owners(tokens):
        """
        Get a list of all tokens and their owners.
        """
        return tokens