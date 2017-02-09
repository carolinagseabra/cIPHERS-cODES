import random
import string
def encrypt_melro(msg):
    L_msg=list(msg)
    L_encrypt=list(msg)
    for i in range(len(L_msg)):
        letter=random.choice(string.ascii_letters)
        L_encrypt.insert(1+i*2, letter)
    encrypt=""
    for pos in L_encrypt:
        encrypt+= " ".join(map(str,pos))
    return encrypt

def decrypt_melro(msg):
    L_msg=list(msg)
    L_decrypt=L_msg[::2]
    decrypt=""
    for pos in L_decrypt:
        decrypt+= " ".join(map(str,pos))
    return decrypt

def melro():
    choice=raw_input("Encrypt or Decrypt?")
    while choice!="Encrypt" and choice!="Decrypt":
        choice=raw_input("Must enter 'Encrypt' or 'Decrypt'./nEncrypt or Decrypt?")
    if choice=="Encrypt":
        msg=raw_input("Enter message to encrypt:")
        return encrypt_melro(msg)
    else:
        msg=raw_input("Enter message to decrypt:")
        return decrypt_melro(msg)
    
print melro()