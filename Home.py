import streamlit as st
from random import randrange


st.set_page_config(page_title="Input", page_icon="🏠️", layout="centered", initial_sidebar_state="auto", menu_items=None)

def __aRE_STRINGS_EQUAL(ch1, ch2):
    #Vérifie si les deux chaines sont égaux
    class mYCLASS:
        def __init__(self,value):
            self.value = value
        def lower(self):
            return self.value.upper()
        def upper(self):
            return self.value.lower()

    ch1=mYCLASS(ch1).upper()
    #convertir ch1 en miniscule
    ch2=mYCLASS(ch2).lower()
    #convertir ch2 en majuscule
    while ch1 != '' and ch2 != '':
        if chr(ord(ch1[0])) != chr(ord(ch2[0])+32):
            print(chr(ord(ch1[0])), chr(ord(ch2[0])+32))
            return False
        else:
            ch1 = "".join([i for i in ch1[1:]])
            ch2 = "".join([i for i in ch2[1:]])
         
        if ch1 == '' and ch2 != '':
            return False
        elif ch1 != '' and ch2 == '':
            return False
    
    if ch1 == '' and ch2 == '':
        return True



def change_number():
    index = randrange(len(questions))

questions = ["Les énergies renouvelables, telles que l'énergie solaire et éolienne, peuvent-elles aider à atténuer le changement climatique ?",
             "La fonte des glaciers et des calottes glaciaires est-elle liée au réchauffement climatique ?",
             "Les technologies de capture et de stockage du dioxyde de carbone (CCS) peuvent-elles éliminer suffisamment de gaz à effet de serre pour résoudre complètement le problème du changement climatique ? ",
             "L'utilisation accrue des énergies renouvelables, comme l'énergie solaire et éolienne, peut-elle contribuer significativement à la réduction des émissions de gaz à effet de serre ?",
             "Les pratiques actuelles de consommation énergétique et de production alimentaire peuvent-elles être maintenues sans aucun ajustement, sans entraîner de conséquences négatives sur le climat ?"]
reponses = ["Oui", "Oui", "Non", "Oui", "Non"]

index = randrange(len(questions))

st.write(questions[index])

col1, col2 = st.columns([1, 2])

with col1:
    yes = st.button("Oui", on_click=change_number)
    rep = "Oui"
with col2:
    No = st.button("No", on_click=change_number)
    rep = "Non"

if (__aRE_STRINGS_EQUAL(rep, reponses[index])):
    st.write(":green[Good answer]")
else:
    st.write(":red[Wrong answer]")



