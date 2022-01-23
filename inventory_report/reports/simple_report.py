from datetime import datetime, date


def get_fab_date(arr):
    expiration = arr[0]['data_de_fabricacao']
    fab_date = datetime.strptime(expiration, '%Y-%m-%d').date()

    for fab in arr:
        string_date = fab['data_de_fabricacao']
        format = datetime.strptime(string_date, '%Y-%m-%d').date()
        if (format < fab_date):
            fab_date = format
    return fab_date


def get_expiration_date(arr):
    today = date.today()
    expiration = arr[0]['data_de_validade']
    expiration_date = datetime.strptime(expiration, '%Y-%m-%d').date()
    for fab in arr:
        string_date = fab['data_de_validade']
        format = datetime.strptime(string_date, '%Y-%m-%d').date()
        if (expiration_date > format > today):
            expiration_date = format
    return expiration_date


def get_greater_stock(arr):
    greater_stock = 1
    comp = ''
    for i in range(0, len(arr)):
        resp = 1
        for x in range(i+1, len(arr)):
            comp_i = arr[i]['nome_da_empresa']
            comp_x = arr[x]['nome_da_empresa']
            if comp_i == comp_x:
                resp += 1
        if resp > greater_stock:
            greater_stock = resp
            comp = comp_i
    return comp


class SimpleReport:
    def __init__(self):
        pass

    def generate(list):
        fab_date = get_fab_date(list)
        expiration_date = get_expiration_date(list)
        comp = get_greater_stock(list)

        report = {
            'Data de fabricação mais antiga': fab_date,
            'Data de validade mais próxima': expiration_date,
            'Empresa com greater_stock quantidade de fabutos estocados': comp
        }

        result = ''
        for k, e in report.items():
            result += f'{k}: {e}'
            result += '\n'

        return result
