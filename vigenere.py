#!/usr/bin/env python
 # -*- coding: utf-8 -*-
import os, sys
'''
uso: python3 vigenere.py

You will cipher/decipher the given text with the given key in key-autokey mode
https://www.dcode.fr/cifrado-vigenere
'''

def ask_inputs():

    alph = ""
    input_string = ""
    key = ""

    # Takes string from user
    alph = input("Write S for swedish alphabet, else for english : ")
    alph = alph.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if alph == "s":
        alphabet+="åäö"

    # Takes key from user
    key = input("Please enter encryption key: ")
    key = key.lower()

    # Takes string from user
    input_string = input("Please enter a string of text: ")
    input_string = input_string.lower()

    return alphabet,key,input_string


def vigenere_enc():

    enc_string = ""
    alphabet,enc_key,input_string = ask_inputs()

    # Lengths of input_string
    string_length = len(input_string)

    # Expands the encryption key to make it longer than the inputted string
    expanded_key = enc_key
    expanded_key_length = len(expanded_key)

    while expanded_key_length < string_length:
        # Adds another repetition of the encryption key
        expanded_key = expanded_key + enc_key
        expanded_key_length = len(expanded_key)

    key_position = 0
    alph_len = len(alphabet)

    for letter in input_string:
        if letter in alphabet:
            # cycles through each letter to find it's numeric position in the alphabet
            position = alphabet.find(letter)
            # moves along key and finds the characters value
            key_character = expanded_key[key_position]
            key_character_position = alphabet.find(key_character)
            key_position = key_position + 1
            # changes the original of the input string character
            new_position = position + key_character_position
            if new_position > alph_len:
                new_position = new_position - alph_len
            new_character = alphabet[new_position]
            enc_string = enc_string + new_character
        else:
            enc_string = enc_string + letter
    print("The solution is: \n" + enc_string.upper())
    #print(enc_string)


def vigenere_dec():

    dec_string = ""
    alphabet,dec_key,input_string = ask_inputs()

    # Lengths of input_string
    string_length = len(input_string)

    # Expands the encryption key to make it longer than the inputted string
    expanded_key = dec_key
    expanded_key_length = len(expanded_key)

    while expanded_key_length < string_length:
        # Adds another repetition of the encryption key
        expanded_key = expanded_key + dec_key
        expanded_key_length = len(expanded_key)

    key_position = 0
    alph_len = len(alphabet)

    for letter in input_string:
        if letter in alphabet:
            # cycles through each letter to find it's numeric position in the alphabet
            position = alphabet.find(letter)
            # moves along key and finds the characters value
            key_character = expanded_key[key_position]
            key_character_position = alphabet.find(key_character)
            key_position = key_position + 1
            # changes the original of the input string character
            new_position = position - key_character_position
            if new_position > alph_len:
                new_position = new_position + alph_len
            new_character = alphabet[new_position]
            dec_string = dec_string + new_character
        else:
            dec_string = dec_string + letter
    print("The solution is: \n" + dec_string.upper())



if __name__ == "__main__":
    args = sys.argv[1:]
    contin=True
    while contin:
        
        # ask for code or decode
        operation = input("Write D for Decode Operation, else for Code operation: ")
        operation = operation.lower()

        if operation == "d":
            vigenere_dec()
        else:
            vigenere_enc()

        keep = input("Continue to do more operations? press Y to continue, else terminate  ")
        keep = keep.lower()
        if not (keep == 'y'):
            contin=False

