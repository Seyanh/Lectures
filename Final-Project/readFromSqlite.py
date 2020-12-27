# This code is just the basic idea!

import sqlite3

db = sqlite3.connect("DogvsCattest.sqlite")
cur = db.cursor()  # 获取数据库db的一系列操作cur

res = cur.execute("select * from cat")

for picture in res.fetchall():
	file = open("test.jpg", "wb")
	file.write(picture[0])
	file.close()
