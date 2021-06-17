# todo 1. draw the map of the farm
# todo 2. set up a set of objects (field, plants, farmer, facilities, tools, enemies, counter)
# todo 3. create interaction methods
# todo 4. create interface elements

# Game Starts here
import turtle
screen = turtle.Screen()
screen.screensize(800, 555)
screen.bgpic('Background.png')

def write_coordinates(X:int, Y:int):
    print(X, Y)

screen.onclick(write_coordinates)

#mainloop - должен быть последним!
screen.mainloop()


#screen.listen()
#turtle_tom = TurtleParent(pos_x=-60, pos_y=-60, t_color="grey")
#turtle_tom.chaser = True
#turtle_jerry = TurtleParent(pos_x=60, pos_y=60, t_color="purple")
#turtle_tuffy = TurtleParent(pos_x=-100, pos_y=230, t_color="black")
#turtle_tuffy.hideturtle()
