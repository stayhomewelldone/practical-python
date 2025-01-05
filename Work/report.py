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
        portfolio = {} # Initial, list of dicts
        for row in rows: 
                print(row)
                try:
                     portfolio[row[0]] = float(row[1]) 
                except ValueError:
                     print("Couldn't parse", row)
                except IndexError as e:
                     print(f'Indexerror occured:{e}')
               
        return portfolio
def read_prices(filename):
    'Read the contents of prices, and returns a dict'
    with open(filename, 'rt') as f:
     
        rows = csv.reader(f)
        headers = next(rows)
        prices = {} # Initial dict
        for row in rows: 
                print(row)
                try:
                     prices[row[0]] = float(row[1]) 
                except ValueError:
                     print("Couldn't parse", row)
                except IndexError as e:
                     print(f'Indexerror occured:{e}')
               
        return prices
if len(sys.argv) == 2:
     filename = sys.argv[1]
else:
     filename = ('Data/prices.csv')
# portfolio = read_portfolio(filename)
prices = read_prices(filename)


# print(f'Portfolio dict {portfolio}')
print(f'Prices dict {prices}')