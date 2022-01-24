from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(file_path):
        type_file = file_path.split('.')[-1]
        if type_file != 'csv':
            raise ValueError('Arquivo inválido')
        with open(file_path) as file:
            content = csv.DictReader(file, delimiter=",", quotechar='"')
            list_data = []

            for item in content:
                list_data.append(item)
        return list_data
