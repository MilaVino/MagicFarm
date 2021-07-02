# Здесь список из кортежей - каждый элемент хранит координаты каких-то объектов.
import turtle
import time

hole_list_upper_left_coordinates = [(-281.0, 92.0), (-254.0, 200.0), (-191.0, 211.0), (-219.0, 169.0), (-259.0, 133.0), (-222.0, 113.0),
                                    (-255.0, 56.0)]

hole_list_bottom_left = [(-33.0, 305.0),
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

hole_list_right = [(-5.0, 54.0), (67.0, 89.0), (116.0, 90.0)]

# hole_list_right2 = [(-12.0, 129.0)
# (35.0, 191.0)
# (-6.0, 53.0)
# (67.0, 89.0)
# (117.0, 88.0)
# (28.0, 15.0)
# (122.0, 35.0)
# (97.0, -25.0)
# (46.0, -67.0)]

#Лунка имеет следующие характеристики:
# - Политость (цвет)
# - Удобренность (размер)
# - Степень атакованности сорняками (объекты сорняки недалеко от лунки)

class Hole(turtle.Turtle):
    def __init__(self, x, y):
        super(Hole, self).__init__()
        self.penup()
        self.setposition(x, y)
        self.shape("circle")
        self.color("black")
        self.watered_degree = 0

#метод для поливки лунки (один вызов метода +10%)
    def water(self):
        #Здесь надо сделать проверку на текущее значение <10 - иначе ничего не поливаем
        self.watered_degree += 1
        self.color(0, 0, self.watered_degree * 25)

#создаём лунки
hole_list_upper_left = []

for hole in hole_list_upper_left_coordinates:
    hole_list_upper_left.append(Hole(hole[0],hole[1]))

for i in range(0,15):
    for hole in hole_list_upper_left:
        hole.water()
        time.sleep(0.05)
