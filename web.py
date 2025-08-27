import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]  + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    print(todo)

# def complete_todo():
#     for todo in todos:
#         todo_state = st.session_state[todo]
#         if todo_state == "true":
#             todos.remove(todo)

#             functions.write_todos(todos)


st.title("My TODO App")
st.subheader("This is my todo APP")
st.write("This is just a simple app for Python practice")

for index, item in enumerate(todos):
    checkbox = st.checkbox(item, key=item)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[item]
        st.rerun()

st.text_input(label="Enter a todo",
              placeholder="Add a new todo...",
              key="new_todo",
              on_change=add_todo
              )

st.session_state