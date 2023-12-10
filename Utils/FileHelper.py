import pickle
from pathlib import Path
def write_to_file(data):
    with open("saved_data", 'wb+') as f:
        pickle.dump(data, f)
def read_from_file():
    if not Path("saved_data").is_file():
        return []
    return pickle.load(open("saved_data", 'rb'))