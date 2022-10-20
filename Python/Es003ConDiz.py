import random

c=random.randint(0, 3)

def somma(n1, n2):
    f=n1+n2
    return f
def sottrazione(n1, n2):
    f=n1-n2
    return f
def moltiplicazione(n1, n2):
    f=n1+n2
    return f
def divisione(n1, n2):
    f=n1+n2
    return f

    
d={0: somma, 1:sottrazione, 2:moltiplicazione, 3:divisione}
a=int(input("inserire il primo numero: "))
b=int(input("inserire il secondo numero: "))
for i in d:
    if c==i:
     g=d[i]
print(g)
