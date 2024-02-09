import streamlit as st
import files.functions as funct

todos = funct.get_todos("files\\todos.txt")

def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    funct.write_todos(todos, filepath='files\\todos.txt')



st.title("Todo app")

st.subheader(" this is my header")
st.write("this is a new app")

for todo in todos:
    st.checkbox(todo)


st.text_input(label="Add new Todo:", placeholder="Add new Todo",
              on_change=add_todo,
              key="new_todo")

