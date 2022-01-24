from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import Inventory


class JsonImporter(Importer):
    @staticmethod
    def import_data(path):
        Inventory.check_extension(path, ".json")
        return Inventory.reader(path)
