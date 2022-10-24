l=["Gauss", "Conuary", "Eulero", "Hilbert"]
def isGH(a):
    if(a[0]=="G" or a[0]=="H"):
        return True
    else: return False 

l1=[i for i in l if isGH(i)]
print(l1)

#nuovo
print(l[0].upper())

print(l[0].lower())
