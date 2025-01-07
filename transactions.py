from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15
from cryptography.hazmat.primitives import hashes

class Transaction:
    @staticmethod
    def create_token_transaction(sender, recipient, token_id):
        """
        Create a token transfer transaction.
        """
        return {
            'type': 'token_transfer',
            'sender': sender,
            'recipient': recipient,
            'token_id': token_id,
        }
    @staticmethod
    def sign_transaction(private_key, message):
        """
        Sign a transaction message with a private key.
        """
        return private_key.sign(
            message.encode(),
            PKCS1v15(),
            hashes.SHA256()
        )

    @staticmethod
    def verify_transaction(public_key, signature, message):
        """
        Verify a transaction signature using the sender's public key.
        """
        try:
            public_key.verify(
                signature,
                message.encode(),
                PKCS1v15(),
                hashes.SHA256()
            )
            return True
        except:
            return False