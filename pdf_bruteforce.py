#!/usr/bin/python

"""pdf_bruteforce.py: Simple python sccript to bruteforce open password protected pdf file"""
__author__      = "Shiju P K"

import sys # standard library
from io import BytesIO 

import fitz # 3rd party packages

def main(argv):
    inputfile = ''
    n = len(sys.argv) 
    if n!=2:
        print("Pass file name argements")
        return

    filename = sys.argv[1] 
    file =  open(filename, 'rb').read()
    buffer = BytesIO(file)  # convert to stream 
    pdf = fitz.open("pdf", buffer)

    attempts = 0
    passwordfile = open('passwords.txt', 'r')
    contents = passwordfile.read()
    passwords = contents.split('\n')
    for i in range(len(passwords)):
        password = passwords[i]
        print('Decrypting with: {}'.format(password))
        valid = pdf.authenticate(password)
        if valid >= 1:
            print('Success! The password is: ' + password)
            return

        elif valid == 0:
            attempts += 1
            continue
    print('Failed to decrypt with available passwords!')

if __name__ == "__main__":
   main(sys.argv[1:])


