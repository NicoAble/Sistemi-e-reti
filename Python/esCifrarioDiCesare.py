alfabeto= {"a": "b", "b": "c", "c":"d", "d":"e", "e": "f", "f":"g", "g":"h", "h":"i", "i":"l", "l":"m", "m":"n", "n":"o", "o":"p", "p":"q", "q":"r", "r":"s", "s":"t", "t":"u", "u":"v", "v":"z", "z":"a", " ":" "}
frase=input("inserire una frase: ")
frase1= ''
frase2= ''
for lettera in frase:
    frase1+=alfabeto[lettera]
print(frase1)

decodificatore={} #dizionario vuoto

for k,v in alfabeto.items(): #ciclo for simultaneo
    print(k, v)
    decodificatore[v]=k
    print(decodificatore)


for lettera in frase1:
    frase2+=decodificatore[lettera]
print(f"il messaggio decriptato: {frase2}")