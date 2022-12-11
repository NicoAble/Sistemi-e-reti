import turtle
finestra = turtle.Screen()
x=-500
y=150

def stampaBob(i, bob, c, c1):
    bob.pensize(10)
    bob.penup()
    if(c1<=4):
        bob.setposition(x+c, y)
    else: bob.setposition(x+c, y-150)
    bob.pendown()
    bob.begin_fill()
    for _ in range (0, i):
        bob.forward(360/i)
        bob.right(360/i)
    bob.color("violet")
    bob.end_fill()
    

def main():
    c=0
    c1=0
    tartarughe=[turtle.Turtle() for _ in range(9)]
    for i, bob in enumerate(tartarughe):
        c+=150
        bob.speed(4.5)
        stampaBob((i+3), bob, c, c1)
        c1+=1
        if(c1==5):
            c=85
    turtle.done()

if __name__ =="__main__": #"__" = Dunder
    main()