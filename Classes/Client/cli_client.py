from PySimpleGUI import Window
import PySimpleGUI as sg

class CliClient():
    def __init__(self,config_list=None):
        self.config_list = config_list
        self.start_window()
        self.commands = []

    def start_window(self):
        if len(self.commands) == 0:
            layout = [
                        self.get_ps1_text_object(),
                        sg.In(
                             text_color=self.config_list['text']['color']
                            ,background_color=self.config_list['text']['background_color']
                            ,border_width=0
                            ,focus=True
                        )
                     ]
        else:
            cli_history = []
            for ps1,command,result in  self.commands:
                cli_history.append([
                    [
                        self.get_ps1_text_object(ps1),
                        sg.Text(command
                            ,auto_size_text=self.config_list['text']['auto_size']
                            ,text_color=self.config_list['text']['color']
                            ,background_color=self.config_list['text']['background_color']
                        ),
                        sg.Text(result
                            ,auto_size_text=self.config_list['text']['auto_size']
                            ,text_color=self.config_list['text']['color']
                            ,background_color=self.config_list['text']['background_color']
                        )
                    ]
                ])
            
            layout = [ 
                       cli_history
                    ]
                    
        self.window = Window(
            'Python CLI',
            size=(self.config_list['window']['width'],self.config_list['window']['height']),
            background_color=self.config_list['window']['background_color'],
            icon=self.config_list['window']['icon'],
            layout=layout
        )

        self.window.read()

    def get_ps1(self):
        import re
        from datetime import date
        import platform
        termina_config = self.config_list['terminal']['config']
        ps1 = ''
        for match in re.findall(r'\%([a-zA-Z0-9]+)',termina_config):
            if match == 'd':
                ps1 += str(date.today())
            elif match == 'O':
                ps1 += f' {platform.platform()}'
            elif len(match) > 1:
                ps1 += match
            
        ps1 += '>'
        return ps1

    def get_ps1_text_object(self,ps1=None):
        if ps1:
            ps1 = ps1
        else:
            ps1 = self.get_ps1()

        return sg.Text (     
                            ps1
                            ,auto_size_text=self.config_list['text']['auto_size']
                            ,text_color=self.config_list['text']['color']
                            ,background_color=self.config_list['text']['background_color']
                        )

    def close_window(self):
        self.window.close()
