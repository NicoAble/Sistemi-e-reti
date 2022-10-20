lista= [106, 12, 34, 214]
 #modo predefinito (pythonico)

for elemento in lista:
    print(elemento)

#modo C-style

for i in range(0, len(lista)):
    print(lista[i], end=" pablo\n")

#max e min
max=lista[0]
min=lista[0]

for elemento in lista[1:]:
    if elemento>max:
        max=elemento
    else:
        pass
    if elemento<min:
        min=elemento

print(min, max)