from .importer import Importer
from pathlib import Path
import json


class JsonImporter(Importer):
    def import_data(path):
        extension = Path(path).suffix
        result = []

        if extension != ".json":
            raise ValueError("Arquivo inválido")
        else:
            with open(path) as file:
                result = json.load(file)

        return result
