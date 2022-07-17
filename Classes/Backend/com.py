class Com():
    def __init__(self,params):
        self.params = params
        self.result = None
        self.process_result(params)

    def process_result(self,params):
        import subprocess
        try:
            p = subprocess.Popen(params, 
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE)
            out, err = p.communicate()
            self.result = out.decode('ISO-8859-1')
        except:
            self.result = 'Error in command!'