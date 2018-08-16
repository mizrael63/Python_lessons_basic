#!/usr/bin/python3

"""Арсланов Михаил Васимович"""
"""== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки: """

import random
#тут мы создаем наш мешок с бочонками

mylist = []
n=1
m=0
while n<91:
    mylist.append(n)
    n+=1

#bsum = sum([i for i in mylist]) #здесь единожды считали сумму всех чисел от 1 до 90 - она неизменна и является
#print(bsum) константой - 4095. Число пригодится далее
mylist2 = [] #создвем пустой массив 2, который будем использовать для нашего псевдорандома
def varr(mylist): #тут мы используя список значений генерируем числа бочонка
    a = random.choice (mylist) #значение бочонка которое достается из мешка
    mylist.remove(a) #раз достали, удаляем из "мешка"
    mylist2.append(a) #и добавляем к тем, которые уже у нас на руках
#print(mylist)
while sum([i for i in mylist2])!=4095: #здесь собственно благорадя нашей функции создаем заранее предопределенный
    #список ходов на основании нашего псевдорандома. Пользователь видеть этого не будет, но все ходы уже
    #предопределены. В этом случае мы получили статичный массив к которому можем обращаться для отработки других
    #наших модулей
    varr(mylist)
#print(mylist2)

#здесь генерируем карту. Карта это таблица на 27 значений, из которых 15 - int, а остальные '_'

class numberosa: #сюда передаем имя и диапазон через ,
    def __init__(self, name, n, m):
        self.name = name
        self.n = n
        self.m = m

    def whille(self):
        while len(self.name)<3:
            a = random.randint(self.n, self.m)
            self.name.append(a)
        return sorted(self.name)

class prof: #сюда передаем тоже самое имя, функция для того чтобы убрать одинаковые значения
    def __init__(self, name, n, m):
        self.name = name
        self.n = n
        self.m = m
    def metoda(self):
        a = self.name[0]
        #print(a)
        b = self.name[1]
        #print(b)
        c = self.name[2]
        #print(c)
        #print("Полученные в функцию значения", self.name, self.n, self.m)
        while a == b or b==c or a == c:
            if a == self.n:
                if a == b:
                    b = b+random.randint(1,5)
                    if b >= c:
                        c = c+random.randint(1,3)
            if a == self.m:
                a = c-random.randint(1,7)
                b = a+random.randint(1,2)
                c = random.randint(b, self.m)
            if a == b:
                b = a+1
                if b >= c:
                    while b>=c:
                        b-=1
            if b == self.m:
                b = a+2
            if b == c:
                b = c-1
                c = c+1
                if c > self.m:
                    while c > self.m or c == b:
                        c = random.randint(b,self.m)

            return a,b,c
        del self.name[2]
        del self.name[1]
        del self.name[0]
        self.name.append(a)
        self.name.append(b)
        self.name.append(c)
        sorted(self.name)
        return [a,b,c]
one = []
one = numberosa(one, 1, 9)
one = one.whille()
one = prof(one, 1, 9)
one = list(one.metoda())

two = []
two = numberosa(two, 10, 19)
two = two.whille()
two = prof(two, 10, 19)
two = list(two.metoda())

three = []
three = numberosa(three, 20,29)
three = three.whille()
three = prof(three, 20,29)
three = list(three.metoda())

four = []
four = numberosa(four, 30, 39)
four = four.whille()
four = prof(four, 30, 39)
four = list(four.metoda())

five = []
five = numberosa(five, 40,49)
five = five.whille()
five = prof(five,40,49)
five = list(five.metoda())

six = []
six = numberosa(six, 50,59)
six = six.whille()
six = prof(six,50,59)
six = list(six.metoda())

seven = []
seven = numberosa(seven, 60,69)
seven = seven.whille()
seven = prof(seven,60,69)
seven = list(seven.metoda())

eight = []
eight = numberosa(eight,70,79)
eight = eight.whille()
eight = prof(eight,70,79)
eight = list(eight.metoda())

nine = []
nine = numberosa(nine, 80,90)
nine = nine.whille()
nine = prof(nine,80,90)
nine = list(nine.metoda())

aa = [one, two, three, four, five, six, seven, eight, nine]
print(aa)
print(one)
import numpy as np

aaa = np.array([random.random() for i in range(12)])


class avoid:
    def __init__(self, name, name2, name3, name4):
        self.name = name
        self.name2 = name2
        self.name3 = name3
            
    def abgf(self):
        self.name = random.randint(1,2)
        self.name2 = random.randint(3,4)
        self.name3 = random.randint(5,7)
        self.name4 = random.randint(8,9)
        if self.name == self.name2:
            while self.name == self.name2:
                self.name2 = random.randint(1,9)
            if self.name == self.name3 or self.name2 == self.name:
                while self.name == self.name2 == self.name3:
                    self.name3 = random.randint(1,9)
            if self.name4 == self.name or self.name4 == self.name2 or self.name3 == self.name4:
                while self.name4 == self.name or self.name4 == self.name2 or self.name4 == self.name3:
                    self.name4 = random.randint(1,9)
        if self.name == self.name4:
            self.name4 +=1
            
        return self.name, self.name2, self.name3, self.name4
