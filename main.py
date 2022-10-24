import streamlit as st

st.title('Hello streamlit.')
counter = 0

increment = st.button('Increment')
if increment:
    counter += 1

st.write('Count= ', counter)
st.text("lsm")
