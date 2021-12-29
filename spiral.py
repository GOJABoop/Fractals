import turtle

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor("black")
t.width(2)
t.speed(0)
t.hideturtle()

colors = ('white', 'pink', 'cyan')

for i in range (300):
    t.pencolor(colors[i % 3])
    t.forward(i * 4)
    t.right(121)

turtle.mainloop()