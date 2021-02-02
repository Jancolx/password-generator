import random
symbol="@#$%"
n="123456"
smal="abcdefghijklmnopqrst"
bigal="QWERTYUIOPASDFGHJKLZXCVBNM"
passlen = int(input("Enter the length of password :  "))
if(passlen<4):
    print("Please enter password len grater than 4 and to make a strong pass length should minim 8")
passlen=int(passlen/4)
p = (random.sample(symbol, passlen))+(random.sample(n, passlen))+(random.sample(smal, passlen))+(random.sample(bigal, passlen))
p="".join(p)
print(p)