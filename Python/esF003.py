def operazione(p1, n1, n2):
    if(p1==0):
        f=n1+n2
    else:
        if(p1==1):
            f=n1-n2
        else:
         if(p1==2):
            f=n1*n2
         else:
          if(p1==3):
            f=n1/n2

    return f

a=int(input("inserire il primo numero: "))
b=int(input("inserire il secondo numero: "))
c=int(input("inserire un numero a seconda dell'operazione (0:somma, 1:sottrazione, 2:moltiplicazione, 3:divisione): "))
solu=operazione(c, a, b)
print(solu)