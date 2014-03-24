#!/usr/bin/env python2.7

# name:     399crypto_analysis.py
# author:   Chad Hobbs
# created:  140322
#
# description: ##

import os
from Crypto.Cipher import DES3
from Crypto import Random

# ----------------------------------------------------------------------------------------
# Function Name: encrypt_file(in_filename, out_filename, chunk_size, key, iv)
# Parameters:    None
# Returns:       None
# Description:   ##
# ----------------------------------------------------------------------------------------
def encrypt_file(in_filename, out_filename, chunk_size, key, iv):
    des3 = DES3.new(key, DES3.MODE_CFB, iv)

    with open(in_filename, 'r') as in_file:
        with open(out_filename, 'w') as out_file:
            while True:
                chunk = in_file.read(chunk_size)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' ' * (16 - len(chunk) % 16)
                out_file.write(des3.encrypt(chunk))

# ----------------------------------------------------------------------------------------
# Function Name: decrypt_file(in_filename, out_filename, chunk_size, key, iv)
# Parameters:    None
# Returns:       None
# Description:   ##
# ----------------------------------------------------------------------------------------
def decrypt_file(in_filename, out_filename, chunk_size, key, iv):
    des3 = DES3.new(key, DES3.MODE_CFB, iv)

    with open(in_filename, 'r') as in_file:
        with open(out_filename, 'w') as out_file:
            while True:
                chunk = in_file.read(chunk_size)
                if len(chunk) == 0:
                    break
                out_file.write(des3.decrypt(chunk))


# ----------------------------------------------------------------------------------------
# Function Name: ##
# Parameters:    None
# Returns:       None
# Description:   ##
# ----------------------------------------------------------------------------------------

key = Random.get_random_bytes(16)
iv = Random.get_random_bytes(8)

userInput = raw_input('Enter string to encrypt: ')
f = open('to_enc.txt', 'w')
f.write(userInput)
f.close

with open('to_enc.txt', 'r') as f:
    print 'to_enc.txt: %s' % f.read()
encrypt_file('to_enc.txt', 'to_enc.enc', 8192, key, iv)
with open('to_enc.enc', 'r') as f:
    print 'to_enc.enc: %s' % f.read()
decrypt_file('to_enc.enc', 'to_enc.dec', 8192, key, iv)
with open('to_enc.dec', 'r') as f:
    print 'to_enc.dec: %s' % f.read()
