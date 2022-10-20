dizionario= {"w":"avanti", "a":"sinistra", "s":"indietro", "d":"destra",
"i":"avanti", "j":"sinistra", "k":"indietro", "l":"destra"}
d1=[]
comando="avanti"
for chiave in dizionario:
    if dizionario[chiave]==comando:
        d1.append(chiave)
print(d1)
d1=[]
for chiave, azione in dizionario.items():
    if azione==comando:
        d1.append(chiave)
print(d1)