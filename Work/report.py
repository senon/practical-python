# report.py
#
# Exercise 2.16
import csv

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
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
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
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
    '''
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    '''
    report = []
    for stock in portfolio:
        curr_price = prices[stock['name']]
        change = curr_price - stock['price']
        record = (stock['name'], stock['shares'], curr_price, change)        
        report.append(record)    

    return report

def print_report(report):
    '''
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    '''
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-'*10 + ' ') * len(headers))

    for row in report:
        print('%10s %10d %10.2f %10.2f' % row)

def portfolio_report(portfolio_filename, prices_filename):
    '''
    Make a stock report given portfolio and price data files.
    '''
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)


portfolio_report('Data/portfolio.csv', 'Data/prices.csv')

