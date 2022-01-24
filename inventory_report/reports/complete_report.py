from inventory_report.reports.simple_report import SimpleReport


def get_comps_stock(name, result, comp_arr):

    def have_stock(comp):
        for i in comp.items():
            if i == name:
                return comp[i]

    stock = list(filter(have_stock, comp_arr))

    if len(stock) == 0:
        comp_arr.append(result)


def get_stock_qty(data):
    comp_arr = []

    for i in range(0, len(data)):
        comp_name = data[i]['nome_da_empresa']
        res = 1
        for x in range(i + 1, len(data)):
            comp_i = data[i]['nome_da_empresa']
            comp_x = data[x]['nome_da_empresa']
            if comp_i == comp_x:
                res += 1

        result = {
            data[i]['nome_da_empresa']: res
        }

        if len(comp_arr) == 0:
            comp_arr.append(result)
        get_comps_stock(comp_name, result, comp_arr)

    return comp_arr


class CompleteReport(SimpleReport):
    def __init__(self):
        pass

    def generate(data):
        report = SimpleReport.generate(data)
        comp_arr = get_stock_qty(data)
        result = ''

        for i in comp_arr:
            for a, b in i.items():
                result += f'- {a}: {b}\n'

        return f'{report}\nProdutos estocados por empresa: \n{result}'
