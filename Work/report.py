# report.py
#
# Exercise 2.4
import csv
import sys
from pprint import pprint

headers = ('Name', 'Shares', 'Price', 'Change')
def read_portfolio(filename):
    'Read the contents of a portfolio'
    with open(filename, 'rt') as f:
     
        rows = csv.reader(f)
        headers = next(rows)
        portfolio = [] # Initial, list of dicts
        for rowno, row in enumerate(rows, start=1): 
                record = dict(zip(headers,row ))
                print(record)
                try:
                     holding = {'name': record['name'],"share": int(record['shares']), 'price': float(record['price']) } 
                     portfolio.append(holding) 
                except ValueError:
                     print(f'Couldn\'t parse, {row} on line {rowno}')
                
        return portfolio
def read_prices(filename):
    'Read the contents of prices, and returns a dict'
    with open(filename, 'rt') as f:
     
        rows = csv.reader(f)
        prices = {} # Initial dict
        for rowno, row in enumerate(rows): 
                try:
                     prices[row[0]] = float(row[1]) 
                except ValueError:
                     print(f'Couldn\'t parse, {row} on line {rowno}')
                except IndexError as e:
                     print(f'Indexerror occured {row} on line: {rowno}')
               
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
def make_report(portfolio, prices):
     'To create a visually appealing table, combining data from prices.csv and portfolio.csv'
     report = [] #list of tuples     
     for entry in portfolio:
         tuple_line = (entry['name'], entry['share'],  str(round(prices[entry['name']], 2)), entry['price'] - prices[entry['name']])
         report.append(tuple_line)

     return report



if len(sys.argv) == 2:
     filename_portfolio = sys.argv[1]
     filename_prices  = sys.argv[2]

else:
     filename = ('Data/portfoliodate.csv')
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
report = make_report(portfolio, prices)

print()
# pprint(f' Value of current portfolio: {current_portfolio}')
pprint(f'Value of current portfolio: {current_value}')
pprint(f'New value of portfolio:{new_value} ')
pprint(difference)
# for r in report:
#      print('%10s %10d %10.2f %10.2f' % r)

print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
print(f'---------- ---------- ---------- -----------')
for name, shares, price, change in report:
     print(f'{name:>10s} {shares:>10d} {"$" + price:>10} {change:>10.2f}')
    
# pprint(f'Portfolio list of dict {portfolio}')
# pprint(f'Prices dict {prices}')


# Exercise 2.16 done.