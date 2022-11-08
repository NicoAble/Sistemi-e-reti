from random import randrange

#fare 10 lanci per alice e bob
#scriverlo su un file

def lancioDadi():
    file=open("lancioDadi.txt", "w")
    #l=[i for i in range (0, 11)]
    #print(l)
    #exit()

    mat=[[(randrange(5)+1) for i in range(0, 11)]for k in range(0, 2)]
    print(mat)
    c=0
    for f in mat:
        if c==0:
            lista_Alice=f
        else: lista_Bob=f
        c+=1
    for k, v in zip(lista_Alice, lista_Bob):
        print(f"{k} , {v}\n")
        file.write(f"{k} , {v}\n")

    #exit()
    file.close()

def main():
    lancioDadi()

if __name__ =="__main__": #"__" = Dunder
    main()