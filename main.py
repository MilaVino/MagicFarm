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
# import turtle
from objects import *
from constants import *
import random


screen = turtle.Screen()
screen.listen()
screen.screensize(800, 555)
screen.bgpic('Background.png')
screen.colormode(255)

time_remaining = TIME_GAME
score = turtle.Turtle()
score.hideturtle()
score.penup()
score.setposition(0, 400)
score.write(f"Счёт: 0, осталось времени - {round(time_remaining,1)}")


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

# for i in range(10): hole_list_all[4].water(); time.sleep(1); screen.update()

# carrot1 = Carrot()
# carrot2 = Carrot()
# hole_list_all[4].plant_plant(carrot1)
# hole_list_all[2].plant_plant(carrot2)

screen.update()

def restart_game():
    global game_continues
    global time_remaining
    # global reap_plant_counter
    game_continues = True
    time_remaining = TIME_GAME
    # reap_plant_counter = 0

def plant_carrot(X:int, Y:int, self=None):
    """ Функция посадки моркови """
# Функция принимает координаты щелчка по экрану и проверяет их с областью лунки, устанавливает лунку для посадки и сажает в неё мокровку
    mouse_clicked = (X, Y)
    min_distance_to_hole:int = 1000000
    hole_selected: Hole
    for hole in hole_list_all:
        current_distance = hole.distance(mouse_clicked)
        if current_distance < min_distance_to_hole: min_distance_to_hole = current_distance; hole_selected = hole

    if hole_selected.distance(mouse_clicked) <= HOLE_HIT_RADIUS:
        if not hole_selected.plant:
            hole_selected.plant_plant(Carrot())
            print(hole_selected.position())
        else:
            global reap_plant_counter # обращаемся к счетчику как глобальной переменной
            reap_plant_counter += hole_selected.plant.reap_plant() # увеличиваем счетчик очков на величину спелости собранного овоща
            print(reap_plant_counter, "- current score") # выводим в консоль количество собранного урожая в очках
            hole_selected.clean_hole()
            # print(f"Hole {hole_selected} is busy")

        # print(hole_selected.plant)

def plant_water(X:int, Y:int):
    """ Функция полива лунки """
# Функция принимает координаты щелчка по экрану и проверяет их с областью лунки, устанавливает лунку для полива и увеличивает уровень
    mouse_clicked = (X, Y)
    min_distance_to_hole:int = 1000000
    hole_selected: Hole
    for hole in hole_list_all:
        current_distance = hole.distance(mouse_clicked)
        if current_distance < min_distance_to_hole: min_distance_to_hole = current_distance; hole_selected = hole

    if hole_selected.distance(mouse_clicked) <= HOLE_HIT_RADIUS:
        hole_selected.water()
        # print(hole_selected.plant)


screen.onclick(plant_carrot, btn=1)
screen.onclick(plant_water, btn=3)

screen.onkey(key="R", fun=restart_game)
screen.onkey(key="r", fun=restart_game)
# screen.listen()


big_game_continues = True
game_continues = True
reap_plant_counter = 0

while big_game_continues:

    while game_continues:
        score.clear()
        score.write(f"Счёт: {reap_plant_counter}, осталось времени - {round(time_remaining,1)}", align="center", font=("Arial", 12, "bold"))
        time.sleep(TIME_REFRESH)
        time_remaining -= TIME_REFRESH
        if time_remaining <= 0:
            game_continues = False
            break

        for hole in hole_list_all:
            if hole.plant:
                if random.randint(0, 20) == 5:
                    hole.plant.grow_plant()

        screen.update()

    score.clear()
    score.write(f"Игра завершена. Вы набрали {reap_plant_counter} очков! Нажмите R - начать заново, C - продолжить раунд, Q - выход.", align="center", font=("Arial", 12, "bold"))
    time.sleep(TIME_REFRESH)
    screen.update()



#mainloop - должен быть последним!
screen.mainloop()

