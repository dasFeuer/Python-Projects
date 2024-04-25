import turtle 
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ["yellow", "blue", "green", "red", "black", "pink", "purple", "brown", "cyan", "orange"]

def getNumberOfRacers():
    racers = 0
    while True:
        racers = input('Enter the number of racer (2 - 10): ')
        if racers.isdigit():
            racers = int(racers)
        else:
            print('Input is not numeric... Try Again!')
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print('Number not in range 2-10, Try again!')

def race(colors):
    turtles = createTurtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]
            

def initTurtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing!')


def createTurtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i , color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles


racers = getNumberOfRacers()
initTurtle()


random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print(f"The winner is the turtle with color: {winner}")
time.sleep(5)


# racer = turtle.Turtle()
# racer.speed(1)
# racer.penup()
# racer.shape('turtle')
# racer.color('cyan')
# racer.forward(100)
# racer.left(90)
# racer.pendown()
# racer.forward(100)
# racer.right(90)
# racer.backward(100)
