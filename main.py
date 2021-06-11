import PySimpleGUI as sg
import main_window


def main():
    starter_event, starter_values = main_window.main()
    if (starter_event == sg.WIN_CLOSED):
        exit(0)


if __name__ == '__main__':
    main()
