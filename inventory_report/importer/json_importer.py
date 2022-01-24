from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import json_reader


class JsonImporter(Importer):
    def import_data(path):
        if not path.endswith('.json'):
            raise ValueError('Arquivo inválido')

        return json_reader(path)
