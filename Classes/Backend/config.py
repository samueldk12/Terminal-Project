class Config():

    def __init__(self):
        self.path_config = 'C:\\Users\\samuel.arao\\projects\\cli_project\\config\\cpconfig.cg'
        self.config_dict = {}
        self.transform_cpconfi_to_dict()

    def get_config_dict(self):
        return  self.config_dict

    def transform_cpconfi_to_dict(self):
        import re
        with open(self.path_config,'r') as config:
            for config_desc in config.readlines():
                if re.match(r'[a-zA-Z0-9_]+\.[a-zA-Z0-9_]+',config_desc):
                    key, value = config_desc.split('=')
                    last_words = ''
                    for word in key.split('.'):
                        last_words += f"{{'{word.strip()}':"
                    value = value.replace('\n','').replace('\\','\\\\').strip()
                    len_keys = len(key.split('.'))
                    if "'" not in value:
                        last_words += r"'" + value + "'" + "}" * len_keys
                    else:
                        last_words +=  value + r"}" * len_keys 
                    
                    last_words = dict(eval(last_words))
                    first_key_lw = list(last_words.keys())[0]
                    if  first_key_lw in self.config_dict:
                        self.config_dict[first_key_lw] = last_words[first_key_lw] | self.config_dict[first_key_lw]
                    else:
                        self.config_dict.update(last_words)
                    
                print(self.config_dict)
             
                            
