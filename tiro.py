from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200) #posición inicial de la pelota
speed = vector(0, 0)  #la velocidad depende de x y y
targets = [] #inicializa una lista

def tap(x, y): #Función que responde al clic del usuario
    "Respond to screen tap." # Se asegura que solo exista una pelota al jugar
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25

def inside(xy):#Función para verificar que las pelotas estén dentro del juego
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw(): #Función que dibuja las pelotas
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move():
    "Move ball and targets."
    if randrange(40) == 0: #Se genera una posición random en "y" para las pelotas azules
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets: #Aquí se marca la velocidad de las pelotas azules
        target.x -= 0.5

    if inside(ball): #Velocidad en la pelotita roja
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe: #Si la distancia entre la pelota roja y azul es mayor a 13, la pelota azul se conserva
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets: #Si llega una pelota azul llega al otro extremo, se termina el juego
        if not inside(target):
            return

    ontimer(move, 50)

setup(420, 420, 370, 0) #Tamaño de la ventana
hideturtle()
up()
tracer(False)
onscreenclick(tap) #Lee el clic
move()
done()
