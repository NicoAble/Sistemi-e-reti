n=int(input("inserisci un numero"))
s=[1]
s1=s*n
s1[0], s1[-1]=0, 0
print(s1)
