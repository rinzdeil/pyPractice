import zipfile
import pathlib

def make_archive(filepaths, dest_folder, filename):
    dest_path = pathlib.Path(dest_folder, f"{filename}.zip")
    with zipfile.ZipFile(dest_path, "w") as zip:
        for file in filepaths:
            file = pathlib.Path(file)
            zip.write(file, arcname=file.name)
            print(file)

if __name__ == "__main__":
    make_archive(filepaths=["filenames.py", "questions.py"], dest_folder=r"..\text_folder")