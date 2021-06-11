# pcost.py
#
# Exercise 1.27
f = open('Data/portfolio.csv', 'rt')
headers = next(f).split(',')
total_cost = 0

for line in f:
    row = line.split(',')
    row[1] = int(row[1])
    row[2] = float(row[2])
    cost = row[1] * row[2]
    total_cost = total_cost + cost

print(f'Total cost: {total_cost:0.2f}')
f.close()