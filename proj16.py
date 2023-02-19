# from colorama import Cursor
# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="Raaj",
#   password="1234",
#   database="nav"
# )

# mycursor = mydb.cursor()

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]

# mycursor.executemany(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "was inserted.")# mycursor.execute("show tables")

# for x in mycursor:
#     print(x)


import mysql.connector
import json

# import MySQLdb as db
# con = db.connect(user="root", passwd="1234")
# cur = con.cursor()
# cur.execute('CREATE DATABASE somedb;')

cnx = mysql.connector.connect(
    database='nav', user='root', password='1234', host='localhost'
)

cnx1 = mysql.connector.connect(
    database='nav', user='root', password='1234', host='localhost'
)

cursor = cnx.cursor();
cursor1 = cnx1.cursor();

# query = "SELECT a.recipe_id, a.recipe_item_type, b.meta_key, b.meta_value, b.recipe_item_id FROM wp_simmer_recipe_items a, wp_simmer_recipe_itemmeta b WHERE a.recipe_item_id = b.recipe_item_id GROUP BY a.recipe_item_id"
# query1 = "SELECT * FROM wp_simmer_recipe_itemmeta WHERE recipe_item_id=(%s)"

cursor.execute(query)
rs = cursor.fetchall()

data = {}
url = sql_select_Query = "https://www.amfiindia.com/spages/NAVAll.txt"
mfDict = {}
for line in rs:
    if ';' in line:
        row = line.split(';')
        try:
            code = int(row[0])
            mf = {}
            mf['code'] = code
            mf['name'] = row[3]
            mf['nav']  = row[4]
            mf['date'] = row[5].replace('\r\n','')
            mfDict[code] = mf
        except:
            pass
    import json
    with open('nav.json','w') as fp:
        json.dump([mfDict],fp)

cursor1.close()
cnx1.close()
cursor.close()
cnx.close()
