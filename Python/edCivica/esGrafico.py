import matplotlib.pyplot as plt
import csv

def leggiFile(nome_file):
    file=open(nome_file, "r")
    lista_righe= file.readlines()
    print(lista_righe)
    file.close()
    
    diz_mat={"mese":[], "temperatura":[], "giacca":[], "scuola":[], "videogame":[]} #id sono numeri, nomi sono stringhe 
    for riga in lista_righe[1:]:
        if(riga[-1]=="\n"):
            riga_senza_linefeed=riga[:-1] #senza \n
        else: riga_senza_linefeed=riga
        #print(riga_senza_linefeed)
        lista_campi=riga_senza_linefeed.split(",")
        diz_mat["mese"].append(lista_campi[0])
        diz_mat["temperatura"].append(lista_campi[1])
        diz_mat["giacca"].append(lista_campi[2])
        diz_mat["scuola"].append(lista_campi[3])
        diz_mat["videogame"].append(lista_campi[4])
    return diz_mat


def createG(diz):
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1)
    fig.suptitle('temperature medie')

    ax1.plot(diz["mese"], diz["temperatura"], 'o-g')
    ax1.set_xlabel('Mese')
    ax1.set_ylabel('temperature')

    ax2.plot(diz["mese"], diz["giacca"], 'o-r')
    ax2.set_xlabel('Mese')
    ax2.set_ylabel('giorni con giacca')

    ax3.plot(diz["mese"], diz["scuola"], 'o-b')
    ax3.set_xlabel('Mese')
    ax3.set_ylabel('giorni a scuola')

    ax4.plot(diz["mese"], diz["videogame"], 'o-y')
    ax4.set_xlabel('Mese')
    ax4.set_ylabel('giorni videogame')

    plt.show()

def main():
    diz=leggiFile("dati.csv")
    print(diz)
    createG(diz)
    
    

if __name__ == "__main__":
    main()