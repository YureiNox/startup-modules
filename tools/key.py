import json
import os

class jinfo:
    def __init__(self):
        with open(os.path.join(os.path.dirname(__file__), 'json/startup.json')) as f:
            self.data = json.load(f)

    def get_value(self, balise):
        if balise in self.data:
            return self.data[balise]
        else:
            available_keys = ', '.join(self.data.keys())
            return f"Balise '{balise}' not found. Here are the available options: {available_keys}"

    def get_all(self):
        return self.data
