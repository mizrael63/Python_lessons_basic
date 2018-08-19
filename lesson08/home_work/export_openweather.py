
""" OpenWeatherMap (экспорт)

Сделать скрипт, экспортирующий данные из базы данных погоды, 
созданной скриптом openweather.py. Экспорт происходит в формате CSV или JSON.

Скрипт запускается из командной строки и получает на входе:
    export_openweather.py --csv filename [<город>]
    export_openweather.py --json filename [<город>]
    export_openweather.py --html filename [<город>]
    
При выгрузке в html можно по коду погоды (weather.id) подтянуть 
соответствующие картинки отсюда:  http://openweathermap.org/weather-conditions

Экспорт происходит в файл filename.

Опционально можно задать в командной строке город. В этом случае 
экспортируются только данные по указанному городу. Если города нет в базе -
выводится соответствующее сообщение.

"""
import json
import requests
import sqlite3
import sys
a = open("app.id")
my_app_id = a.read().splitlines()
api_url = "http://api.openweathermap.org/data/2.5/weather"
city = input("Введите название города на английском языке: ")
data_list = {"q": city, "appid": my_app_id, "units": "metric"}
a.close()
try: #Проверка существования города
    inquiry = requests.get(api_url, params=data_list) #Отправляем запрос
    data = inquiry.json() #сохраняем
    conclusion = "Температура в городе {} сейчас {} градус(ов)"
    print(conclusion.format(data["name"], data["main"]["temp"])) #Вытаскиваем градусы из данных
except:
    sys.exit("Такого города нет в базе!")
save_data = input("Хотите сохранить данные в SQLite? y/n: ")
if save_data == "y" or "Y":
    weather = [(data["id"], data["name"], data["dt"], data["main"]["temp"], data["weather"][0]["id"])] #Записываем необходимые данные
    connect = sqlite3.connect("cities.db")
    c = connect.cursor()
    c.execute(
        """CREATE TABLE IF NOT EXISTS {} (id_города INTEGER PRIMARY KEY, Город VARCHAR(255), Дата DATE, Температура INTEGER, id_погоды INTEGER)""".format(
            data["name"]))
    c.executemany("INSERT OR REPLACE INTO {} VALUES (?, ?, ?, ?, ?)".format(data["name"]), weather)  # Добавляем значения в БД
    connect.commit()
    c.close()
    connect.close()
    print("Город в базе данных cities.db создан!")
else:
    print("Хорошо, создавать БД не будем.")
