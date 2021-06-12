import PySimpleGUI as sg
import main_window
import sys


def main():
    starter_event, starter_values = main_window.main()
    if (starter_event == sg.WIN_CLOSED):
        sys.exit()


if __name__ == '__main__':
    main()
