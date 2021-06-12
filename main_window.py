import random

import PySimpleGUI as sg


def main():
    sg.theme('DarkGrey11')

    layout = [
        [sg.Text('Add choices with a comma between each choice')],
        [sg.Input(key='-INPUT-', size=(100, 1), tooltip='Option 1, Option 2, Option 3, etc.', enable_events=True)],
        [sg.Text(key='-OUTPUT-', visible=False, size=(50, 1), font=('Microsoft JhengHei', 20))],
        [sg.Button('Choose For Me', bind_return_key=True), sg.Exit()],
    ]

    window = sg.Window('Random Choice Generator', layout)

    while True:
        event, values = window.Read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        if event == 'Choose For Me':
            selected_choice = select_rand_choice(values['-INPUT-'])
            window['-OUTPUT-'].update(selected_choice, visible=True)

    window.close()
    return event, values


def select_rand_choice(str):
    if not str:  # checks if string is empty
        return 'No choices to choose from'

    choices = str.split(',')
    return random.choice(choices).strip()  # strip() trims any white spaces
