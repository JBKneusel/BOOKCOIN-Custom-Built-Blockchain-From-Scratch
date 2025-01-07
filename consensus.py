class Consensus:
    @staticmethod
    def get_token_owners(tokens):
        """
        Get a list of all tokens and their owners.
        """
        return tokens
        
    @staticmethod
    def is_valid_chain(chain):
        """
        Check if a blockchain is valid.
        """
        for i in range(1, len(chain)):
            block = chain[i]
            previous_block = chain[i - 1]
            # Check if the block's previous hash matches
            if block['previous_hash'] != Blockchain.hash(previous_block):
                return False
            # Check if the proof of work is valid
            if not Blockchain.valid_proof(previous_block['proof'], block['proof']):
                return False
        return True