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
            holding = {headers[0]: row[0], 
                        headers[1]: int(row[1]), 
                        headers[2]: float(row[2])}
            portfolio.append(holding)    
    
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

# Exercise 2.7
portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

total_gain = 0

for stock in portfolio:
    curr_price = prices[stock['name']]
    total_gain += stock['shares'] * (curr_price - stock['price'])

print(f'Total gain: {total_gain:0.2f}')

# Exercise 2.9
def make_report(portfolio, prices):

    report = []
    for stock in portfolio:
        curr_price = prices[stock['name']]
        change = curr_price - stock['price']
        record = (stock['name'], stock['shares'], curr_price, change)
        report.append(record)    

    return report

report = make_report(portfolio, prices)

headers = ('Name', 'Shares', 'Price', 'Change')
print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
print(('-'*10 + ' ')*4)

for name, shares, price, change in report:    
    print(f'{name:>10s} {shares:>10d} ${price:>10.2f} {change:>10.2f}')