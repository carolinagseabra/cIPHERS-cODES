'''
Created on Dec 26, 2016

@author: Carolina
'''
def ceaser_encrypt(key,message):
    cipher=""
    for i in range(len(message)):
        b=message[i]
        if (97<=ord(b)<=122):
            a=chr((ord(b)-ord('a')+key)%26+ord('a'))
            cipher+=a
        else:
            cipher+=b
    return ("Message translated: %s" %cipher)

def teste_ceaser_encrypt():
    message = get_message()
    key = get_key()
    return ceaser_encrypt(key,message)

def get_key():
    key=raw_input("Insert key (1-26):")
    if key.isdigit():
        if (int(key) >= 1) and (int(key)<= 26):
            return int(key)
    return get_key()
def get_message():
    message = raw_input("Message to translate:")
    return message.lower()

#print teste_ceaser_encrypt()
