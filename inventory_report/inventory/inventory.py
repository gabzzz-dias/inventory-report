import csv
import json
import xml.etree.ElementTree as Et
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def csv_reader(path):
        with open(path) as file:

            return list(csv.DictReader(file))

    @staticmethod
    def json_reader(path):
        with open(path) as file:

            return json.load(file)

    @staticmethod
    def xml_reader(path):
        root = Et.parse(path).getroot()
        resp = []
        for i in root:
            res = {}
            for x in i:
                res[x.tag] = x.text
            resp.append(res)

        return resp

    @classmethod
    def reader(cls, path):
        if ".csv" in path:
            return cls.csv_reader(path)
        elif ".json" in path:
            return cls.json_reader(path)
        elif ".xml" in path:
            return cls.xml_reader(path)

    @classmethod
    def check_extension(cls, path, extension):
        if extension not in path:
            raise ValueError("Arquivo inválido")

    @classmethod
    def import_data(cls, path, report_type):
        read_method = cls.reader(path)
        if report_type == "simples":
            return SimpleReport.generate(read_method)
        else:
            return CompleteReport.generate(read_method)
