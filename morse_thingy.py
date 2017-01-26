'''
Created on Dec 24, 2016

@author: Carolina
'''
#import string

def morse(frase):
    alfabeto=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', ' ']
    #alfabeto = string.ascii_lowercase + " "
    
    morse=['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','/']
    
    traducao = ""
    frase=frase.lower()
    for i in range(0,len(frase)):
        c=frase[i]
        posicao= None
        for j in range(0,len(alfabeto)):
            if c == alfabeto[j]:
                posicao=j
                
        if posicao==None:
            print ("Traducao completa impossivel. Foram traduzidos %d." %i)
            return ("Message translated: %s" %traducao)
        
        traducao+=morse[posicao]+"  "

    return ("Message translated: %s" %traducao)


def teste_morse():
    frase=raw_input("Message to translate:")
    return morse(frase)

#print teste_morse()
