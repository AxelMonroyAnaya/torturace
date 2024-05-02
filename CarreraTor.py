import turtle
scr = turtle.Screen()
def pintarL(forw,lef):
    dib.hideturtle()
    dib.penup()
    dib.goto(forw, lef)#600,-420
    dib.begin_fill()
    for i in range(4):
        dib.forward(890) #890
        dib.left(90)      #90
        dib.penup()
    dib.end_fill()
    dib.home()

def start():
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.end_fill()
def clou(x,y):
    dib.goto(x,y)
    #dib.showturtle()
    #dib.speed(2)
    dib.begin_fill()
    dib.fillcolor("lightblue")
    dib.circle(50)
    dib.right(30)
    dib.fd(90)
    dib.circle(100)
    #dib.lt(100)
    dib.right(30)
    dib.end_fill()
    dib.home()


class Jugadores():

    def __init__(self):
        self.tor = turtle.Turtle()
        self.tor.speed(10)
        self.tor.pensize(3)
        self.tor.shapesize(4)
        self.tor.lt(90)

    def estilo(self, color1, color2, colorpluma, figura):
        self.tor.color(color1, color2)
        self.tor.pencolor(colorpluma)
        self.tor.shape(figura)

    def goT(self, x, y):
        self.tor.goto(x, y)

    def movI(self):
        self.tor.home()

    def fd(self, x):
        self.tor.fd(x)

    def goals(self):
        self.tor.penup()
        self.fd(680)
        self.tor.pendown()
        self.tor.setheading(180)
        self.tor.circle(70)
        self.tor.setheading(90)
    def pos1(self):
        self.tor.penup()
        self.tor.goto(-350, -300)
        self.tor.pendown()

    def pos2(self):
        self.tor.penup()
        self.tor.goto(450, -300)
        self.tor.pendown()

dado = (-1, -1, 0, 1, 2, 3)
scr.title("CARRERA DE TORTUGAS")
scr.bgcolor("green")
dib = turtle.Turtle()
scr.setup(width=1.0, height=1.0)
dib.fillcolor("#3e2723")
dib.begin_fill()
dib.speed(10)
pintarL(-1490, -420)
pintarL(600,-420)
#start()
clou(-730, -400)
clou(-600, -450)
clou(600, -400)
clou(600, 400)
clou(0, 400)
clou(90, 450)
clou(-780, 400)

tur1 = Jugadores()
tur2 = Jugadores()
tur1.pos1()
tur1.estilo("red","blue","black","turtle")
tur2.estilo("blue","pink","white","turtle")
tur2.pos2()
tur1.goals()
tur2.goals()
tur1.pos1()
tur2.pos2()

###############
def turns():
    nom1 = input("\ningresa el nombre del jugador 1: ")
    nom2 = input("\ningresa el nombre del jugador 2: " )
    print("para ver quien ira primero...")
    while True:
        res1= int(input(f"\n{nom2} ingresa  un numero del 1 al 10"))
        res2= int(input(f"\n{nom1} ingresa un numero del 1 al 10"))
        if (res1 in range(1, 11) and res2 in range(1, 11)):
            print(f"{nom1} ha ingresado el numero {res1}\n y {nom2} ha ingresado el numero: {res2}")
            break
        else:
            print("\nel numero ingresado no es del 1 al 10, intenta de nuevo...\n")
    if res1<res2:
        pass
################

while True:
    res = int(input("ingresa 1 para empezar el juego..\\n ingresa "
                    "teclea culaquier otra tecla para salir"))
    if res == 1:
        print("bienvenido a carrera de tortugas..\n")
        turns()
        break

#tur1.movI()


scr.exitonclick()
