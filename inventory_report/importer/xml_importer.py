from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import xml_reader


class XmlImporter(Importer):
    def import_data(file_path):
        if not file_path.endswith('.xml'):
            raise ValueError('Arquivo inválido')
        return xml_reader(file_path)
