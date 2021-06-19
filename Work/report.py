#!/usr/bin/env python3
# report.py
#
# Exercise 2.16
import fileparse 
import stock
import tableformat
from portfolio import Portfolio

def read_portfolio(filename, **opts):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    with open(filename, 'rt') as file:
        portdicts = fileparse.parse_csv(file, 
                                        select=['name','shares','price'], 
                                        types=[str, int, float],
                                        **opts)    
    
    # portfolio = [ stock.Stock(d['name'], d['shares'], d['price']) for d in portdicts ]
    portfolio = [ stock.Stock(**d) for d in portdicts ]
    return Portfolio(portfolio)

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
    for s in portfolio:
        curr_price = prices[s.name]
        change = curr_price - s.price
        record = (s.name, s.shares, curr_price, change)        
        report.append(record)    

    return report

def print_report(reportdata, formatter):
    '''
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    '''
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in reportdata:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)


def portfolio_report(portfolio_filename, prices_filename, fmt='txt'):
    '''
    Make a stock report given portfolio and price data files.
    '''
    # Read data files
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)

    # Create the report data
    report = make_report(portfolio, prices)

    # Print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)

def main(argv):    
    # portfolio_report('Data/portfolio.csv', 'Data/prices.csv')

    if len(argv) != 4:
        raise SystemExit(f'usage: {argv[0]} ' 'portfoliofile pricefile fmt="txt"')

    portfoliofile = argv[1]
    pricefile = argv[2]
    fmt = argv[3]
    portfolio_report(portfoliofile, pricefile, fmt)

if __name__ == '__main__':
    import sys
    main(sys.argv)

