📚 BookCoin

A custom blockchain implementation built from scratch in Python

---

🚀 Overview

BookCoin is a lightweight blockchain system built from scratch to demonstrate the core mechanics behind decentralized ledgers like Bitcoin.

It includes block creation, transaction handling, wallet management, and a basic consensus mechanism—implemented without external blockchain frameworks to showcase fundamental concepts.

---

✨ Features
⛓️ Custom blockchain implementation
🔐 SHA-256 cryptographic hashing
⛏️ Proof-of-Work mining & consensus
💸 Transaction creation and validation
👛 Wallet system for managing balances
📦 Chain verification and integrity checks
🧠 Modular architecture for easy extension
🧠 Architecture

The project is organized into modular components:

BookCoin/
│── blockchain.py     # Core blockchain logic
│── consensus.py     # Proof-of-Work / consensus algorithm
│── transactions.py  # Transaction creation & validation
│── wallet.py        # Wallet and balance management
│── utils.py         # Helper functions (hashing, etc.)
│── run.py           # Entry point to run the blockchain
│── __init__.py
│── BookCoins_List.txt
│── LICENSE
│── README.md

⚙️ How It Works

---

🔗 Blockchain (blockchain.py)
Maintains the chain of blocks
Handles block creation and linking via hashes
⛏️ Consensus (consensus.py)
Implements a Proof-of-Work algorithm
Ensures blocks meet difficulty requirements before being added
💸 Transactions (transactions.py)
Defines transaction structure
Validates transaction data
👛 Wallet (wallet.py)
Manages user balances
Simulates sending and receiving coins

🛠️ Utilities (utils.py)
Provides hashing and helper functions

🛠️ Tech Stack
Language: Python
Concepts:
Cryptography
Distributed Systems
Data Structures
Libraries:
Built-in hashlib for SHA-256

---

▶️ Getting Started
Clone the repo
git clone https://github.com/yourusername/bookcoin.git
cd bookcoin
Run the blockchain
python run.py
🧪 Example Workflow
Create a wallet
Submit transactions
Mine a new block
Verify the updated chain

---

🎯 Learning Objectives

This project demonstrates:

How blockchains maintain immutability
How Proof-of-Work secures a network
How transactions are validated and stored
How wallets interact with a blockchain

---

⚠️ Disclaimer

This project is for educational purposes only and is not intended for real-world financial use.

---

🚧 Future Improvements
Peer-to-peer networking
Public/private key cryptography
REST API for external interaction
GUI or web dashboard
Smart contract support

---

📜 License

MIT License

---

👤 Author

Joseph K
