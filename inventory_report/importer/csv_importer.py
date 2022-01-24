from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(path):
        extension = path.split('.')[-1]

        if extension != 'csv':
            raise ValueError('Arquivo inválido')

        with open(path) as file:
            data = csv.DictReader(file, delimiter=",", quotechar='"')
            result = []

            for i in data:
                result.append(i)
        return result
