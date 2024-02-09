import files.functions as functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open('todos.txt', 'w') as file:
        pass

sg.theme("LightGreen4")

clock = sg.Text('', key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button(tooltip="Add button", image_source="add.png",
                       size=2, mouseover_colors=("medium sea green"), key='Add')
list_box = sg.Listbox(values=functions.get_todos(),
                      key='todos',
                      enable_events=True,
                      size=[45, 10])
edit_buttion = sg.Button("Edit")
complete_button = sg.Button("Complete", key='complete')
exit_button = sg.Button("Exit", key="exit")

layout = [[clock],
          [label],
          [input_box, add_button],
          [list_box, edit_buttion, complete_button],
          [exit_button]]

window = sg.Window("To-Do List App",
                   layout=layout,
                   font=("Helvetica", 15))

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime('%a %m-%d-%Y %H:%M'))

    #shows values of the event and the values of the instances(values)
    #print(event)
    #print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)



        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)

            except IndexError:
                sg.popup("Please select an item first", font=15)

        case "complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first", font=15)
            except ValueError:
                continue

        case "exit":
            break

        case "todos":
            try:
                window['todo'].update(value=values['todos'][0])
            except IndexError:
                sg.popup("Todos Completed")
        case sg.WIN_CLOSED:
            break


window.close()
