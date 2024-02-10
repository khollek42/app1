import streamlit as st
import files.functions as funct

todos = funct.get_todos("files\\todos.txt")

def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    funct.write_todos(todos, filepath='files\\todos.txt')



st.title("To-do's")

st.subheader("For the love of my life!")
st.write("Do IT!!!")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        funct.write_todos(todos, filepath='files\\todos.txt')
        del st.session_state[todo]
        st.rerun()


st.text_input(label="Add new Todo:", placeholder="Add new Todo",
              on_change=add_todo,
              key="new_todo")

#st.session_state