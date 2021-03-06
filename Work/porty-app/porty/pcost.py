#!/usr/bin/env python3
# pcost.py
#
# Exercise 1.30 - 1.33
from . import report

def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    total_cost = 0

    portfolio = report.read_portfolio(filename)
    return portfolio.total_cost

    # for stockno, stock in enumerate(portfolio, start=1):
    #     try:
    #         total_cost += stock['shares'] * stock['price']
    #     except ValueError as e:
    #         print(f'Row {stockno}: {stock}')
    #         print(f'Row {stockno}: Reason {e}')
    # return total_cost

def main(argv):
    if len(argv) != 2:
        raise SystemExit(f'usage: {argv[0]} ' 'portfoliofile')

    portfoliofile = argv[1]
    cost = portfolio_cost(portfoliofile)
    print('Total cost: %0.2f' % cost)

if __name__ == '__main__':
    import sys
    main(sys.argv)