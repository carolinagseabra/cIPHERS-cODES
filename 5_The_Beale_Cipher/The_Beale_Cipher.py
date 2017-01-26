f1=open('Beale-Treasure.txt', 'r')
num = f1.read().split(",")
numbers=[]
for i in num:
    numbers.append(int(i)-1)
f1.close()
f2 = open('US-Constitution.txt', 'r')
words = f2.read().split()
f2.close()
txt=""
for i in numbers:
    letter=words[i][0]
    txt+=str(letter)
print txt