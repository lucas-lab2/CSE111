import PySimpleGUI as sg

# Set a modern theme for a nicer look
sg.theme('DarkBlue3')

def create_main_window():
    """Creates and returns the main window."""
    # Start with one task row using descriptive placeholder text.
    task_row = [
        [sg.Checkbox('', key='checkbox_0'),
         sg.Input('Enter task here...', key='input_0', size=(30, 1))]
    ]
    layout = [
        [sg.Frame('Tasks', layout=task_row, key='container', font=('Helvetica', 12))],
        [sg.Button('New Task', font=('Helvetica', 12)),
         sg.Button('Reset', font=('Helvetica', 12))]
    ]
    return sg.Window('Todo List', layout=layout, finalize=True, font=('Helvetica', 12))

def add_task(window, task_count):
    """Adds a new task (checkbox and input field) to the tasks container."""
    new_task = [sg.Checkbox('', key=f'checkbox_{task_count}'),
                sg.Input('Enter task here...', key=f'input_{task_count}', size=(30, 1))]
    window.extend_layout(window['container'], [new_task])

def reset_window(window):
    """Resets the window by closing the current one and creating a new main window."""
    window.close()
    return create_main_window()

def main():
    """Main function to run the Todo List application."""
    window = create_main_window()
    task_count = 1  # Counter for the number of tasks; one task is already present.
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'New Task':
            add_task(window, task_count)
            task_count += 1
        elif event == 'Reset':
            window = reset_window(window)
            task_count = 1
    window.close()

if __name__ == "__main__":
    main()
