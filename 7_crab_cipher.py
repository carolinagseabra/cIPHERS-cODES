def inverter(a):
    if len(a)==0:
        print("nothing to translate")
    else:
        str1=a.split()
        for i in range(len(str1)):
            a=str1[i]
            str1[i] = a[::-1]
        str2 = ' '.join(str1)
        return str2

def teste_inverter():
    msg=raw_input("Message to translate:")
    return inverter(msg)

print teste_inverter()