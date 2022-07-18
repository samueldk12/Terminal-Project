

class Command():

    def __init__(self,command):
        self.command = self.get_command(command)
        self.params  = self.get_params(command)
        self.result  = self.process_result(self.command,self.params)

    def get_result(self):
        return self.result

    def get_command(self, command):
        return list(command.split(' '))[0].capitalize()
    
    def get_params(self, command):
        return list(map(lambda x: x.lower(),command.split(' ')[1:]))

    def process_result(self,command, params):
        import importlib
        try:
            module = importlib.import_module(f'Classes.Backend.{command.lower()}')
            command_class = getattr(module , command)
            instance = command_class(params)
            result = None
            while not result:
               result =  instance.result
            return result
        except:
            return "Invalid Command"


    
