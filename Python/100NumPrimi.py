def controllo(a, b):
    for i in range(2, int(a**0.5)+1):
        if a%i==0: b=False
    return b

c=True
l=[i*(if controllo(i, c)==True) for i in range(1, 100+1)]
print(l)