import yaml

def load_data():
    
    with open("Database/config.yml", "r") as file:
        return yaml.safe_load(file)
    
def save_data(data):

    with open("Database/config.yml", "w") as file:
        yaml.dump(data, file, default_flow_style = False)

def load_afk():
    
    with open("Database/afk.yml", "r") as file:
        return yaml.safe_load(file)

def save_afk(afk_data):

    with open("Database/afk.yml", "w") as file:
        yaml.dump(afk_data, file, default_flow_style = False)