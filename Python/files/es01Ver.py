def leggiFile(nome_file):
    file=open(nome_file, "r")
    lista_righe= file.readlines()
    print(lista_righe)
    file.close()
    
    diz_mat={"data":[], "cognome":[], "quota":[]} #id sono numeri, nomi sono stringhe 
    #print(diz_mat)
    #exit()
    sommaTot=2200
    sommaPTot=100
    sommaP=0
    somma=0
    for riga in lista_righe[1:]:
        if(riga[-1]=="\n"):
            riga_senza_linefeed=riga[:-1] #senza \n
        else: riga_senza_linefeed=riga
        #print(riga_senza_linefeed)
        lista_campi=riga_senza_linefeed.split(";")
        #print(lista_campi)
        data=lista_campi[0]
        cognome=lista_campi[1]
        quota=lista_campi[2]
        #print(id, nome)
        diz_mat["data"].append(data)
        diz_mat["cognome"].append(cognome)
        diz_mat["quota"].append(quota)
        somma+=int(quota)
        if(cognome=="Abello"):
            sommaP+=int(quota)

    #print(somma)
    if somma==sommaTot:
        print(f"totale corretto")
    else:
        if somma>sommaTot: 
            print(f"sono presenti {somma-sommaTot} euro in più")   
        else: print(f"sono presenti {sommaTot-somma} euro in meno")

    if(sommaP==sommaPTot): print(f"pagato tutta la quota")
    else: print(f"controllare la quota versata")   


    return diz_mat

def main():
    diz=leggiFile("4AROB_GITA.csv")
    #print(diz)

if __name__ =="__main__":
    main()

