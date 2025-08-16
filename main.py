from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_input = input("Type ADD, SHOW, EDIT, COMPLETE or QUIT: ").strip()
    todos = get_todos()

    if user_input.startswith("add"):
        todo = user_input[4:]
        todos.append(todo + "\n")

        write_todos(todos)

    elif user_input.startswith("show"):
        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}. {item}"
            print(row)

    elif user_input.startswith("edit"):
        try:
            number = int(user_input[5:]) - 1
            todos[number] = todos[number].strip("\n")
            edit_todo = input(f"Change {todos[number]} to: ")
            todos[number] = edit_todo + "\n"

            write_todos(todos)


        except ValueError:
            print("Invalid input. Please try again.")
            continue

    elif user_input.startswith("complete"):
        try:
            number = int(user_input[9:]) - 1
            todos.pop(number)

            write_todos(todos)


        except IndexError:
            print(
                f"Invalid input. Only {len(todos)} items in list. Please try again."
            )
            continue

        except ValueError:
            print(f"Invalid input. Please enter a number.")
            continue

    elif user_input.startswith("quit"):
        break

    else:
        print("Invalid input")
