## IMPORT DES LIBRAIRIES

import streamlit as st
import app1
import app2

PAGES = {
    "Iris": app1,
    "App2": app2
}
selection = st.sidebar.radio("MENU", list(PAGES.keys()))
page = PAGES[selection]
page.app()

