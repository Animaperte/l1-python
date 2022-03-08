import turtle

def draw_circle(tur, x, y, radius, color="black"):
    """
    Draws a circle with center at (x, y), radius radius and color color.
    Create your turtle elsewhere and pass it in as tur.
    """
    tur.color(color)
    tur.pu()
    tur.begin_fill()
    tur.goto(x, y - radius)  # -radius because the default circle method starts drawing at the border.
    tur.pd()
    tur.circle(radius)
    tur.end_fill()


screen = turtle.Screen()
screen.title("tk")
screen.setup(1920, 1080)
screen.bgcolor("black")
screen.listen()

# Draw the target
toby = turtle.Turtle()
toby.speed(0)
toby.width(5)
toby.hideturtle()

colord = ['blue', 'green', 'black', 'yellow', 'magenta', 'red']
i = int(input("nombre de cercles"))
zz = 0
radius = 400
while i != 0 and radius > 0:
    draw_circle(toby, 0, 0, radius, colord[zz])
    radius = radius - 10
    zz = zz+1
    if zz == 6:
        zz = 0
    i = i - 1

# Make it all work properly.
turtle.done()