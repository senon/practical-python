# report.py
#
# Exercise 2.5
import csv

def read_portfolio(filename):

    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers, row))
            portfolio.append(record)    
    
    return portfolio

# Exercise 2.6
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

# Exercise 2.16
portfolio = read_portfolio('Data/portfoliodate.csv')
prices = read_prices('Data/prices.csv')

total_gain = 0

for stock in portfolio:
    curr_price = prices[stock['name']]
    nshares = int(stock['shares'])
    price = float(stock['price'])
    total_gain += nshares * (curr_price - price)

print(f'Total gain: {total_gain:0.2f}')

# Exercise 2.9
def make_report(portfolio, prices):

    report = []
    for stock in portfolio:
        curr_price = prices[stock['name']]
        price = float(stock['price'])
        change = curr_price - price
        nshares = int(stock['shares'])
        record = (stock['name'], nshares, curr_price, change)
        report.append(record)    

    return report

report = make_report(portfolio, prices)

headers = ('Name', 'Shares', 'Price', 'Change')
print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
print(('-'*10 + ' ')*4)

for name, shares, price, change in report:    
    print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')