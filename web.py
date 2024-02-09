import streamlit as st
import files.functions as funct

todos = funct.get_todos("files\\todos.txt")

st.title("Todo app")

st.subheader(" this is my header")
st.write("this is a new app")

for todo in todos:
    st.checkbox(todo)


st.text_input(label="", placeholder="Add new Todo")

