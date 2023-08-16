from configparser import ConfigParser


credential_path = "./configs/credential.ini"
param_path = "./configs/param.ini"

# credential config
credential_config = ConfigParser()
credential_config.read(credential_path)

# param config
param_config = ConfigParser()
param_config.read(param_path)

# credential
bot_token = credential_config.get("default", "bot_tele_token")

# input
chat_id = credential_config.get("input", "chat_id")
