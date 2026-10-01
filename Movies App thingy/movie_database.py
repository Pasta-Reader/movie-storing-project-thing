import os
import json

class MoviesAnimeDatabase:
    def __init__(self, filename="mymovies.json"):
        # Automatically find the directory where this script runs
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.file_path = os.path.join(self.script_dir, filename)

    def load(self):
        """Loads data from the JSON file or returns an empty dictionary."""
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                return json.load(file)
        return {}

    def save(self, data_dict):
        """Saves a dictionary directly into the JSON file."""
        with open(self.file_path, "w") as file:
            json.dump(data_dict, file, indent=4)
