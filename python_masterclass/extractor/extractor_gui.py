import FreeSimpleGUI as sg

sg.theme('Black')

select_files = sg.Text("Select files to Archive")
output_dir = sg.Text("Select output folder")
extract_label = sg.Text(key="success", text_color="green")

input_path = sg.Input(size=20)
dir_path = sg.Input(size=20)

select_btn = sg.FileBrowse("Choose", key = "archive")
output_btn = sg.FolderBrowse("Choose", key = "folder")
extract_btn = sg.Button("Extract")


layout = [
    [select_files, input_path, select_btn],
    [output_dir, dir_path, output_btn],
    [extract_btn],
    [extract_label]
]

window = sg.Window(
    "Archive Extractor",
    layout = layout,
    font = ("Segoe UI", 10),
)

window.read()
window.close()


