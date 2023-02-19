from base64 import decode
from click import password_option
import sql
from matplotlib.pyplot import connect
import mysql.connector 
mydb =mysql.connector.connect(host="localhost", user="Raaj",password="1234")


# mycursor=mydb.cursor()

# mycursor.execute("show databases")
url = sql_select_Query = "https://www.amfiindia.com/spages/NAVAll.txt"
mfDict = {}
for line in url:
    line = line.decode('utf-8')
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
# for db in mycursor:
#     print(db)