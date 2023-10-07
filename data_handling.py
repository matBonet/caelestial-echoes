import astropy

class FitsImporter:
    def __init__(self, filepath: str):
        self.filepath = filepath
        with open(filepath, 'r') as data:
            pass