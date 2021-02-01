
#!/usr/bin/env python
# -*- coding: latin1 -*-
import sys,os
'''
uso: python3 playfair.py [option]

if 0 then encode
else then decode

Meter en el archivo input:
La clave
El texto a cifrar/descifrar
(Separados entre todos por saltos de linea)

https://es.planetcalc.com/7751/
'''

f = open("input", "r")
data = f.readlines()
key=data[0]
key = key.replace("\n", "")
f.close()
def matrix(x,y,initial):
    return [[initial for i in range(x)] for j in range(y)]
    
result=list()
for c in key: #storing key
    if c not in result:
        if c=='J':
            result.append('I')
        else:
            result.append(c)
flag=0
for i in range(65,91): #storing other character
    if chr(i) not in result:
        if i==73 and chr(74) not in result:
            result.append("I")
            flag=1
        elif flag==0 and i==73 or i==74:
            pass    
        else:
            result.append(chr(i))
k=0
my_matrix=matrix(5,5,0) #initialize matrix
for i in range(0,5): #making matrix
    for j in range(0,5):
        my_matrix[i][j]=result[k]
        k+=1
print("-----------------------------\nMATRIX:")
i=0
while(i<5):
    print(my_matrix[i])
    i+=1
print("-----------------------------\n")
def locindex(c): #get location of each character
    loc=list()
    if c=='J':
        c='I'
    for i ,j in enumerate(my_matrix):
        for k,l in enumerate(j):
            if c==l:
                loc.append(i)
                loc.append(k)
                return loc
            
def encrypt(msg):  #Encryption
    #SALVACION
    #POR NOTICIAS DE FUENTE FIDEDIGNA SABEMOSZ

    msg=msg.replace(" ", "")
    msg = msg.replace("\n", "")             
    i=0
    for s in range(0,len(msg)+1,2):
        if s<len(msg)-1:
            if msg[s]==msg[s+1]:
                msg=msg[:s+1]+'Z'+msg[s+1:]
    if len(msg)%2!=0:
        msg=msg[:]+'Z'
    print("CIPHER TEXT:",end=' ')
    while i<len(msg):
        loc=list()
        loc=locindex(msg[i])
        loc1=list()
        loc1=locindex(msg[i+1])
        if loc[1]==loc1[1]:
            print("{}{}".format(my_matrix[(loc[0]+1)%5][loc[1]],my_matrix[(loc1[0]+1)%5][loc1[1]]),end=' ')
        elif loc[0]==loc1[0]:
            print("{}{}".format(my_matrix[loc[0]][(loc[1]+1)%5],my_matrix[loc1[0]][(loc1[1]+1)%5]),end=' ')  
        else:
            print("{}{}".format(my_matrix[loc[0]][loc1[1]],my_matrix[loc1[0]][loc[1]]),end=' ')    
        i=i+2        
    print("\n")             
def decrypt(msg):  #decryption
    #SALVACION
    #WF QB DP DS OS CI FG SM DQ FG OI KI NE OL AL IH PI CU 
    msg=msg.replace(" ", "")
    msg = msg.replace("\n", "") 
    print("PLAIN TEXT:",end=' ')
    i=0
    while i<len(msg):
        loc=list()
        loc=locindex(msg[i])
        loc1=list()
        loc1=locindex(msg[i+1])
        if loc[1]==loc1[1]:
            print("{}{}".format(my_matrix[(loc[0]-1)%5][loc[1]],my_matrix[(loc1[0]-1)%5][loc1[1]]),end=' ')
        elif loc[0]==loc1[0]:
            print("{}{}".format(my_matrix[loc[0]][(loc[1]-1)%5],my_matrix[loc1[0]][(loc1[1]-1)%5]),end=' ')  
        else:
            print("{}{}".format(my_matrix[loc[0]][loc1[1]],my_matrix[loc1[0]][loc[1]]),end=' ')    
        i=i+2        
    print("\n")

if __name__ == '__main__':
    
    args = sys.argv[1:]
    f = open("input", "r")
    data = f.readlines()
    if len(args) == 1 and args[0] == '0':
        encrypt(data[1])
    elif len(args) == 1:
        decrypt(data[1])
    f.close()
