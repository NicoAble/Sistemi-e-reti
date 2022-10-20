def controllo(a, b):
    for i in range(2, int(a**0.5)+1):
        if a%i==0: b=False
    return b

a=int(input("inserire un numero: "))
b=True
c=controllo(a, b)
if c==True: print("numero primo")
else: print("non primo")