#!/usr/bin/env python
 # -*- coding: utf-8 -*-

'''
uso: python3 ic.py
Haya el Indice de Coincidencia de una cadena de caracteres
'''

from collections import Counter

def frequency_analisis(abcd,data):
    if len(abcd) == 26:
        letter_freq = {'e': 12.70, 't': 9.06, 'a': 8.17, 'o': 7.51, 
                        'i': 6.97, 'n': 6.75, 's': 6.33, 'h': 6.89, 
                        'r': 5.99, 'd': 4.25, 'l': 4.03, 'c': 2.78, 
                        'u': 2.76, 'm': 2.41, 'w': 2.36, 'f': 2.23, 
                        'g': 2.02, 'y': 1.97, 'p': 1.93, 'b': 1.29, 
                        'v': 0.98, 'k': 0.77, 'j': 0.15, 'x': 0.15, 
                        'q': 0.10, 'z': 0.07 }
    else:
        letter_freq = {
                        'a' :  9.38,        'k' :  3.14,        'u' :  1.92,
                        'b' :  1.54,        'l' :  5.28,        'v' :  2.42,
                        'c' :  1.49,        'm' :  3.47,        'w' :  0.14,
                        'd' :  4.70,        'n':  8.54,        'x' :  0.16,
                        'e' : 10.15,        'o' :  4.48,        'y' :  0.71,
                        'f' :  2.03,        'p' :  1.84,        'z' :  0.07,
                        'g' :  2.86,        'q' :  0.02,        'å' :  1.34,
                        'h' :  2.09,        'r' :  8.43,        'ä' :  1.80,
                        'i' :  5.82,        's' :  6.59,        'ö' :  1.31,
                        'j' :  0.61,        't' :  7.69 }
                        
    counter = Counter(data)
    return sum([abs(counter.get(letter,0) * 100 / len(data) - letter_freq[letter]) for letter in abcd ])

def ic(abcd,data):
    res = 0.0
    n = 0.0
    for val in abcd:
        i = data.count(val)
        res += i * (i-1)
        n += i
    if (n == 0.0):
        return 0.0
    else:
        res /= ( n * (n - 1))
        return res

if __name__ == "__main__":
    
    alph = input("Write S for swedish alphabet, else for english : ")
    alph = alph.lower()
    abcd = "abcdefghijklmnopqrstuvwxyz"
    if alph == "s":
        abcd+="åäö"

    data = input("Please enter the text to calculate the IC: ")
    data = data.lower()
    data.replace(" ","")

    print("\n")

    print(ic(abcd,data))