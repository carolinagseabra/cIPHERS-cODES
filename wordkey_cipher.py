'''
Created on Dec 27, 2016

@author: Carolina
'''
import string
def wordkey_cipher(message,key):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    cipher= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in range(0, len(key)):
        a=key[i]
        for j in range(0,len(cipher)):
            if a==cipher[j]:
                cipher.remove(a)
                break
            
    cipher = list(key) + cipher 
    traducao = ""
    message=message.lower()
    for i in range(0,len(message)):
        c=message[i]
        posicao= None
        for j in range(0,len(cipher)):
            if c == cipher[j]:
                posicao=j
                traducao+=alphabet[posicao]
        if posicao==None:
                traducao+=c
                
    return ("Message translated: %s" %traducao)

def teste_wordkey_cipher():
    message = raw_input("Message to translate:")
    key=raw_input("Insert key:\nWord must not repeat letters.")
    L_key=list(key)
    if len(L_key) == len(set(L_key)):
        return wordkey_cipher(message, key)
    else:
        print "Key not accepted, please insert key without reapeated letters."
        key=raw_input("Insert key:")
        return wordkey_cipher(message, key)

#print teste_wordkey_cipher()    