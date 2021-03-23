import turtle
import math

Lisa = turtle.Turtle()
otto = turtle.Turtle()
otto.hideturtle()

def polygon(t ,n , l):
    angle = 360 / n
    for i in range(n):
        t.fd(l)
        t.lt(angle)

def box(t, l):
    if(l < 1):
        t.pu()
        t.fd(100)
        return 0
    t.fd(l)
    t.lt(30)
    t.fd(l)
    t.bk(l)
    t.rt(60)
    t.fd(l)
    t.bk(l)
    t.lt(30)
    box(t, l*0.8)

def square(t, length): # t=Lisa , length=250
    for i in range(4):
        t.fd(length)  # length
        t.lt(94)
    if length < 8: return
    square(t, length * 0.98)

square(Lisa, 300)
# hier wird turtle, namens Lisa, ausgegeben und in der Größe 250


# absoulute werte
# box(otto, 50)

turtle.mainloop()
turtle.bye()

 
