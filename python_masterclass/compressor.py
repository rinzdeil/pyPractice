import FreeSimpleGUI as sg

input_label = sg.Text("Select files to compress")
input_filepath = sg.Input()
choose_input = sg.FilesBrowse("Choose")

output_label = sg.Text("Select files to compress")
output_filepath = sg.Input()
choose_output = sg.FilesBrowse("Choose")

compress_button = sg.Button("Compress")

window = sg.Window("File Compressor", layout=[
    [input_label, input_filepath, choose_input],
    [output_label, output_filepath, choose_output],
    [compress_button]
])

window.read()
window.close()