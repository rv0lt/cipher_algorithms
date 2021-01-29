
#!/usr/bin/env python
# -*- coding: latin1 -*-
import sys,os
'''
uso: python3 porta-bellaso.py [option]

if 0 then encode
else then decode

Meter en el archivo input:
La clave para constuir la tabla de polibius
La clave de la tranposición columnar
El texto a cifrar/descifrar
(Separados entre todos por saltos de linea)

https://www.dcode.fr/adfgvx-cipher
'''
MAGIC ="ADFGVX"

'''
Build the Polibius square with the given secret
'''
def build_table(secret):
    secret = secret.replace("\n", "")
    abcd = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    #secret = secret.lower()
    print("\nWe start building the polibius square: \n  1) " + secret)
    i = 0
    j = len(secret)
    while not ( i == j):
        if secret[i] in abcd:
            abcd.remove(secret[i])
        i+=1
    i = 0
    j = len(abcd)
    while not (i == j):
        secret = secret + abcd[i]
        i+=1
    print("  2) " + secret)
    secret = secret.replace("A", "A1")
    secret = secret.replace("B", "B2")
    secret = secret.replace("C", "C3")
    secret = secret.replace("D", "D4")
    secret = secret.replace("E", "E5")
    secret = secret.replace("F", "F6")
    secret = secret.replace("G", "G7")
    secret = secret.replace("H", "H8")
    secret = secret.replace("I", "I9")
    secret = secret.replace("J", "J0")
    print("  3) " + secret)

    print("__________________________________")
    print("    ADFGVX")
    print("    -------")
    print("A | " + secret[:-30])
    print("B | " + secret[6:-24])
    print("F | " + secret[12:-18])
    print("G | " + secret[18:-12])
    print("V | " + secret[24:-6])
    print("X | " + secret[30:])
    print("__________________________________")
    return secret.lower()


def encode(message, polibius, key):
#AMENOS
#CRIPTA
#Con un poco de paciencia esto se puede leer

    key = key.replace("\n", "")
    # make sort index -> k
    # key = 'cipher' -> k = [0, 4, 3, 2, 1, 2, 5]
    n = len(key)
    k = sorted(range(n), key=lambda i: key[i])

    # encode
    # message = 'I am going' ->
    # s = ['F','A','D','V','A','G','X','X','D','X','F','A','G','D','X','X']
    secret_alphabet1 = build_table (polibius)
    #print(secret_alphabet1)
    s = []
    for c in message.lower():
        if c.isalpha() or c.isdigit():
            row, col = divmod(secret_alphabet1.index(c), 6)
            s += [MAGIC[row], MAGIC[col]]

    print("\nWe have obtain the following output with the polibius square cipher \n" + " ".join(s))

    # reorder
    # reorder index = [0, 6, 12, 4, 10, 3, 9, 15, 1, 7, 13, 2, 8, 14, 5, 11]
    print("\n the indexes for the columnar transposition is:\n  " + key + "\n  " + "".join(str(elem) for elem in k) + "\n")
    print("If we place the output below the numbers and then reorder each column we obtain the following:")
    return ''.join(s[j] for i in k for j in range(i, len(s), n))


def decode(message, polibius, key):
#AMENOS
#CRIPTA
#XFAFFVGAFAGDXDFAAGDDXAADADADAAVAAVVAXVGVXAXGGDVVAAAAGFDDAGGAVDVGDADVFA

    key = key.replace("\n", "")
    # make sort index -> k
    # keyword = 'cipher' -> k = [0, 4, 3, 2, 1, 2, 5]
    n = len(key)
    k = sorted(range(n), key=lambda i: key[i])

    # make reorder index
    # len(message) == 16 ->
    # x = [0, 6, 12, 4, 10, 3, 9, 15, 1, 7, 13, 2, 8, 14, 5, 11]
    print("\n the indexes for the columnar transposition is:\n  " + key + "\n  " + "".join(str(elem) for elem in k) + "\n")
    print("If we place the output below the numbers and then reorder each column we obtain the following:")

    m = len(message)
    x = [j for i in k for j in range(i, m, n)]

    # reorder
    # message = 'FXGAFVXXAXDDDXGA' ->
    # y = ['F','A','D','V','A','G','X','X','D','X','F','A','G','D','X','X']
    y = ['']*m
    for i, c in zip(x, message): y[i] = c
    print(" ".join(y))
    # decode
    # y -> s = ['i','a','m','g','o','i','n','g']
    secret_alphabet1 = build_table (polibius)
   #print(secret_alphabet1)
    s = []
    for i in range(0, m, 2):
        row, col = y[i:i+2]
        s.append(secret_alphabet1[6 * MAGIC.index(row) + MAGIC.index(col)])
    return ''.join(s)



if __name__ == '__main__':
    args = sys.argv[1:]
    f = open("input", "r")
    data = f.readlines()
    if len(args) == 1 and args[0] == '0':
        print (encode(data[2], data[0], data[1]))
    elif len(args) == 1:
        print (decode(data[2], data[0], data[1]))
    f.close()

