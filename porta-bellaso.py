#!/usr/bin/env python
# -*- coding: latin1 -*-

'''
uso: python3 porta-bellaso.py

Meter en el archivo input:
La clave
El texto a cifrar/descifrar
(Separados ambos por un salto de linea)

https://www.dcode.fr/porta-cipher
'''
#PROFUNDIS
#CLAMAVIT A DEO

def porta_cipher(key,data):
    
    diccionarios= { 'A':{'A':'N','B':'O','C':'P','D':'Q','E':'R','F':'S','G':'T','H':'U','I':'V','J':'W','K':'X','L':'Y','M':'Z'},
                    'B':{'A':'N','B':'O','C':'P','D':'Q','E':'R','F':'S','G':'T','H':'U','I':'V','J':'W','K':'X','L':'Y','M':'Z'},
                    'C':{'A':'Z','B':'N','C':'O','D':'P','E':'Q','F':'R','G':'S','H':'T','I':'U','J':'V','K':'W','L':'X','M':'Y'},
                    'D':{'A':'Z','B':'N','C':'O','D':'P','E':'Q','F':'R','G':'S','H':'T','I':'U','J':'V','K':'W','L':'X','M':'Y'},
                    'E':{'A':'Y','B':'Z','C':'N','D':'O','E':'P','F':'Q','G':'R','H':'S','I':'T','J':'U','K':'V','L':'W','M':'X'},
                    'F':{'A':'Y','B':'Z','C':'N','D':'O','E':'P','F':'Q','G':'R','H':'S','I':'T','J':'U','K':'V','L':'W','M':'X'},
                    'G':{'A':'X','B':'Y','C':'Z','D':'N','E':'O','F':'P','G':'Q','H':'R','I':'S','J':'T','K':'U','L':'V','M':'W'},
                    'H':{'A':'X','B':'Y','C':'Z','D':'N','E':'O','F':'P','G':'Q','H':'R','I':'S','J':'T','K':'U','L':'V','M':'W'},
                    'I':{'A':'W','B':'X','C':'Y','D':'Z','E':'N','F':'O','G':'P','H':'Q','I':'R','J':'S','K':'T','L':'U','M':'V'},
                    'J':{'A':'W','B':'X','C':'Y','D':'Z','E':'N','F':'O','G':'P','H':'Q','I':'R','J':'S','K':'T','L':'U','M':'V'},
                    'K':{'A':'V','B':'W','C':'X','D':'Y','E':'Z','F':'N','G':'O','H':'P','I':'Q','J':'R','K':'S','L':'T','M':'U'},
                    'L':{'A':'V','B':'W','C':'X','D':'Y','E':'Z','F':'N','G':'O','H':'P','I':'Q','J':'R','K':'S','L':'T','M':'U'},
                    'M':{'A':'U','B':'V','C':'W','D':'X','E':'Y','F':'Z','G':'N','H':'O','I':'P','J':'Q','K':'R','L':'S','M':'T'},
                    'N':{'A':'U','B':'V','C':'W','D':'X','E':'Y','F':'Z','G':'N','H':'O','I':'P','J':'Q','K':'R','L':'S','M':'T'},
                    'O':{'A':'T','B':'U','C':'V','D':'W','E':'X','F':'Y','G':'Z','H':'N','I':'O','J':'P','K':'Q','L':'R','M':'S'},
                    'P':{'A':'T','B':'U','C':'V','D':'W','E':'X','F':'Y','G':'Z','H':'N','I':'O','J':'P','K':'Q','L':'R','M':'S'},
                    'Q':{'A':'S','B':'T','C':'U','D':'V','E':'W','F':'X','G':'Y','H':'Z','I':'N','J':'O','K':'P','L':'Q','M':'R'},
                    'R':{'A':'S','B':'T','C':'U','D':'V','E':'W','F':'X','G':'Y','H':'Z','I':'N','J':'O','K':'P','L':'Q','M':'R'},
                    'S':{'A':'R','B':'S','C':'T','D':'U','E':'V','F':'W','G':'X','H':'Y','I':'Z','J':'N','K':'O','L':'P','M':'Q'},
                    'T':{'A':'R','B':'S','C':'T','D':'U','E':'V','F':'W','G':'X','H':'Y','I':'Z','J':'N','K':'O','L':'P','M':'Q'},
                    'U':{'A':'Q','B':'R','C':'S','D':'T','E':'U','F':'V','G':'W','H':'X','I':'Y','J':'Z','K':'N','L':'O','M':'P'},
                    'V':{'A':'Q','B':'R','C':'S','D':'T','E':'U','F':'V','G':'W','H':'X','I':'Y','J':'Z','K':'N','L':'O','M':'P'},
                    'W':{'A':'P','B':'Q','C':'R','D':'S','E':'T','F':'U','G':'V','H':'W','I':'X','J':'Y','K':'Z','L':'N','M':'O'},
                    'X':{'A':'P','B':'Q','C':'R','D':'S','E':'T','F':'U','G':'V','H':'W','I':'X','J':'Y','K':'Z','L':'N','M':'O'},
                    'Y':{'A':'O','B':'P','C':'Q','D':'R','E':'S','F':'T','G':'U','H':'V','I':'W','J':'X','K':'Y','L':'Z','M':'N'},
                    'Z':{'A':'O','B':'P','C':'Q','D':'R','E':'S','F':'T','G':'U','H':'V','I':'W','J':'X','K':'Y','L':'Z','M':'N'}}
    
    print("Key used is: " + key)
    
    end=False
    res=""
    i_key=0
    i_data=0
    while not end:
        j_key= len(key)
        if i_key==j_key-1:
            i_key = 0
        j_data = len(data)
        if i_data==j_data-1:
            end = True

        dictionary = key[i_key]
        letter = data[i_data]

        print("We use dictionary " + dictionary + " to cipher the letter " + letter)
        letter_ciph = diccionarios.get(dictionary).get(letter)
        if letter_ciph is None:
            aux=diccionarios.get(dictionary)
            letter_ciph=(list(aux.keys())[list(aux.values()).index(letter)])
        res = res+letter_ciph
        print(letter_ciph)
        
        i_key+=1
        i_data+=1

    
    print(res)



f = open("input", "r")
data = f.readlines()
data[1]= data[1].replace(" ", "")
porta_cipher(data[0], data[1])
f.close()
