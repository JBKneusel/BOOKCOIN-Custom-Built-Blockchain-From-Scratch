import hashlib
import json
from time import time

class Blockchain:
    def __init__(self):
        self.chain = []  # This is our chain, as in block"chain". AKA an empty list.
        self.current_transactions = []  # Storing current transactions
        self.tokens = self.initialize_tokens()  # Initialize 1407 tokens
        self.create_block(previous_hash='1', proof=100)  # Genesis block

    def initialize_tokens(self):
        """
        Create 1407 unique tokens with unique IDs and assign them to the creator (e.g., 'Creator').
        """
        return {f"Token#{i + 1}": "Coin Sultan" for i in range(1407)}

    def transfer_token(self, sender, recipient, token_id):
        """
        Transfer ownership of a token.
        Validate that the sender owns the token and update its owner.
        """
        # Ensure the token exists
        if token_id not in self.tokens:
            raise ValueError(f"Token {token_id} does not exist.")
        
        # Validate ownership
        if self.tokens[token_id] != sender:
            raise ValueError("Sender does not own this token.")
        
        # Update ownership
        self.tokens[token_id] = recipient
        return True

    def create_block(self, proof, previous_hash):
        """
        Create a new block and append it to the chain.
        """
        block = {
            'index': len(self.chain) + 1,  # Where in the chain it is
            'timestamp': time(),  # What time was this transaction?
            'transactions': self.current_transactions,  # List of transactions in the block
            'proof': proof,  # Proof-of-work for the block
            'previous_hash': previous_hash,  # Hash of the previous block
        }
        self.current_transactions = []  # Clear current transactions
        self.chain.append(block)  # Link the block onto the chain
        return block

    def get_last_block(self):
        """
        Return the most recent block.
        """
        return self.chain[-1]

    def proof_of_work(self, last_proof):
        """
        Simple proof-of-work algorithm to prevent tampering.
        """
        proof = 0
        while not self.is_valid_proof(last_proof, proof):
            proof += 1
        return proof

    @staticmethod
    def is_valid_proof(last_proof, proof):
        """
        Validate the proof-of-work.
        """
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"  # Adjust difficulty as needed

    @staticmethod
    def hash(block):
        """
        Hash a block using SHA-256.
        """
        return hashlib.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()

    def add_transaction(self, sender, recipient, amount):
        """
        Add a new transaction to the list of pending transactions.
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.get_last_block()['index'] + 1

    def is_chain_valid(self, chain):
        """
        Check if the blockchain is valid.
        """
        for i in range(1, len(chain)):
            prev_block = chain[i - 1]
            curr_block = chain[i]

            # Check if the hash of the previous block matches
            if curr_block['previous_hash'] != self.hash(prev_block):
                return False

            # Check if the proof-of-work is valid
            if not self.is_valid_proof(prev_block['proof'], curr_block['proof']):
                return False

        return True