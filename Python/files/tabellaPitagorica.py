#fare tabellina pitagorica
#scriverlo su un file
def tabellaPitagorica():
    file=open("tabellaPitagorica.txt", "w")
    #l=[i for i in range (0, 11)]
    #print(l)
    #exit()
    
    mat=[[k * i for k in range (0, 11)] for i in range(1, 11)]


    for k in mat:
        for t in k:
            print(t, end=" ")
            file.write(f"{t}\t")
        print(f"\n")
        file.write(f"\n")
        #file.write(f"{k}\n")
        #print(f"{k}\n")
    #exit()
    
    file.close()

def main():
    tabellaPitagorica()

if __name__ =="__main__": #"__" = Dunder
    main()
