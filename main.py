import functions as fn
import FreeSimpleGUI as sg
import time

sg.theme('LightBlue')
clock = sg.Text("", key="clock")
label = sg.Text("Type in a TODO")
input_box = sg.InputText(tooltip = "Type in a TODO", key = "input_todo")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")


list_box = sg.Listbox(values=fn.get_todos(),
                      key="lb_todos",
                      enable_events=True,
                      size=(45,10))

def update_list():
    window["lb_todos"].update(values=todos)

def clear_input():
    window["input_todo"].update(value="")

# Layout of elements in GUI
layout = [[clock],
          [label, input_box, add_button],
          [list_box, edit_button, complete_button],
          [exit_button]
]

window = sg.Window("My TODO App",
        layout=layout,
        font=('Helvetica', 12)

)
while True:
    event, values = window.read(timeout=1000)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M"))

    print(event)
    print(values)
    print(values["lb_todos"])



    match event:
        case "Add":
            if values["input_todo"] != '':
                todos = fn.get_todos()
                new_todo = values["input_todo"] + "\n"
                todos.append(new_todo)
                fn.write_todos(todos)
                update_list()
                clear_input()
            else:
                continue

        case "Edit":
            try:
                selected_todo = values["lb_todos"][0]
                new_todo = values["input_todo"] + "\n"

                todos = fn.get_todos()

                index = todos.index(selected_todo)
                todos[index] = new_todo
                fn.write_todos(todos)
                update_list()
                clear_input()
            except IndexError as e:
                sg.popup("Select a TODO first")

        case "Complete":
            try:
                todos = fn.get_todos()
                selected_todo = values["lb_todos"][0]
                todos.remove(selected_todo)
                fn.write_todos(todos)

                update_list()
                clear_input()
                selected_todo = selected_todo.strip("\n")
                sg.popup(f"{selected_todo} complete")
            except IndexError as e:
                sg.popup("Select a TODO first")

        case "lb_todos":
            selected_todo = values["lb_todos"][0].strip("\n")
            window["input_todo"].update(value=selected_todo)

        case "Exit":
            break

        case sg.WIN_CLOSED:
            break

window.close()