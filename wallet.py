from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

class Wallet:
    @staticmethod
    def generate_keys():
        """
        Generate a new public-private key pair.
        """
        private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        public_key = private_key.public_key()
        return private_key, public_key

    @staticmethod
    def export_key(key, key_type='public'):
        """
        Export the public or private key as a PEM-formatted string.
        """
        if key_type == 'public':
            return key.public_bytes(
                serialization.Encoding.PEM,
                serialization.PublicFormat.SubjectPublicKeyInfo,
            ).decode()
        elif key_type == 'private':
            return key.private_bytes(
                serialization.Encoding.PEM,
                serialization.PrivateFormat.PKCS8,
                serialization.NoEncryption(),
            ).decode()