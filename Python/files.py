def leggiFile(nome_file):
    file=open(nome_file, "r")
    lista_righe= file.readlines()
    print(lista_righe)
    file.close()
    
    diz_mat={"id":[], "nomi":[]} #id sono numeri, nomi sono stringhe 
    #print(diz_mat)
    #exit()
    for riga in lista_righe[1:]:
        if(riga[-1]=="\n"):
            riga_senza_linefeed=riga[:-1] #senza \n
        else: riga_senza_linefeed=riga
        #print(riga_senza_linefeed)
        lista_campi=riga_senza_linefeed.split(",")
        #print(lista_campi)
        id=int(lista_campi[0])
        nome=lista_campi[1]
        #print(id, nome)
        diz_mat["id"].append(id)
        diz_mat["nomi"].append(nome[1:])
    return diz_mat
def scorriDiz(id, diz):
    for k,v in diz.items():
        if k==id:
            n=v
    return n


diz=leggiFile("./matematici.csv")
print(diz)
id=input("inserisci l'id: ")
nome=scorriDiz(id, diz)
print(nome)
