# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from hashlib import sha256

def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

max_nonce = 2000000000

def mine(block_number, transactions, previous_hash, prefix_zeroes):
    prefix_str = '0'*prefix_zeroes
    for nonce in range(max_nonce):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print("Good, was able to mine the block")
            return new_hash

    raise BaseException("Sorry, couldn't come up with the hash value")

if __name__ == '__main__':
    transactions = """
        alice -> bob -> 20,
        bob -> carol -> 10,
        carol -> qfc -> 5
    """
    print(SHA256(transactions))
    difficulty = 6
    new_hash = mine(5, transactions, "68f57a49420bf81083f7d759826eba19f0efae985b861315dc2a219ee603ab15", difficulty)
    print(new_hash)