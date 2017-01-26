'''
Created on Dec 26, 2016

@author: Carolina
'''
from alphabet_inverter import *
from ceaser_cipher import *
from morse_thingy import *
from wordkey_cipher import *

def mixer_ciphers(choice):
    if (choice=='AI'):
        return teste_alphabet_inverter()
    elif (choice=='CC'):
        return teste_ceaser_encrypt()
    elif (choice=='M'):
        return teste_morse()
    elif (choice=='WkC'):
        return teste_wordkey_cipher()
    else:
        return "CIPHER NOT RECOGNISED"

def get_cipher():
    choice=raw_input("Which cipher do you want to translate to? \nChoose -- 'AI' for Alphabet Inverter; 'CC' for Ceaser Cipher; 'M' for Morse; 'WkC' for Wordkey Cipher")
    print mixer_ciphers(choice)
    
get_cipher()