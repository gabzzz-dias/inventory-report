from .importer import Importer
from pathlib import Path
import csv


class CsvImporter(Importer):
    def import_data(path):
        extension = Path(path).suffix
        result = []

        if extension != ".csv":
            raise ValueError("Arquivo inválido")
        else:
            with open(path) as file:
                data = csv.DictReader(file)

                for i in data:
                    result.append(i)

        return result
