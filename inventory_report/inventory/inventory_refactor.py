import csv
import json
import xml.etree.ElementTree as Et
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class InventoryRefactor:
    def __init__(self, importer):
        self.data = []
        self.importer = importer

    def __iter__(self):
        return InventoryIterator(self.data)

    @staticmethod
    def csv_reader(file_path):
        with open(file_path) as file:

            return list(csv.DictReader(file))

    @staticmethod
    def json_reader(file_path):
        with open(file_path) as file:

            return json.load(file)

    @staticmethod
    def xml_reader(file_path):
        root = Et.parse(file_path).getroot()
        read_method = []

        for i in root:
            result = {}
            for x in i:
                result[x.tag] = x.text
            read_method.append(result)

        return read_method

    @classmethod
    def reader(cls, file_path):
        if ".csv" in file_path:
            return cls.csv_reader(file_path)
        elif ".json" in file_path:
            return cls.json_reader(file_path)
        elif ".xml" in file_path:
            return cls.xml_reader(file_path)

    @classmethod
    def check_extension(cls, file_path, extension):
        if extension not in file_path:
            raise ValueError("Arquivo inválido")

    def import_data(self, file_path, report_type):
        self.data += self.importer.import_data(file_path)
        reader = self.reader(file_path)
        if report_type == "simples":

            return SimpleReport.generate(reader)
        else:

            return CompleteReport.generate(reader)
