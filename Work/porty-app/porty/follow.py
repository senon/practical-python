# follow.py
import os
import time

def follow(filename):
    with open(filename, 'rt') as f:
        f.seek(0, os.SEEK_END)

        while True:
            line = f.readline()
            if line == '':
                time.sleep(0.1)
                continue
            yield line

def main(argv):
    import report

    portfolio = report.read_portfolio('Data/portfolio.csv')

    for line in follow('Data/stocklog.csv'):
        row = line.split(',')
        name = row[0].strip('"')
        price = float(row[1])
        change = float(row[4])
        if name in portfolio:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')

if __name__ == '__main__':
    import sys
    main(sys.argv)