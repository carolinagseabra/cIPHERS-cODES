'''
Created on Dec 26, 2016

@author: Carolina
'''
def alphabet_inverter(frase):
    alfabeto=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    #alfabeto = string.ascii_lowercase + " "
    
    alphabet_inverter=alfabeto[::-1]
    traducao = ""
    frase=frase.lower()
    for i in range(0,len(frase)):
        c=frase[i]
        posicao= None
        for j in range(0,len(alfabeto)):
            if c == alfabeto[j]:
                posicao=j
                traducao+=alphabet_inverter[posicao]
        if posicao==None:
                traducao+=c
                
    return ("Message translated: %s" %traducao)

def teste_alphabet_inverter():
    frase=raw_input("Message to translate:")
    return alphabet_inverter(frase)

#print teste_alphabet_inverter()
