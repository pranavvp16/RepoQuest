import streamlit as st


st.title("Web URL Input ")


url = st.text_input("Enter a web URL")

if st.button("Open URL"):
    st.write(f"You entered the URL: [{url}]({url})")