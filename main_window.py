import random

import PySimpleGUI as sg


def main():
    layout = [
        [sg.Text('Add choices with a comma between each choice')],
        [sg.Input(key='-INPUT-', size=(100,1), tooltip='Option 1, Option 2, Option 3, etc.')],
        [sg.Text(key='-OUTPUT-', size=(20,1), visible=False)],
        [sg.Button('Choose For Me'), sg.Exit()]
    ]

    window = sg.Window('Random Choice Generator', layout)

    while True:
        event, values = window.Read()
        print(event, values)  # debugging
        if event == sg.WIN_CLOSED or event == 'Exit':  # if user closes window or clicks cancel
            break

        if event == 'Choose For Me':
            print(values['-INPUT-'])
            # return random choice
            window['-OUTPUT-'].update('selected_choice', visible=True)

    window.close()
    return event, values
