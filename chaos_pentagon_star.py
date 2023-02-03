
import turtle
import random
import math


A = (-242.71,85.32)  # points for the vertices of a pentagon
B = (0.00,261.65)
C = (242.71,85.32)
D = (150.00,-200.00)
E = (-150.00,-200.00)
colors = ['red', 'orange', 'yellow', 'green', 'blue','indigo', 'purple']
t = turtle.Turtle()
#t.speed(0)
t.hideturtle()
scn = turtle.Screen()   
scn.tracer(False)            # make it run really fast
scn.bgcolor('black')
t.pencolor('white')
t.penup()
t.goto(-80,80)
temp = 0
turtle.title('Chaos game pentagon star')
temp2 = 0
for i in range(25000):                 # make 25000 dots (overkill)
    x = random.randint(1,5)
    y = random.randint(0,6)            # set color to random rainbow color

    t.pencolor(colors[y])
    if temp == temp2:
        if abs(x-temp) != 1 :  # skip if the vertex neighbors the last chosen vertex
            if abs(x-temp)!= 4:   # the one off case where abs 1 doesn't catch neighbor(1-5 or 5-1)
                    
                if x == 1:            # choose direction based on vertex
                    dist = t.distance(A)
                    t.setheading(t.towards(A))
                elif x ==2:
                    dist = t.distance(B)
                    t.setheading(t.towards(B))
                elif x == 3:
                    dist = t.distance(C)
                    t.setheading(t.towards(C))
                elif x == 4:
                    dist = t.distance(D)
                    t.setheading(t.towards(D))
                elif x == 5:
                    dist = t.distance(E)
                    t.setheading(t.towards(E))
                t.forward(dist/2)           # jump half the distance to the vertex
                t.pendown()
                t.dot(3)            # place a dot
                t.penup()
                scn.update()
                temp2 = temp        # set temp2 for next time
                temp = x         # reset temp to check if the previous 2 vertices are the same

    else:                   # if the last two vertices were not the same just go halfway to chosen vertex
        if x == 1:
            dist = t.distance(A)
            t.setheading(t.towards(A))
        elif x ==2:
            dist = t.distance(B)
            t.setheading(t.towards(B))
        elif x == 3:
            dist = t.distance(C)
            t.setheading(t.towards(C))
        elif x == 4:
            dist = t.distance(D)
            t.setheading(t.towards(D))
        elif x == 5:
            dist = t.distance(E)
            t.setheading(t.towards(E))
        t.forward(dist/2)
        t.pendown()
        t.dot(3)
        t.penup()
        scn.update()

        temp2 = temp
        temp = x
    if i == 24999:
        print('done')   
        
    
scn.tracer(True)   # reset scn.Tracer to default to avoid future issues
scn.mainloop()      # close out mainloop
