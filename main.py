#from functions import get_todos, write_todos
from files import functions
import time

def todolist():
    while True:
        user_action = input("Type add ___ to add, show to show todo list, replace # to replace, complete # to complete, exit to exit: ")
        user_action = user_action.strip()

        if user_action.startswith("add"):
            try:
                todo = user_action[4:]

                todos = functions.get_todos()

                todos.append(todo + '\n')

                functions.write_todos(todos)
            except ValueError:
                print("invalid input")
                continue

        elif user_action.startswith("replace"):
            try:
                number = int(user_action[8:])
                number = number - 1

                todos = functions.get_todos()

                changed_todo = todos[number]
                chanded_todo_index = number + 1

                new_todo = input("New todo: ")
                todos[number] = new_todo + '\n'

                functions.write_todos(todos)

                message = f'item {chanded_todo_index}: {changed_todo} was changed to {new_todo}'
                print(message)
            except ValueError:
                print("invalid input")
                continue
            except IndexError:
                print("not in range of list")
                continue


        elif user_action.startswith("complete"):
            try:
                number = int(user_action[8:])
                number = number - 1

                todos = functions.get_todos()

                todo_to_remove = todos[number].strip('\n')
                todo_to_remove_index = number + 1
                todos.pop(number)

                functions.write_todos(todos)

                message = f"item {todo_to_remove_index}: {todo_to_remove} was removed from the list."
                print(message)
            except ValueError:
                print("invalid input")
                continue
            except IndexError:
                print("not in range of list")
                continue
        elif user_action.startswith("show"):
            try:
                todos = functions.get_todos()


                    #list comprehension method of removing the new line in the print function
                    #new_todos = [item.strip('\n') for item in todos]

                for index, item in enumerate(todos):
                    item = str(item.strip('\n'))
                    print(f"{index + 1}-{item}")
            except ValueError:
                print("invalid input")
                continue
        elif 'exit' in user_action:
            try:
                break
            except ValueError:
                print("invalid input")
                continue



now = time.strftime('%a %m-%d-%Y %H:%M')
print(f"It is {now}")
todolist()
