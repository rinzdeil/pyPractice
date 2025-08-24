import FreeSimpleGUI as sg
from python_masterclass.compressor.compressor_fn import make_archive

filename = sg.Input("Enter filename .zip", key="filename")
input_label = sg.Text("Select files to compress")
input_filepath = sg.Input()
choose_input = sg.FilesBrowse("Choose", key="input")

output_label = sg.Text("Select files to compress")
output_filepath = sg.Input()
choose_output = sg.FolderBrowse("Choose", key="output")

compress_button = sg.Button("Compress")

window = sg.Window("File Compressor", layout=[
    [filename],
    [input_label, input_filepath, choose_input],
    [output_label, output_filepath, choose_output],
    [compress_button]
])

while True:
    event, values = window.read()
    print(event)
    print(values)
    filepaths = values["input"].split(";")
    dest_folder = values["output"]
    filename = values["filename"]


    if event == "Compress":
        make_archive(filepaths, dest_folder, filename)

window.close()