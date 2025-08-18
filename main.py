import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a TODO")
input_box = sg.InputText(tooltip = "Type in a TODO")
add_button = sg.Button("Add")


window = sg.Window("My TODO App", layout=[[label], [input_box, add_button]])
window.read()
window.close()



