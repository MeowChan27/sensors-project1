#https://www.youtube.com/watch?v=2R-BveCE-so&ab_channel=FormationVid%C3%A9o - Tutoriel Python - base de données MySQL

time = "10h00" # à Changer ! 
temp = 10 # à Changer ! 
humi = 0.4 # à Changer ! 
humi_2 = str(int(100*humi)) + "%"
pres = 1.6 # à Changer ! 

import mysql.connector as MC

try:
    conn = MC.connect(host = 'localhost',database = 'datatest', user = 'root', password = 'Ichan2012!')
    cursor = conn.cursor()

    req = 'INSERT INTO atmosphere(time,temperature, humidite, pression) VALUES(%s,%s,%s,%s)'
    infos = (time,temp,humi_2,pres) # On utilise un joker
    cursor.execute(req,infos) # Enlever le 2e arg si pour visualiser
    conn.commit() # Enlever pour visualiser

""""
Permet l'affichage de la table atmosphere

    req = 'SELECT * FROM atmosphere'
    cursor.execute(req)
    my_list = cursor.fetchall()
    print(my_list)

"""
except MC.Error as err :
    print(err)
finally:
    if(conn.is_connected()):
        cursor.close()
        conn.close()