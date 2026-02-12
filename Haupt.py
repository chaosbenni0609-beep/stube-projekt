from numpy import *
from sqlite3 import *
import streamlit as st
import mysql.connector
list = []
User_in = []

try:
    con = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "user",
        database = "datab"
    )

    if con.is_connected():
        print("connected to base")
    else :
        print("not connected ")
    curs = con.cursor()
    con.commit
except:
    print("connection issue")



curs.execute('SELECT * FROM tab')
result = curs.fetchall()
for i in result : 
    list.append(i)
print(result)
print(list)




def vergleich(a,b):
    a = array(a,dtype=float)
    b = array(b,dtype=float)
    test = dot(a,b)
    # Step 2: Compute the magnitudes of the vectors
    magnitude_A = linalg.norm(a)
    magnitude_B = linalg.norm(b)
    # Step 3: Calculate cosine similaritycosine_similarity = test2 / (magnitude_A * magnitude_C)
    cos_similarity = test / (magnitude_A * magnitude_B)
    return cos_similarity

for i in list[0]:
    x = input()
    User_in.append(x)
t = 0 
for n in list:
    erg_list = list[t]
    erg = vergleich(User_in, erg_list)
    print(erg)
    t =+ 1

