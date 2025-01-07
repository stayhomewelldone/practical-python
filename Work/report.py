# report.py
#
# Exercise 2.4
import csv
import sys
from pprint import pprint
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
def read_prices(filename):
    'Read the contents of prices, and returns a dict'
    with open(filename, 'rt') as f:
     
        rows = csv.reader(f)
        prices = {} # Initial dict
        for row in rows: 
                try:
                     prices[row[0]] = float(row[1]) 
                except ValueError:
                     print("Couldn't parse", row)
                except IndexError as e:
                     print(f'Indexerror occured on {row}: {e}')
               
        return prices
    
def calculate_current_portfolio(prices, portfolio):
     'Calculates and returns the current portfolio value'
     current_portfolio = []
     for row in portfolio:
          
               row['gain/loss'] = round(prices[row['name']] - row['price'] ,2)
               row['price'] = prices[row['name']]
               current_portfolio.append(row)


     return current_portfolio        
               

if len(sys.argv) == 2:
     filename_portfolio = sys.argv[1]
     filename_prices  = sys.argv[2]

else:
     filename = ('Data/portfolio.csv')
     filename_prices = ('Data/prices.csv')
portfolio = read_portfolio(filename)
prices = read_prices(filename_prices)
current_portfolio = calculate_current_portfolio(prices, portfolio)
pprint(f' Value of current portfolio: {current_portfolio}')
# pprint(f'Portfolio list of dict {portfolio}')
# pprint(f'Prices dict {prices}')