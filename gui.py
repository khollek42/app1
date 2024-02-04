import files.functions as functions
import PySimpleGUI as sg
import time

sg.theme("LightGreen4")

clock = sg.Text('', key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(),
                      key='todos',
                      enable_events=True,
                      size=[45, 10])
edit_buttion = sg.Button("Edit")
complete_button = sg.Button("Complete", key='complete')
exit_button = sg.Button("Exit", key="exit")

layout = [[clock],
          [label, input_box, add_button],
          [list_box, edit_buttion, complete_button],
          [exit_button]]

window = sg.Window("To-Do List App",
                   layout=layout,
                   font=("Helvetica", 15))

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime('%a %m-%d-%Y %H:%M'))

    #shows values of the event and the values of the instances(vlaues)
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
                sg.popup("Please select a item first", font=15)

        case "complete":

            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select a item first", font=15)

        case "exit":
            break

        case "todos":
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break


window.close()
