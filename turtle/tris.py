import turtle
finestra = turtle.Screen().bgcolor("black")
SPESSORE = 10
COLOR = "white"
X = 0
Y = 300
B1 = 300
B2 = 600
RAGGIO = 75

def disegna0(x, y):
    oDis= turtle.Turtle()
    oDis.pensize(SPESSORE)
    oDis.speed(0)
    oDis.penup()
    oDis.setposition(x, y)
    oDis.pendown()
    oDis.begin_fill()
    oDis.color(COLOR)
    oDis.circle(RAGGIO)
    oDis.end_fill()
    oDis.penup()
    oDis.setposition(x, y+15)
    oDis.pendown()
    oDis.begin_fill()
    oDis.color("black")
    oDis.circle(RAGGIO-15)
    oDis.end_fill()

def disegnaX(x, y):
    xDis= turtle.Turtle()
    xDis.pensize(SPESSORE)
    xDis.speed('fast')
    xDis.penup()
    xDis.setposition(x, y)
    xDis.pendown()
    xDis.begin_fill()
    xDis.color(COLOR)
    xDis.right(45)
    xDis.forward(200)
    xDis.end_fill()
    #-------------------
    xDis.penup()
    xDis.setposition(x+150, y)
    xDis.pendown()
    xDis.begin_fill()
    xDis.color(COLOR)
    xDis.right(90)
    xDis.forward(200)
    xDis.end_fill()

def printBase(base):
    for i, el in enumerate(base):
        el.pensize(SPESSORE)
        el.speed(0)
        el.penup()
        if i==0:
            el.setposition(X, Y-400)
        elif i==1:
            el.setposition(X, Y-200)
        elif i==2:
            el.setposition(X-100, Y-200)
        elif i==3:
            el.setposition(X+100, Y-200)
        el.pendown()
        
        el.begin_fill()
        el.color(COLOR)
        if i==0:
            el.forward(B1)
            el.backward(B2)
        elif i==1:
            el.forward(B1)
            el.backward(B2)
        elif i==2:
            el.right(-90)
            el.forward(B1-100)
            el.backward(B2)
        elif i==3:
            el.right(-90)
            el.forward(B1-100)
            el.backward(B2)
        el.end_fill()
        


def main():
    n1=input("inserire il nome del primo giocatore: ")
    n2=input("inserire il nome del secondo giocatore: ")
    in1=0; in2=0; v1=False; v2=False
    base=[turtle.Turtle() for _ in range(4)]
    x1 = False; x2 = False; x3 = False; x4 = False; x5 = False; x6 = False; x7 = False; x8 = False; x9 = False
    o1 = False; o2 = False; o3 = False; o4 = False; o5 = False; o6 = False; o7 = False; o8 = False; o9 = False
    #x, y=base.position()
    #print(x, y)
    printBase(base)
    #--------------------------
    esc=False
    while(esc==False):
        c1=False; c2=False; in1=0; in2=0
        while(c1==False):
            in1=int(input(f"{n1} inserisci un numero da 1 a 9 (nella rispettiva casella verra disegnata una 'X': "))
            if in1==1 and (x1==False and o1==False): 
                disegnaX(X-275, Y-25)
                x1=True
                c1=True
            elif in1==2 and (x2==False and o2==False): 
                disegnaX(X-75, Y-25)
                x2=True
                c1=True
            elif in1==3 and (x3==False and o3==False): 
                disegnaX(X+125, Y-25)
                x3=True
                c1=True
            elif in1==4 and (x4==False and o4==False): 
                disegnaX(X-275, Y-225)
                x4=True 
                c1=True       
            elif in1==5 and (x5==False and o5==False): 
                disegnaX(X-75, Y-225)
                x5=True
                c1=True
            elif in1==6 and (x6==False and o6==False): 
                disegnaX(X+125, Y-225)
                x6=True
                c1=True
            elif in1==7 and (x7==False and o7==False): 
                disegnaX(X-275, Y-425)
                x7=True
                c1=True
            elif in1==8 and (x8==False and o8==False): 
                disegnaX(X-75, Y-425)
                x8=True
                c1=True
            elif in1==9 and (x9==False and o9==False): 
                disegnaX(X+125, Y-425)
                x9=True
                c1=True
        if((x1==True and x2==True and x3==True) or (x4==True and x5==True and x6==True) or (x7==True and x8==True and x9==True) or
        (x1==True and x4==True and x7==True) or (x2==True and x5==True and x8==True) or (x3==True and x6==True and x9==True) or 
        (x1==True and x5==True and x9==True) or (x3==True and x5==True and x7==True)):
            v1=True
            esc=True
        while(c2==False and v1==False):
            in2=int(input(f"{n2} inserisci un numero da 1 a 9 (nella rispettiva casella verra disegnata una 'O': "))
            if in2==1 and (x1==False and o1==False): 
                disegna0(X-200, Y-175)
                o1=True
                c2=True
            elif in2==2 and (x2==False and o2==False): 
                disegna0(X, Y-175)
                o2=True
                c2=True
            elif in2==3 and (x3==False and o3==False): 
                disegna0(X+200, Y-175)
                o3=True
                c2=True
            elif in2==4 and (x4==False and o4==False): 
                disegna0(X-200, Y-375)
                o4=True
                c2=True
            elif in2==5 and (x5==False and o5==False): 
                disegna0(X, Y-375)
                o5=True
                c2=True
            elif in2==6 and (x6==False and o6==False): 
                disegna0(X+200, Y-375)
                o6=True
                c2=True
            elif in2==7 and (x7==False and o7==False): 
                disegna0(X-200, Y-575)
                o7=True
                c2=True
            elif in2==8 and (x8==False and o8==False): 
                disegna0(X, Y-575)
                o8=True
                c2=True
            elif in2==9 and (x9==False and o9==False): 
                disegna0(X+200, Y-575)
                o9=True 
                c2=True
        
        if ((o1==True and o2==True and o3==True) or (o4==True and o5==True and o6==True) or (o7==True and o8==True and o9==True) or
        (o1==True and o4==True and o7==True) or (o2==True and o5==True and o8==True) or (o3==True and o6==True and o9==True) or
        (o1==True and o5==True and o9==True) or (o3==True and o5==True and o7==True)):
            v2=True
            esc=True
        elif ((x1==True or o1==True) and (x2==True or o2==True) and (x3==True or o3==True) and (x4==True or o4==True) and (x5==True or o5==True) and (x6==True or o6==True) and (x7==True or o7==True) and (x8==True or o8==True) and (x9==True or o9==True)):
            esc=True

    
    if(v1==True):
        print(f"{n1} vince la partita!")
    elif (v2==True):
        print(f"{n2} vince la partita!")
    else: print(f"nessun vincitore")
    turtle.done()

if __name__ =="__main__": #"__" = Dunder
    main()