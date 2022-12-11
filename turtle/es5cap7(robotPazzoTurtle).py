import turtle
import random #finestra = turtle.Screen()
def impazzito(bob):
    bob.speed(0)
    bob.right(90*((random.randrange((3)+1))+1)) #uguale a randint(0, 3)
    bob.forward(10)

def main():
    bob=turtle.Turtle()
    for k in range(0, (1*60*120)):
        impazzito(bob)
    turtle.done()

if __name__ =="__main__": #"__" = Dunder
    main()