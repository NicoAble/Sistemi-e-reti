def leggi_file(nome_file):
    """La funzione legge i file"""

    file = open(nome_file, "r")

    #per leggere un file e salvare le righe in una lista
    lista_righe = file.readlines()

    #print(lista_righe)

    file.close()

    diz = {"data":[], "nome":[], "euro_versati":[]}

    for riga in lista_righe[1:]:
        #per stampare riga per riga senza andare a capo 2 volte
        riga_senza_linefeed = riga[:-1]
        lista_campi = riga_senza_linefeed.split(",") #è un metodo, la virgola è il separatore
        #.split è come l'strtok su c
        data = int(lista_campi[0])
        nome = lista_campi[1]
        euro_versati = int(lista_campi[2])
        diz["data"].append(data)
        diz["nome"].append(nome[1:])
        diz["euro_versati"].append(euro_versati)
    
    return diz

def printIncassi(diz):
    for k in diz:
        totInc = totInc + diz["euro_versati"][k]
    
    if totInc >= 2200:
        print(f"Si è raggiunta la cifra richiesta")
    else:
        anomalia = 2200 - totInc
        print(f"Non si è raggiunta la cifra richiesta per {anomalia} euro")


def cercaNome(diz):
    new_diz = {"nome":[], "quota":[]}

    for k in diz:
        if "Gallo" == new_diz["nome"][k]:
            quota = quota + diz["euro_versati"][k]
            new_diz["quota"].append(quota)
            if new_diz["quota"] == 100:
                print(f"Ho pagato tutto")


diz = leggi_file("4AROB_GITA.csv")

printIncassi(diz)
cercaNome(diz)

print(diz)