from numpy import *
import streamlit as st
from random import * 
User_in = []
list = [["Maler", 1, 1, 2, 3, 1, 5, 2, 3, 2, 2, 5, 4, 2, 1, 5, 4, 2, 5, 1, 2, 1, 2, 4, 1, 1, 1, 2, 1, 5, 5, 2],
        ["Kindergärtnerin ",1,1,5,5,2,5,3,4,2,1,2,4,4,3,2,3,2,5,2,4,2,3,4,2,1,2,3,3,4,4,2],
        ["Innenarchitekt ",1,1,2,4,2,5,3,3,4,3,4,2,4,1,3,2,5,5,1,3,2,2,4,3,1,3,3,2,5,5,4],
        ["Assistenz im Labor ",5,1,2,2,3,5,3,5,5,5,5,1,4,4,3,2,3,2,3,5,5,5,4,1,4,2,3,5,4,2,2],
        ["Tierarzt ",3,1,2,4,5,3,3,5,3,3,3,4,4,2,3,1,3,4,5,4,4,2,3,1,4,1,1,1,4,3,2],
        ["Kaufmännischer Fachwirt",1,4,3,4,4,2,2,4,4,4,3,4,4,3,3,3,4,2,3,3,3,2,3,1,1,2,3,2,2,1,3],
        ["Handelsfachwirt/Einzelhandelskauffrau",1,1,4,4,1,5,3,4,3,4,3,4,5,2,5,5,2,5,2,5,2,4,3,3,2,2,4,3,4,3,4],
        ["Lehrerin",2,5,4,3,2,5,4,5,2,4,4,3,4,5,4,3,2,5,3,4,5,4,4,5,5,5,5,5,4,5,5],
        ["Betriebswitschaftslehre",3,3,1,3,1,1,2,1,3,4,2,3,4,4,2,2,3,4,2,4,3,4,3,2,4,3,3,2,2,5,3],
        ["Dachdecker",1,1,5,3,1,3,2,3,2,2,1,4,3,1,5,5,1,4,2,4,1,2,4,3,4,3,2,3,2,3,1],
        ["Sachbearbeiterin ",2,4,5,4,3,4,3,5,4,2,2,5,3,2,2,1,1,1,5,4,2,1,4,5,1,1,4,1,4,4,2],
        ["Technische Systemplanerin für Versorgungs- und Ausrüstungstechnik",1,2,1,2,5,5,2,3,3,2,5,4,3,3,3,3,1,2,4,4,2,3,4,4,3,2,2,1,2,2,2],
        ["Versicherungskaufmann ", 1, 2, 1, 4, 5, 4, 4, 5, 2, 4, 5, 5, 4, 4, 4, 1, 5, 4, 2, 4, 2, 4, 5, 2, 2, 5, 4, 2, 4, 1, 1]
        ]

list_without_first = [i[1:] for i in list]

User_in.append(st.slider("Wie gerne arbeite ich in einem Labor?",1,5,3))
User_in.append(st.slider("Wie gerne arbeite ich in einem Museum?",1,5,3))
User_in.append(st.slider("Ich arbeite gerne mit Kindern",1,5,3))
User_in.append(st.slider("Ich arbeite gerne mit Menschen",1,5,3))
User_in.append(st.slider("Ich arbeite gerne mit Tieren",1,5,3))
User_in.append(st.slider("Ich mag es kreativ zu sein",1,5,3))
User_in.append(st.slider("Ich spreche gerne andere Sprachen",1,5,3))
User_in.append(st.slider("Ich mag es lange in der Natur zu sein",1,5,3))
User_in.append(st.slider("Ich arbeite gerne mit Computern",1,5,3))
User_in.append(st.slider("Ich mag es mit Zahlen zu arbeiten",1,5,3))
User_in.append(st.slider("Ich arbeite gerne allein",1,5,3))
User_in.append(st.slider("Ich mag Routine",1,5,3))
User_in.append(st.slider("Ich löse gerne Probleme",1,5,3))
User_in.append(st.slider("Ich verfasse gerne Texte",1,5,3))
User_in.append(st.slider("Ich mag es mit meinen Händen zu arbeiten",1,5,3))
User_in.append(st.slider("Ich mag es mich körperlich zu betätigen",1,5,3))
User_in.append(st.slider("Ich mag es vor Leuten zu sprechen",1,5,3))
User_in.append(st.slider("Ich mag es Verantwortung zu übernehmen",1,5,3))
User_in.append(st.slider("Mir ist es wichtig Menschen oder Tieren zu helfen (biologisch)",1,5,3))
User_in.append(st.slider("Ich mag es neue Themen zu erfahren",1,5,3))
User_in.append(st.slider("Ich arbeite gerne Experimente durchzuführen",1,5,3))
User_in.append(st.slider("Ich setze mich gerne mit theoretischen Fragen auseinander",1,5,3))
User_in.append(st.slider("Ich setze gerne meine eigenen Ideen um",1,5,3))
User_in.append(st.slider("Ich beschäftige mich gerne mit Kunst, Musik oder Literatur",1,5,3))
User_in.append(st.slider("Ich lese gerne wissenschaftliche Texte",1,5,3))
User_in.append(st.slider("Ich diskutiere gerne",1,5,3))
User_in.append(st.slider("Ich setze mich gerne mit anderen Kulturen auseinander",1,5,3))
User_in.append(st.slider("Ich beschäftige mich gerne mit Geschichte",1,5,3))
User_in.append(st.slider("Ich koordiniere oder sortiere gerne",1,5,3))
User_in.append(st.slider("Ich arbeite gerne von verschiedenen Orten",1,5,3))
User_in.append(st.slider("Ich gehe/würde gerne oft auf Arbeitsreisen gehen",1,5,3))


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

#noch anpassen 
t = 0 
best_erg = 0 
best_index = 0 
for n in list:
    erg = vergleich(User_in, list_without_first[t])
    if erg > best_erg :
        best_erg = erg
        best_index = t
    t += 1
best_erg = list[best_index]
st.write(best_erg[0])
st.write(list[best_index])

