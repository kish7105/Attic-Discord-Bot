import json

def load_data():
    
    with open("Database/config.json", "r") as file:
        return json.load(file)
    
def save_data(data):

    with open("Database/config.json", "w") as file:
        json.dump(data, file, indent = 4)

def load_afk():
    
    with open("Database/afk.json", "r") as file:
        return json.load(file)

def save_afk(afk_data):

    with open("Database/afk.json", "w") as file:
        json.dump(afk_data, file, indent = 4)