a11 = avoid(aaa[0], aaa[1], aaa[2],aaa[3])
a11 = list(a11.abgf())
a22 = avoid(aaa[4], aaa[5], aaa [6], aaa[7])
a22 = list(a22.abgf())
a33 = avoid(aaa[8], aaa[9], aaa[10], aaa[11])
a33 = list(a33.abgf())
a11[:] = [x-1 for x in a11]
a22[:] = [x-1 for x in a22]
a33[:] = [x-1 for x in a33]

for t in zip(one, two, three, four, five, six, seven, eight, nine):
    print(t[0], t[1], t[2], t[3], t[4], t[5], t[6], t[7], t[8])

bb = [a11, a22, a33]
print(bb)
aa[(bb[0][0])][0] = '_'
aa[(bb[0][1])][0] = '_'
aa[(bb[0][2])][0] = '_'
aa[(bb[0][3])][0] = '_'
aa[(bb[1][0])][1] = '_'
aa[(bb[1][1])][1] = '_'
aa[(bb[1][2])][1] = '_'
aa[(bb[1][3])][1] = '_'
aa[(bb[2][0])][2] = '_'
aa[(bb[2][1])][2] = '_'
aa[(bb[2][2])][2] = '_'
aa[(bb[2][3])][2] = '_'
for t in zip(one, two, three, four, five, six, seven, eight, nine):
    print(t[0], t[1], t[2], t[3], t[4], t[5], t[6], t[7], t[8])
print(aa)

zbg =(np.array([random.random() for i in range(15)])) #билет компьютера
i = 0
while i <15:
    zbg[i]=int(random.randint(1,90))
    i+=1
    while zbg[i-1] == zbg[i-2]:
        zbg[i] = random.randint(1,90)
    
zbg = sorted(zbg)
zbg = [int(item) for item in zbg]
strr1=zbg[0:3]
strr2=zbg[3:6]
strr3=zbg[6:9]
strr4=zbg[9:12]
strr5=zbg[12:15]
for t in zip(strr1, strr2, strr3,strr4,strr5):
    print(t[0], t[1], t[2], t[3], t[4])

def module():
    zzzz=int(input("Начнем игру? 1 - да, 2 - нет "))
    bsum2 = sum([i for i in mylist2])
    print("Осталось ещё ", bsum2, " очков в мешочке")
    bsum3 = sum([i for i in aa])
    if bsum3 ==0:
	print("Поздравляю вас с победой!")
	print("Если хотите попробовать ещё, нажмите 1")
	ase = int(input("Ввод:  ")
	if ase == 1:
		module1()	  
    if zzzz==1:
        print("Хороший выбор")
        module1()
    elif zzzz==2:
	print("Всего доброго")
	pass
    else: 
        print("Введены неизвестные символы, повторите ввод")
        module()
def module1():
    print("Вас приветствует игра лото, в которой побеждает тот, кто первый закроет все цифры своего билета")
    print("Вам предлагается два варианта: 1. Закрыть число. 2. Пропустить")
    print("Если вы пропустите, когда число есть на вашей карточке или попытаетесь закрыть число, когда его у вас нет")
    print("Вы проиграете!")
    print("Это билет компьютера. Если на нем закончатся числа раньше чем у вас, то вы проиграете")
    for t in zip(strr1, strr2, strr3,strr4,strr5):
        print(t[0], t[1], t[2], t[3], t[4])
    print("-----------------------------")
    print("Это ваш билет")
    for t in zip(one, two, three, four, five, six, seven, eight, nine):
        print(t[0], t[1], t[2], t[3], t[4], t[5], t[6], t[7], t[8])
    print("Мы достали бочонок", mylist2[0])
    wqr = mylist2[0]
    del mylist2[0]
    print("У вас есть этот бочонок, если да, то нажмите 1. Если нет, то нажмите 2  ")
    qqq=input("Ввод:  ")
    print(wqr)
    if qqq == 1:
        i = 0
        n = 0#перебирать значения и сравнивать с полученным числом
        while wqr!=aa[i][n]: #i от 0 до 8, n от 0 до 3 просто уже не могу сообразить как счет правильно реализовать
            i = i for i in xrange(0, 8)
            n = n for n in xrange(0, 2)
            #не знаю как перебор реализовать корректно
            return aa[i][n]
        aa[i][n] =  "_"
	module1()
        else: 
		print("Конец игры")
		print("Если хотите попробовать ещё раз нажмите 1")
		zzzz=int(input("Ввод" ))
		if zzzz==1:
			module1()
		else: pass
        print("Хороший выбор")
        module1()
	while wqr!=zbg[i][n]:
            i = i for i in xrange(0, 8)
            n = n for n in xrange(0, 2)
            
            return zbg[i][n]
        aa[i][n] =  "_"
        else: pass	
    
              
#module() #не отрабатывал условие
module1()
