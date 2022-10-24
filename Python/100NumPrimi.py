def controllo(a):
    b=True
    for i in range(2, int(a**0.5)+1):
        if a%i==0: b=False
    return b

l=[i for i in range(1, 100+1) if controllo(i)]
print(l)
