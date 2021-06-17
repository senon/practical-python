#!/usr/bin/env python3
# report.py
#
# Exercise 2.16
import fileparse 

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    with open(filename, 'rt') as file:
        portfolio = fileparse.parse_csv(file, select=['name','shares','price'], types=[str, int, float])
    
    return portfolio

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    with open(filename, 'rt') as file:
        prices = fileparse.parse_csv(file, types=[str, float], has_headers=False)
    
    return dict(prices)

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

def main(argv):    
    # portfolio_report('Data/portfolio.csv', 'Data/prices.csv')

    if len(argv) != 3:
        raise SystemExit(f'usage: {argv[0]} ' 'portfoliofile pricefile')

    portfoliofile = argv[1]
    pricefile = argv[2]
    portfolio_report(portfoliofile, pricefile)

if __name__ == '__main__':
    import sys
    main(sys.argv)

