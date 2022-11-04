lista= ["a", "b", "c", "d"]
lista1= [1, 2, 3, 4]

# for su lista1 c.style
for i in range(0, len(lista1)):
    print(lista1[i])
# for su lista1 python.style
for k in lista1:
    print(k)
# for su lista1 enumerate
for indice, elemento in enumerate(lista1):
    print(elemento)
# for su lista1, lista2 python.style (zip)
for k, v in zip(lista, lista1):
    print(k, v)
# for su lista1, lista2 c.style (range)
for k in range(0, len(lista)):
    print(lista[k], lista1[k])

diz={"a":1, "b":2, "c":3, "d":4}

# for su diz usanto items()
for k, v in diz.items():
    print(k, v)
# for su diz senza items()
for k in diz:
    print(k, diz[k])
