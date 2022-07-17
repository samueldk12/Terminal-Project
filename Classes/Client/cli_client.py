from PySimpleGUI import Window
import PySimpleGUI as sg

class CliClient():
    def __init__(self,config_list=None):
        self.config_list = config_list
        self.commands = []
        self.window = None
        self.start_window()


    def get_window(self):
        return self.window
    
    def add_command(self,command,result):
        self.commands.append((self.ps1,command,result))
        self.update_layout()

    def update_layout(self):
        cli_history = []
        for ps1,command,result in  self.commands:
            cli_history.append([
                [
                    self.get_ps1_text_object(ps1),
                    sg.Text(command
                        ,auto_size_text=self.config_list['text']['auto_size']
                        ,text_color=self.config_list['text']['color']
                        ,background_color=self.config_list['text']['background_color']
                    )
                ],
                [
                    sg.Text(result
                        ,auto_size_text=self.config_list['text']['auto_size']
                        ,text_color=self.config_list['text']['color']
                        ,background_color=self.config_list['text']['background_color']
                    )
                ]
            ])
        layout = [[ 
                    cli_history,
                    [
                    self.get_ps1_text_object(ps1),
                    sg.In(
                        text_color=self.config_list['text']['color']
                        ,background_color=self.config_list['text']['background_color']
                        ,border_width=0
                        ,focus=True
                        ,key='input-p'
                    )
                    ]
                ]]
        self.update_screen(layout=layout)

    def update_screen(self,layout):
        if self.window:
            self.window.close()
        self.window = Window(
            'Python CLI',
            size=(self.config_list['window']['width'],self.config_list['window']['height']),
            background_color=self.config_list['window']['background_color'],
            icon=self.config_list['window']['icon'],
            layout=[layout],
            finalize=True
        )
        self.window.force_focus()
        self.window['input-p'].set_focus()
      
    def start_window(self): 
        layout = [
                    self.get_ps1_text_object(),
                    sg.In(
                         text_color=self.config_list['text']['color']
                        ,background_color=self.config_list['text']['background_color']
                        ,border_width=0
                        ,focus=True
                        ,key='input-p'
                    )
                ]
        self.update_screen(layout)
       

    def get_ps1(self):
        import re
        from datetime import date
        import datetime
        import platform
        termina_config = self.config_list['terminal']['config']
        ps1 = ''
        for match in re.findall(r'\%([a-zA-Z0-9]+)',termina_config):
            if match == 'd':
                ps1 += str(date.today())
            elif match == 'O':
                ps1 += f' {platform.platform()}'
            elif match == 'n':
                ps1 += str(datetime.datetime.now())
            elif len(match) > 1:
                ps1 += match
            
        ps1 += '>'
        return ps1

    def get_ps1_text_object(self,ps1=None):
        if ps1:
            ps1 = ps1
        else:
            ps1 = self.get_ps1()
        self.ps1 = ps1 
        return sg.Text (     
                            ps1
                            ,auto_size_text=self.config_list['text']['auto_size']
                            ,text_color=self.config_list['text']['color']
                            ,background_color=self.config_list['text']['background_color']
                            ,key='current_ps1'
                        )

    def close_window(self):
        self.window.close()
