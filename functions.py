FILEPATH = "text_folder/todos.txt"


def get_todos(filepath=FILEPATH):
    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos


def write_todos(todos_arg, filepath=FILEPATH):
    with open("text_folder/todos.txt", "w") as file:
        file.writelines(todos_arg)
