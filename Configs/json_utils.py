import json

def load_afk() -> dict:
    
    with open("Database/afk.json", "r") as file:
        return json.load(file)

def save_afk(afk_data: dict) -> None:

    with open("Database/afk.json", "w") as file:
        json.dump(afk_data, file, indent = 4)