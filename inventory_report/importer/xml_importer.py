
from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import Inventory


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        Inventory.check_extension(path, ".xml")

        return Inventory.reader(path)
