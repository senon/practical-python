# report.py
#
# Exercise 2.16
import csv

def read_portfolio(filename):

    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers, row))
            stock = {
                'name'  : record['name'],
                'shares': int(record['shares']),
                'price' : float(record['price'])
            }

            portfolio.append(stock)    
    
    return portfolio

def read_prices(filename):

    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                # print('list index out of range', row)
                pass
    
    return prices

def make_report(portfolio, prices):

    report = []
    for stock in portfolio:
        curr_price = prices[stock['name']]
        change = curr_price - stock['price']
        record = (stock['name'], stock['shares'], curr_price, change)        
        report.append(record)    

    return report

portfolio = read_portfolio('Data/portfoliodate.csv')
prices = read_prices('Data/prices.csv')

report = make_report(portfolio, prices)

headers = ('Name', 'Shares', 'Price', 'Change')
#print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
print('%10s %10s %10s %10s' % headers)
print(('-'*10 + ' ') * len(headers))

# for name, shares, price, change in report:    
#     print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')
for row in report:
    print('%10s %10d %10.2f %10.2f' % row)
