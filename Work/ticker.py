# ticker.py

import csv
import report
import tableformat
from follow import follow
    
def select_column(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]
    # return ( [row[index] for index in indices] for row in rows )

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
    # for row in rows:
    #     yield dict(zip(headers, row))
    return ( dict(zip(headers, row)) for row in rows )

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_column(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows

# def filter_symbols(rows, names):
#     for row in rows:
#         if row['name'] in names:
#             yield row

def ticker(portfile, logfile, fmt):
    portfolio = report.read_portfolio(portfile)
    lines = follow(logfile)
    rows = parse_stock_data(lines)
    rows = (row for row in rows if row['name'] in portfolio) # generator expressions

    formatter = tableformat.create_formatter(fmt)
    formatter.headings(['Name', 'Price', 'Change'])
    for row in rows:
        rowdata = [ row['name'], f"{row['price']:0.2f}", f"{row['change']:0.2f}" ]
        formatter.row(rowdata)

def main(argv):
    if len(argv) != 4:
        raise SystemExit('Usage: %s portfoliofile logfile fmt' % argv[0])
    ticker(argv[1], argv[2], argv[3])

if __name__ == '__main__':
    import sys
    main(sys.argv)