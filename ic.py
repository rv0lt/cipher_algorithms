#!/usr/bin/env python
 # -*- coding: latin1 -*-

'''
uso: python3 ic.py
Meter el string  en el archivo input
Haya el Indice de Coincidencia de una cadena de caracteres
'''
#AUGEZYXUELZKYVJJERMWZMPSPACUHAIYQVORBBKSBEFZFTRDYTFIIGEWEKLKFXELKJYLDMW

def ic(self):
    res = 0.0
    n = 0.0
    abcd="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    abcd=list(abcd.strip())
    print(abcd)
    for val in abcd:
        i = self.count(val)
        j = i * (i-1)
        print(str(val) + ":=" + str(i) + "  // " + str(i-1) + " ==> " + str(j))
        res += j
        n += i
    if (n == 0.0):
        return 0.0
    else:
        print("\n")
        print(res)
        res = res / ( n * (n - 1))
        print("\n")
        print(res)


f = open("input", "r")
data = f.read()
data=data.replace(" ", "")
ic(data)
f.close()
