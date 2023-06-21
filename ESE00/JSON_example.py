import json 

data = {
    "country": "Germany",
    "vehicle": {
        "name": "Volkswagen",
        "model": "T-Roc"
    }
}

with open("file.json", "w") as file:
    json.dump(data, file)
