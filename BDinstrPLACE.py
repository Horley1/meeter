import psycopg2
dbconfig = {
    'host':'localhost',
    'user':'postgres',
    'password': '1188',
    'port':'5432',
    'database':'Metro'
    }

connection = psycopg2.connect(**dbconfig)
cur = connection.cursor() #необходимый синтаксис, именно он занимает большую часть времени
print('connect')#просто так
ID=1
name="kon"
lan=124.23244
lon=243.44444
address="yuyskaya street, 15"
typeof=0
a="insert into places (idplace, nameplace, lat, lon, address , TypeOfPlace) values ("+str(ID)+", '"+name+"', "+str(lan)+","+str(lon)+",'"+address+"',"+str(typeof)+" )" #команда SQL на для загрузки дынных
cur.execute(a)#сама команда, где аргумент стринг
connection.commit()#сохранение данных
tab="places"
a="select * from places"
cur.execute(a)#команда выбора элеметов из таблицы
print(cur.fetchall())#печать результата 