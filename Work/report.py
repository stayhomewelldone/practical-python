# report.py
#
# Exercise 2.4
import csv
import sys
def read_portfolio(filename):
    'Read the contents of a portfolio'
    with open(filename, 'rt') as f:
     
        rows = csv.reader(f)
        headers = next(rows)
        portfolio = [] # Initial, list of dicts
        for row in rows: 
           
                try:
                     holding = {'name': row[0],"share": int(row[1]), 'price': float(row[2]) } 
                     portfolio.append(holding)
                except ValueError:
                     print("Couldn't parse", row)
        return portfolio
if len(sys.argv) == 2:
     filename = sys.argv[1]
else:
     filename = ('Data/portfolio.csv')
portfolio = read_portfolio(filename)

print(f'Portfolio dict {portfolio}')