a=int(input("inserire un numero: "))

if(a%2==0 or a%3==0 or a%5==0):
    if a%2==0:
     print("e' divisibile per 2")
    if a%3==0:
     print("e' divisibile per 3")
    if a%5==0:
     print("e' divisibile per 5")
else:
    print("non e' divisibile per nessuno")