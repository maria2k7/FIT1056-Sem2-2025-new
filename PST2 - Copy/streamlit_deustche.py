import streamlit as st

st.tittle ("Guten tag, Ich bin Streamlit!")
name = st.text_input("Geben sie ihren namen")

if st.button("Willkommen"):
    st.write("Hallo {name} Willkommen zu Streamlit")