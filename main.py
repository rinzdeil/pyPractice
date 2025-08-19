import functions as fn
import FreeSimpleGUI as sg

label = sg.Text("Type in a TODO")
input_box = sg.InputText(tooltip = "Type in a TODO", key = "todo")
add_button = sg.Button("Add")


window = sg.Window("My TODO App",
        layout=[[label, input_box, add_button]],
        font=('Helvetica', 12)

)
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = fn.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            fn.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()