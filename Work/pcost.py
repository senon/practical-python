# pcost.py
#
# Exercise 1.30 - 1.33
import report

def portfolio_cost(filename):
    total_cost = 0

    portfolio = report.read_portfolio(filename)
    for stockno, stock in enumerate(portfolio, start=1):
        try:
            total_cost += stock['shares'] * stock['price']
        except ValueError as e:
            print(f'Row {stockno}: {stock}')
            print(f'Row {stockno}: Reason {e}')

    return total_cost

import sys
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    #filename = 'Data/portfolio.csv'
    filename = input('Enter a filename:')

cost = portfolio_cost(filename)
print('Total cost: %0.2f' % cost)
