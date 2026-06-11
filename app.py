import streamlit as st

st.title("Mage Palameni Web App eka! 🚀")
st.write("Hello! Google Colab saha GitHub use karala hadapu web app ekak.")

# Simple input box ekak
name = st.text_input("Oyage nama liyanna:")
if name:
    st.write(f"Ayubowan, {name}!")
