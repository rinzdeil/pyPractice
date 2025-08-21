import functions as fn
import FreeSimpleGUI as sg

label = sg.Text("Type in a TODO")
input_box = sg.InputText(tooltip = "Type in a TODO", key = "input_todo")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")

list_box = sg.Listbox(values=fn.get_todos(),
                      key="lb_todos",
                      enable_events=True,
                      size=(45,10))


def update_list():
    window["lb_todos"].update(values=todos)

layout = [[label, input_box, add_button],
          [list_box, edit_button]
]

window = sg.Window("My TODO App",
        layout=layout,
        font=('Helvetica', 12)

)
while True:
    event, values = window.read()
    print(event)
    print(values)
    print(values["lb_todos"])
    match event:
        case "Add":
            todos = fn.get_todos()
            new_todo = values["input_todo"] + "\n"
            todos.append(new_todo)
            fn.write_todos(todos)
            update_list()

        case "Edit":
            edited_todo = values["lb_todos"][0]
            new_todo = values["input_todo"] + "\n"

            todos = fn.get_todos()
            index = todos.index(edited_todo)
            todos[index] = new_todo
            fn.write_todos(todos)
            update_list()

        case "lb_todos":
            window["input_todo"].update(value=values["lb_todos"][0])

        case sg.WIN_CLOSED:
            exit()

window.close()