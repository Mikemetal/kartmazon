import urllib2
import MySQLdb
import urllib
import json


db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                      passwd="w4p1ll0", # your password
                      db="kartmazon")

cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM marca_marca")
texto = ""
# print all the first cell of all the rows
for row in cur.fetchall() :
    print str(row[0]) + " - " + row[1]
    marca = { 'make' : row[1] }
    parametro = urllib.urlencode(marca)
    url = "http://www.cardomain.com/handlers/MakeModelTrim.ashx?action=models&"+parametro

    modelos = urllib2.urlopen(url).read()
    decoded_data = json.loads(modelos)
    totalModelos = len(decoded_data["models"]) - 1
    for num in range(0,totalModelos):
        query = "insert into modelo_modelo (marca_id,nombre) values('%s','%s');" % (row[0],decoded_data["models"][num]['Model_name'])
        query.replace("'","")
        texto = texto + query
        # cur.execute(query)
        print query


text_file = open("Output.txt", "w")
text_file.write(texto)
text_file.close()