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
               
def current_value_portfolio( portfolio):
     'Calculate the current value of the portfolio'
     current_amount = 0
     for entry in portfolio:
          current_amount += entry['share'] * entry['price']

     return current_amount

def new_value_portfolio(prices, portfolio):
     'Calculate new value of portfolio based on the new prices in prices.csv'
     new_value = 0
     for entry in portfolio:
          new_value += entry['share'] * prices[entry['name']]

     return new_value



if len(sys.argv) == 2:
     filename_portfolio = sys.argv[1]
     filename_prices  = sys.argv[2]

else:
     filename = ('Data/portfolio.csv')
     filename_prices = ('Data/prices.csv')
portfolio = read_portfolio(filename)
prices = read_prices(filename_prices)


# current_portfolio = calculate_current_portfolio( prices, portfolio)
current_value = current_value_portfolio(portfolio=portfolio)
new_value =  new_value_portfolio(prices, portfolio)
difference  = round(current_value - new_value, 2)
if new_value > current_value :
     difference = f'Gain of {difference}'
else:
     difference = f'Loss of {difference}'
# pprint(f' Value of current portfolio: {current_portfolio}')
pprint(f'Value of current portfolio: {current_value}')
pprint(f'New value of portfolio:{new_value} ')
pprint(difference)
# pprint(f'Portfolio list of dict {portfolio}')
# pprint(f'Prices dict {prices}')