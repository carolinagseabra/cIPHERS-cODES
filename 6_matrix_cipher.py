import random
import string
def matrixcipher(width,txt):
    if len(txt)%width != 0:
        height= (len(txt)//width)+1
    else:
        height= len(txt)//width
    m_phrase= list(txt)
    for l in range(len(m_phrase)):
        if m_phrase[l]==" ":
            m_phrase[l]="_"
    c=0
    M=[]
    for o in range(height):
        m=[]
        for p in range(width):
            m.append(0)
        M.append(m)
    for i in range(height):
        if c+width<=len(txt):
            for k in range(c, c+width):
                for j in range(width):
                    if M[i][j]!=0: continue
                    letter=m_phrase[k]
                    M[i][j]=letter
                    break
            c+=width
        else:
            for k in range(c, len(txt)):
                for j in range(width):
                    if M[i][j]!=0: continue
                    letter=m_phrase[k]
                    M[i][j]=letter
                    break
            for j in range(width):
                    if M[i][j]!=0: continue
                    M[i][j]=random.choice(string.ascii_letters)
    for row in M:
        print " ".join(map(str,row))
    hide=""
    for i in range(len(M[0])):
        for j in range(len(M)):
            hide+=M[j][i]
    return hide     

def encrypt():
    width=int(input("key:"))
    txt=str(raw_input("message to encrypt:"))
    print matrixcipher(width,txt)

def matrixdecipher(width,txt):
    if len(txt)%width != 0:
        height= (len(txt)//width)+1
    else:
        height= len(txt)//width
    m_phrase= list(txt)
    for l in range(len(m_phrase)):
        if m_phrase[l]=="_":
            m_phrase[l]=" "
    M=[]
    for o in range(height):
        m=[]
        for p in range(width):
            m.append(0)
        M.append(m)
    c=0
    for i in range(width):
        if c+height<=len(txt):
            for k in range(c,len(m_phrase)+c):
                for j in range(height):
                    if M[j][i]!=0: continue
                    M[j][i]=m_phrase[k]
                    break
            c+=height
#     for row in M:
#         print " ".join(map(str,row))
    hide=""
    for i in range(len(M)):
        for j in range(len(M[0])):
            hide+=str(M[i][j])
    return hide

def decrypt():
    key=int(input("key:"))
    txt=str(raw_input("message to decrypt:"))
    print matrixdecipher(key,txt)

def try_auto_decrypt(begin,txt):
    for key in range(1, len(txt)):
        z = matrixdecipher(key,txt)
        if z.startswith(begin):
            return (key, z)
        
def auto_decrypt():
    key=raw_input("key:")
    txt=str(raw_input("message to decrypt:"))
    print try_auto_decrypt(key,txt)
    
#encrypt()    
#decrypt()
auto_decrypt()