from Classes.Client.cli_client import CliClient
from Classes.Backend.config import Config

def exec():
    config = Config()
    config_dict = config.get_config_dict()
    application = CliClient(config_dict)
   
exec()