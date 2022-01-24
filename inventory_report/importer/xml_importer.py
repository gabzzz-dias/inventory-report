from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import xml_reader
from pathlib import Path


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        extension = Path(path).suffix

        if extension != '.xml':
            raise ValueError('Arquivo inválido')
        return xml_reader(path)
