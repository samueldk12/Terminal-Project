from PySimpleGUI import Window

class CliClient():
    def __init__(self,config_list=None):
        self.config_list = config_list
        self.start_window()

    def start_window(self):
        self.window = Window(
            'Python CLI',
            #size(self.config_list['window']['width'],self.config_list['window']['height']),
            size=(800,400),
            #background_color=self.config_list['window']['background_color'],
            background_color='#000',
            #icon=self.config_list['window']['icon'],
            icon=r'C:\Users\samuel.arao\projects\cli_project\Assets\Images\icon.ico',
            layout=[[]]
        )
        self.window.read()


    def close_window(self):
        self.window.close()
