import yaml

def load_data():
    
    with open("config.yml", "r") as file:
        return yaml.safe_load(file)
    

def save_data(data):

    with open("config.yml", "w") as file:
        yaml.dump(data, file, default_flow_style = False)


data = {
    "host": {
        "players": ["mustafa", "kish", "internet", "abhi"],
        "cards": []
    }
}

save_data(data)