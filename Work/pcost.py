# pcost.py
#
# Exercise 1.30 - 1.33
import sys
import csv
def portfolio_cost(filename):
    f = open(filename, 'rt')
    rows = csv.reader(f)
    headers = next(rows)
    total_cost = 0

    for row in rows:
        try:
            row[1] = int(row[1])
            row[2] = float(row[2])
            cost = row[1] * row[2]
            total_cost = total_cost + cost
        except ValueError:
            print("Couldn't parse", row)
        
    f.close()
    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost: {cost:0.2f}')
