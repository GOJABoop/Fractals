import turtle

def drawTriangule(points,t):
    t.fillcolor('white')
    t.up()
    t.goto(points[0][0],points[0][1])
    t.down()
    t.begin_fill()
    t.goto(points[1][0],points[1][1])
    t.goto(points[2][0],points[2][1])
    t.goto(points[0][0],points[0][1])
    t.end_fill()

def half(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points,grade,t):
    drawTriangule(points,t)
    if grade > 0:
        sierpinski( [points[0], 
                    half(points[0], points[1]), 
                    half(points[0], points[2])],
                    grade-1, t)
        sierpinski( [points[1],
                    half(points[0], points[1]),
                    half(points[1], points[2])],
                    grade-1, t)
        sierpinski( [points[2],
                    half(points[2], points[1]),
                    half(points[0], points[2])],
                    grade-1, t)

def main():
   t = turtle.Turtle()
   screen = turtle.Screen()
   t.hideturtle()
   t.speed(0)
   points = [[-200,-100],[0,200],[200,-100]]
   sierpinski(points,5,t)
   screen.exitonclick()

main()
