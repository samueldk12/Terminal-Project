from Classes.Client.cli_client import CliClient
from Classes.Backend.config import Config
from Classes.Backend.command import Command
import PySimpleGUI as sg


def exec():
    config = Config()
    config_dict = config.get_config_dict()
    application = CliClient(config_dict)
    window = application.get_window()
    window['input-p'].bind('<Return>','_Enter')
    while True:
        event, values = window.read()
        if event not in (sg.WIN_CLOSED,'_EXIT_', 'Close'):
            if event == "input-p" + "_Enter":
                command = Command(values['input-p'])
                application.add_command(values['input-p'],command.get_result())
                window = application.get_window()
                window['input-p'].bind('<Return>','_Enter')
        else:
            break
      
exec()