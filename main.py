# todo 1. draw the map of the farm
# todo 2. set up a set of objects (field, plants, farmer, facilities, tools, enemies, counter)
# todo 3. create interaction methods
# todo 4. create interface elements
# todo 5. create gifs for progress bar and locate near the hole
# todo 7.Добавить к игре функции полива на левую кнопку мыши и посадки/сбора урожая на правую.
# todo 8.На раунд даётся фиксированное количество времени (минута, например). Цель -- набрать максимальное число очков.
# todo 9.Очки начисляются за собранные морковки, чем она спелее, тем лучше.
#        После максимальной спелости морковка начинает сохнуть, и число очков за неё уменьшается.

# todo actions: 1. Сажать морковку - левая клавиша мышки
# todo actions: 2. Собирать морковку - левая клавиша мышки
# todo actions: 3. Поливать лунку - правая клавиша мышки


# Game Starts here
import turtle
from objects import *


screen = turtle.Screen()
screen.screensize(800, 555)
screen.bgpic('Background.png')
screen.colormode(255)

def write_coordinates(X:int, Y:int):
    print((X, Y))

# screen.onclick(write_coordinates)

hole_list_upper_left_coordinates = [(-281.0, 92.0), (-254.0, 200.0), (-191.0, 211.0), (-219.0, 169.0), (-259.0, 133.0), (-222.0, 113.0),
                                    (-255.0, 56.0)]

hole_list_bottom_left_coordinates = [
(-332.0, -99.0),
(-317.0, -8.0),
(-299.0, -54.0),
(-259.0, -26.0),
(-267.0, -92.0),
 (-228.0, -59.0),
 (-219.0, -118.0),
 (-168.0, -69.0),
 (-164.0, -135.0),
 (-115.0, -93.0),
 (-97.0, -161.0),
 (-70.0, -125.0),
 (-21.0, -117.0)]

hole_list_right_coordinates = [(-5.0, 54.0), (67.0, 89.0), (116.0, 90.0)]


screen.tracer(0)
screen.update()


#создаём лунки
hole_list_all = []

for hole in hole_list_upper_left_coordinates: hole_list_all.append(Hole(hole[0], hole[1]))
for hole in hole_list_bottom_left_coordinates: hole_list_all.append(Hole(hole[0], hole[1]))
for hole in hole_list_right_coordinates: hole_list_all.append(Hole(hole[0], hole[1]))

for i in range(10): hole_list_all[4].water(); time.sleep(1); screen.update()

carrot1 = Carrot()
carrot2 = Carrot()
hole_list_all[4].plant_plant(carrot1)
hole_list_all[2].plant_plant(carrot2)

screen.update()

def plant_carrot(X:int, Y:int):
    """ Функция посадки моркови """
# Функция принимает координаты щелчка по экрану и проверяет их с областью лунки, устанавливает лунку для посадки и сажает в неё мокровку



screen.onclick(plant_carrot)


game_continues = False
while game_continues:
    time.sleep(TIME_REFRESH)


    #for i in range(1): hole_list_upper_left[4].water(); time.sleep(0.5)

    for i in range(15):
        carrot1.grow_plant()
#        indicator1.water_indicator_status(hole_list_upper_left[4].watered_degree)
        screen.update()
        print(f"Plant has grown for {i}")
        time.sleep(2)

    carrot1.reap_plant()
    #hole_list_upper_left[4].clean_hole()

    # for i in range(0,15):
    #     for hole in hole_list_upper_left:
    #         hole.water()
    #         time.sleep(0.05)
    #
    # for i in range(0,15):
    #     for hole in hole_list_upper_left:
    #         hole.fertilize()
    #         time.sleep(0.05)
    #
    # for i in range(0,15):
    #     for hole in hole_list_upper_left:
    #         hole.defertilize()
    #         time.sleep(0.05)

    screen.update()








#mainloop - должен быть последним!
screen.mainloop()

#screen.listen()
#turtle_tom = TurtleParent(pos_x=-60, pos_y=-60, t_color="grey")
#turtle_tom.chaser = True
#turtle_jerry = TurtleParent(pos_x=60, pos_y=60, t_color="purple")
#turtle_tuffy = TurtleParent(pos_x=-100, pos_y=230, t_color="black")
#turtle_tuffy.hideturtle()
