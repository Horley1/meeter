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
EdgTime=6#время ребра
ID1=5#первая станция
ID2=7#вторая станция
a="insert into edges (id1, id2, edgtime ) values ("+str(ID1)+ ","+str(ID2)+ ","+str(EdgTime)+" )" #команда SQL на для загрузки дынных
cur.execute(a)#сама команда, где аргумент стринг
connection.commit()#сохранение данных
roll="EdgTime"#первый столбец\откуда берем
tab="Edges"#таблица, откуда берем
roll1="ID1"#столбил\условие 1
num1=1#значение столбика\условие 1
roll2="ID2"#столбик\условие 2
num2=2#значение стголбика\условие 2
a="select "+roll+" from "+tab+" where "+roll1+"="+str(num1)+" and "+roll2+"="+str(num2)#команда
cur.execute(a)#команда выбора элеметов из таблицы
print(cur.fetchall())#печать результата 