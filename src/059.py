import string
import itertools as it


with open("059.dat", 'r') as f:
    encrypted_bytes = [int(i) for i in f.read().split(',')]


def decode(ascii_val, key):
    kbytes = ord(key)
    return chr(ascii_val ^ kbytes)


def encode(char, key):
    return ord(char) ^ ord(key)


common_words = {'the', 'and', 'this', 'are', 'that', 'have', 'with'}
wierd_stuff = {'<', '>', '[', ']', '~', '|', '#', '"'}
for password in it.product(string.ascii_lowercase, repeat=3):
    key = it.islice(it.cycle(password), len(encrypted_bytes))
    decoded = (decode(byte, k) for byte, k in zip(encrypted_bytes, key))
    message = ''.join(decoded)
    if any(word in message for word in common_words):
        if not any(stuff in message for stuff in wierd_stuff):
            print(password)
            print(message)
            print(sum(ord(c) for c in message))