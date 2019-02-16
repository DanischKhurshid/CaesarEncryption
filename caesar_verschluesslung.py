# -*- coding: utf-8 -*-

from __future__ import division # important package for precise division of floats


class Caesar: # create Class Caesar => Python OOP

    def __init__(self): # Constructor which initialize and declare a attribute alphabet
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # Different Methods in Class Caesar

    def encrypt(self, shift_key, message):
        message = message.upper() # make every letter in string Upper Case
        encrypt_message = "" # define encrypt message

        # tries to to find letter from text in the alphabet string with the help of nested for loop
        for character in message:
            for a in self.alphabet:
                if character == a: # if it finds a letter from text in the alphabet string
                    index = self.alphabet.index(character) # get the index of the letter in alphabet string
                    index = (index + shift_key) % 26 # shift the index according to the shift_key
                    encrypt_message = encrypt_message + self.alphabet[index] # add the letter from alphabet list with specific index to the new encrypt message string

        return "Normal Message is {}, Encrypt Message is {}".format(message, encrypt_message) # return the normal and encrypted message

    def decrypt(self, shift_key, encrypt_message):
        encrypt_message = encrypt_message.upper()
        decrypt_message = ""

        # the same happens like in method encrypt(self, shift_key, message)
        for character in encrypt_message:
            for a in self.alphabet:
                if character == a:
                    index = self.alphabet.index(character)
                    index = (index - shift_key) % 26 # IMPORTANT: By decrypting a message we shift backwards!
                    decrypt_message = decrypt_message + self.alphabet[index]

        return "Encrypt Message is {}, Decrypt Message is {}".format(encrypt_message, decrypt_message)

    # frequency Analysis of words
    def analyseMessage(self, encrypt_message):
        dataset = {} # define dictionary dataset

        # for every character in the encrypt_message mesage we want to get his frequency and then devide to the length of the masseage for getting the frequency in percentage
        for character in encrypt_message:
            character = character.upper()
            dataset[character] = float(dataset.get(character, 0) + 1 / len(encrypt_message) * 100)

        return 'Encrypt Message: ' + encrypt_message + ', ' + str(dataset) # return the enecrypted message and the frquency in percentage in a dictionary


# START THE PROGRAM:

#1. Put in your things into file and the execute it
c = Caesar() # initialise a object of the class Caesar

# print out the methods by giving your arguments
print(c.encrypt(1, "Znveruvbeuvbeubvubeuvbu"))
print(c.decrypt(16, "dLUHKLRUKLRUKRLKRUkLRK"))
print(c.analyseMessage("dLUHKLRUKLRUKRLKRUkLRK"))


#2. Execute File in Python Shell by: execfile('caesar_verschluesslung.py') and the execute the methods in the terminal
