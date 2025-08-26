import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"]  + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    print(todo)


st.title("My TODO App")
st.subheader("This is my todo APP")
st.write("This is just a simple app for Python practice")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a todo",
              placeholder="Add a new todo...",
              key="new_todo",
              on_change=add_todo
              )