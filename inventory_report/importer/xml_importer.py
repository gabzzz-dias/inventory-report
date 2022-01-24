from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import xml_reader


class XmlImporter(Importer):
    def import_data(path):
        if not path.endswith('.xml'):
            raise ValueError('Arquivo inválido')

        return xml_reader(path)
