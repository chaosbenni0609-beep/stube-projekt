from numpy import *
from sqlite3 import *
import streamlit as st
from sqlalchemy import *
list = []
User_in = []

con = st.connection('mysql', type='sql')

# Perform query.
result= con.query('SELECT * from mytable;', ttl=600)



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

