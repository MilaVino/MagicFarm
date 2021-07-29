# Здесь список из кортежей - каждый элемент хранит координаты каких-то объектов.
import turtle
import time

screen = turtle.Screen()
screen.screensize(800, 555)
screen.bgpic('Background.png')
screen.colormode(255)

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
        #self.pencolor("brown")
        self.watered_degree = 0
        self.manure_degree = 0
        self.plant = None

    #метод для поливки лунки (один вызов метода +10%)
    def water(self):
        #Здесь надо сделать проверку на текущее значение <10 - иначе ничего не поливаем
        if self.watered_degree < 10 :
            self.watered_degree += 1
            self.color(0, 0, self.watered_degree * 25)
            self.pencolor("brown")

    #метод для высушивания лунки (один вызов метода -10%)
    def dehydrate(self):
        #Здесь надо сделать проверку на текущее значение <10 - иначе ничего не поливаем
        if self.watered_degree > 0 :
            self.watered_degree -= 1
            self.color(0, 0, self.watered_degree * 25)

    #метод для удобрения лунки (один вызов метода +1)
    def fertilize(self):
        """Метод увеличивает удобренность лунки"""
        #Здесь удобренность принимает значение +1
        if self.manure_degree < 3 :
            self.manure_degree += 1
            self.shapesize(outline = float(self.manure_degree * 2))

    #метод для удобрения лунки (один вызов метода +1)
    def defertilize(self):
        """Метод уменьшает удобренность лунки"""
        #Здесь удобренность принимает значение -1
        if self.manure_degree > 0 :
            self.manure_degree -= 1
            self.shapesize(outline = float(self.manure_degree * 2))

    def plant_plant(self, picked_plant):
        """Метод для посадки растения"""
        self.plant = picked_plant
        self.plant.setposition(self.position())

class Plant(turtle.Turtle):
    def __init__(self):
        super(Plant, self).__init__()
        self.penup()
        self.screen = screen
        self.hole: Hole
        self.ripeness = 0       #Спелость - от 0 до 5
        self.water_consume = 0  #Скорость поглощения воды
        self.manure_consume = 0 #Скорость поглощения удобрений
        self.edibility: bool    #Съедобность

class Carrot(Plant):
    def __init__(self):
        super(Carrot, self).__init__()
        self.screen.register_shape("carrot.gif")
        self.shape("carrot.gif")
        self.water_consume = 20
        self.manure_consume = 10
        self.edibility = True

#Todo: Индикация состояния спелости растения


#создаём лунки
hole_list_upper_left = []

for hole in hole_list_upper_left_coordinates:
    hole_list_upper_left.append(Hole(hole[0],hole[1]))

carrot1 = Carrot()
hole_list_upper_left[4].plant_plant(carrot1)

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


screen.mainloop()