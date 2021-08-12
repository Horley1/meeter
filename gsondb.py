import json
import psycopg2
dbconfig = {
    'host':'ec2-52-23-45-36.compute-1.amazonaws.com',
    'user':'oxtoyzhnayeeoj',
    'password': '1fcb70fbb4cd9d12a3b4c385a8e031e52d329f777cf6ba4bed6610b5844fc6a7',
    'port':'5432',
    'database':'d6k99pdrf80vm8'
    }

json = json.load(open('D:\cafes.json', 'r'))
print(json[0]['title'])
connection = psycopg2.connect(**dbconfig)
cur = connection.cursor() 
print('connect')
a="insert into places (placeid, placename, placetype, lan, lon, address) values (1, 'Force', 'Coffee', 13.3434, 55.33434, 'Yuyskaya street, 16' )" 
cur.execute(a)
connection.commit()
a="select * from places"
cur.execute(a)
print(cur.fetchall())
