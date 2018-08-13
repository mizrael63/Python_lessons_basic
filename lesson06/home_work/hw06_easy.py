# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


import sys
import math
#создали класс
class triangulate:
#создали базовую конструкцию в которую передаем координаты всех точек
#В ней же считаем стороны
    def __init__(self, x1, y1, x2, y2, x3, y3):
#корректировки, изначально решал через инт, забыл про отрицательные числа
        self.x1 = float(x1)
        self.y1 = float(y1)
        self.x2 = float(x2)
        self.y2 = float(y2)
        self.x3 = float(x3)
        self.y3 = float(y3)
        self.a = math.sqrt((self.x2-self.x1)**2+(self.y2-self.y1)**2)
        self.b = math.sqrt((self.x3-self.x1)**2+(self.y3-self.y1)**2)
        self.c = math.sqrt((self.x3-self.x2)**2+(self.y3-self.y2)**2)
#Вычисляем периметр
        def perimetr(self):
            d = self.a+self.b+self.c
        return d
#Вычисляем площадь
    def area(self):
        area1 = self.x1*(self.y2-self.y3)
        area2 = self.x2*(self.y3-self.y1)
        area3 = self.x3*(self.y1-self.y2)
        area0 = math.fabs(area1 + area2 + area3) / 2.0
        return area0
 #формируем высоты   
    def heights(self):
        ah = 2*self.area() / self.a
        bh = 2*self.area() / self.b
        ch = 2*self.area() / self.c
        return [ah, bh, ch]


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

#Арсланов Михаил Васимович

class Trapeci:
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1 = float(x1)
        self.y1 = float(y1)
        self.x2 = float(x2)
        self.y2 = float(y2)
        self.x3 = float(x3)
        self.y3 = float(y3)
        self.x4 = float(x4)
        self.y4 = float(y4)
#длина сторон    
    def sides(self):
        a = math.sqrt(((self.x2-self.x1) ** 2) + ((self.y2-self.y1) ** 2))
        b = math.sqrt(((self.x3-self.x2) ** 2) + ((self.y3-self.y2) ** 2))
        c = math.sqrt(((self.x4-self.x3) ** 2) + ((self.y4-self.y3) ** 2))
        d = math.sqrt(((self.x4-self.x1) ** 2) + ((self.y4-self.y1) ** 2))
        return [a, b, c, d]
    #выполняем проверку равнобедренности трапеции - равенство боковых сторон
    def be_true(self):
         
        if trapeci.sides([0]) == trapeci.sides([2]):
            return 'Трапеция равнобедренная'
        else:
            return 'Трапеция не является равнобедренной'
    #считаем периметр
    def perim(self):
        summ = sum(trapeci.sides([]))
        return summ
   #вычисляем площадь
    def areass(self):
        a = Trapeci.sides([0])
        b = Trapeci.sides([1])
        c = Trapeci.sides([2])
        d = Trapeci.sides([3])
        S0 = ((b+d)/2)
        S1 = math.sqrt((a**2)-((((d-b)**2)+(a**2)-(c**2)/(2*(d-b)))))
        S = S0*S1
        return S

