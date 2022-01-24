from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from pathlib import Path
import csv
import json
import xml.etree.ElementTree as ET


class Read:
    @classmethod
    def reader(cls, path):
        extension = Path(path).suffix
        result = ""

        if extension == ".csv":
            result = cls.csv_reader(path)
        elif extension == ".json":
            result = cls.json_reader(path)
        else:
            result = cls.xml_reader(path)

        return result

    def xml_reader(data):
        file = ET.parse(data).getroot()
        result = []

        for i in file:
            res = {}
            for x in i:
                res[x.tag] = x.text
            result.append(res)

        return result

    def json_reader(path):
        with open(path) as json_path:
            result = json.load(json_path)

        return result

    def csv_reader(path):
        result = []

        with open(path) as csv_path:
            data = csv.DictReader(csv_path)

            for i in data:
                result.append(i)

        return result


class Inventory:
    @staticmethod
    def import_data(path, version):
        report = Read.reader(path)
        result = ""

        if version == "simples":
            result = SimpleReport.generate(report)
        else:
            result = CompleteReport.generate(report)

        return result
