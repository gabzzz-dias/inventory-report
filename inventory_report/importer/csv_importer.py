from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import Inventory


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        Inventory.check_extension(path, ".csv")
        return Inventory.reader(path)
