import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import sklearn
from sklearn.datasets import load_iris
from PIL import Image
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
def app():
    ## EN TETE DE PAGE
    st.title('My First Streamlit App')
    st.markdown('Made by [@Tavares Dylan](https://www.linkedin.com/in/dylan-tavar%C3%A8s-727b23187/)')
    image = Image.open("flower.jpg")
    st.image(image)
    st.header('Iris Dataset Analysis')
    st.markdown('Streamlit is **_really_ cool** 😎.')
    st.text('Le dataset Iris est très connu des amateurs de machine learning , c\'est un jeu de données\nd\'entrainement pour de la classification. Voici le jeu de données en question \nci-dessous ⬇️.')

    ## DATAVIZ
    # Chargement des données Iris
    data = load_iris()
    # Création des dataframe pandas 
    df_data = pd.DataFrame(data=data.data,columns=data.feature_names)
    df_target = pd.DataFrame(data=data.target, columns=["species"])
    # Affichage des données X
    st.dataframe(df_data)
    st.text('Le jeu de données comporte des informations concernant la longueur et largeur des pétales\n, et la longueur et largeur des sépales.')
    st.dataframe(df_data.describe())
    st.text('Voici la description du dataset , on peu observer différentes statistiques \nsur l\'ensemble du jeu de données.Par exemple la moyenne , ou encore les \nvaleurs minimum et maximum.')
    # Affichage des données y
    st.dataframe(df_target)
    st.dataframe(df_target.describe())

    # MENU SIDEBAR
    st.sidebar.title("Selectionez vos paramètres")
    pl_btn = st.sidebar.number_input(
        'Longueur de pétale',)
    pw_btn = st.sidebar.number_input(
        'Largeur de pétale',)
    sl_btn = st.sidebar.number_input(
        'Longueur de sépale',)
    sw_btn = st.sidebar.number_input(
        'largeur de sépale',)
    sub_btn = st.sidebar.button(
        'Soumettre',)

    st.bar_chart(data.data)

    # Définition du X et du y
    X = df_data
    y = df_target

    # Split des données
    X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=42, test_size=0.25)

    lr = LogisticRegression()
    lr.fit(X_train,y_train)
    test_score = lr.score(X_test,y_test)
    st.write(test_score)


    # TEST DU BOUTTON
    if sub_btn:
        st.write(pl_btn,pw_btn,sl_btn,sw_btn)
        pred = lr.predict([[pl_btn,pw_btn,sl_btn,sw_btn]])
        st.sidebar.header("Votre résultat est "+str(data.target_names[pred]))
        st.sidebar.write()