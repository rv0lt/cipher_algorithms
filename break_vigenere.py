#!/usr/bin/env python
 # -*- coding: utf-8 -*-

import re
from ic import ic, frequency_analisis
from vigenere import vigenere_dec, vigenere_enc

def get_caesar(index, key, data):
    text = ""
    while index < len(data):
        text += data[index]
        index += key
    return text


def get_divisors(n):
    for i in range(2, int(n / 2) + 1):
        if n % i == 0:
            yield i
    yield n


def kasiski(data,sequence_len,key_len):
    # list to store the distances
    seq_distances = []

    # position in the string where the sequence to find starts
    for index in range(0,len(data)-sequence_len):
        posible_seq = data[index:index + sequence_len]
        repetitions = data.count(posible_seq) # find repetions of such sequence

        # if a sequence is repeated, store the distances from each repetion
        if repetitions > 1:
            # use regex to find the indexs 
            indexs = re.finditer(pattern=posible_seq, string=data)
            indexs = [index.start() for index in indexs]
            # now, we hace the index in the text for every repetition, we can calculate the distances
            for i in range(0,len(indexs)):
                for j in range(i,len(indexs)):
                    if i == j:
                        continue
                    seq_distances.append(indexs[j] - indexs[i])

    # seq_distances has all the distances among the sequences
    # Next step is getting the common factor of the distances retrieved
    distances = [*set(seq_distances)] # use set, to remove duplicate distances
    
    factor_count = {}
    for dis in distances:
        divisors = get_divisors(dis)
        for div in divisors:
            if key_len > 0:
                # if the divisor is higher than the maxium possible key, dont store it
                if div > key_len:
                    continue

            if div in factor_count:
                factor_count[div] += 1
            else:
                factor_count[div] = 1

    # now we print the highest counts
    print("=============\n")
    print("The factor count for the string is:")
    for factor in factor_count:
        print("Factor: " + str(factor) + " has a count of = " + str(factor_count[factor]))
    print("=============\n")    

def hacker(abcd,data,key_len):
    contin = True

    for sequence_size in [3,4,5]:
        if not contin:
            break

        print("Now trying to find sequences of size: " + str(sequence_size))

        kasiski(data,sequence_size,key_len)
        possible_keys = input("\nWhich one of the displayed possible keys lengths would you like to use? \n" + 
                        "Separate them with comas\nEx: 2,8,10 \n")

        possible_keys = possible_keys.split(",")
        for key in possible_keys:
            # trying with each length of key specified
            # get the individual possible caesar ciphers

            print("Trying with key of length: " + key)
            
            caesar_ciphers = []
            for i in range(0,int(key)):
                caesar_ciphers.append(get_caesar(i,int(key),data))
            
            # try each letter of the abcedary to find the best score
            # frequency analysis to break each caesar
            vigenere_key = ""
            for caesar in caesar_ciphers:
                caesar_key = ""
                lowest_difference = 99999 # very high number
                
                for letter in abcd:
                    dec = vigenere_dec(abcd,letter,caesar) # decode the caesar with the given letter to calculate the score
                    score = frequency_analisis(abcd,dec) # score based on the frequency of the letters in the given language
                    if score <= lowest_difference: # if the score is the best so far, save the letter
                        lowest_difference = score
                        caesar_key = letter
                
                vigenere_key += caesar_key

            print("Probable Key of length " + key + " := " + vigenere_key + "\n")
            print("The solved cypertext would be: \n")
            solution = vigenere_dec(abcd,vigenere_key,data)
            print(solution)
            
            keep = input("Continue to do more operations? press Y to continue, else terminate  ")
            keep = keep.lower()
            if keep == 'y':
                continue
            else:
                contin = False
                break



if __name__ == "__main__":
    
    alph = input("Write S for swedish alphabet, else for english : ")
    alph = alph.lower()
    abcd = "abcdefghijklmnopqrstuvwxyz"
    if alph == "s":
        abcd += "åäö"

    data = input("Please enter the text to try to break: ")
    data = data.lower()
    data.replace(" ","")

    key_len = input("Do you know the maxium size of the key? Write the size or -1 if you don't know: ")
    key_len = int(key_len)

    print("\n")
    hacker(abcd,data,key_len)