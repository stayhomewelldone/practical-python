# report.py
#
# Exercise 2.4
import csv
import sys
from pprint import pprint
from fileparse import parse_csv

def read_portfolio(filename)->list:
     '''Read the contents of a portfolio'''
     portfolio = parse_csv(filename)
     return portfolio

#     with open(filename, 'rt') as f:
     
#         rows = csv.reader(f)
#         headers = next(rows)
#         portfolio = [] # Initial, list of dicts
#         for rowno, row in enumerate(rows, start=1): 
#                 record = dict(zip(headers,row ))
#                 try:
#                      holding = {'name': record['name'],"share": int(record['shares']), 'price': float(record['price']) } 
#                      portfolio.append(holding) 
#                 except ValueError:
#                      print(f'Couldn\'t parse, {row} on line {rowno}')
def read_prices(filename)->dict:
    'Read the contents of prices, and returns a dict'
    prices = parse_csv(filename, types=[str, float], has_headers=False)
    return prices

#     with open(filename, 'rt') as f:
     
#         rows = csv.reader(f)
#         prices = {} # Initial dict
#         for rowno, row in enumerate(rows): 
#                 try:
#                      prices[row[0]] = float(row[1]) 
#                 except ValueError:
#                      print(f'Couldn\'t parse, {row} on line {rowno}')
#                 except IndexError as e:
#                      print(f'Indexerror occured {row} on line: {rowno}')
               
    
def calculate_current_portfolio(prices, portfolio)->list:
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
          current_amount += entry['shares'] * entry['price']

     return current_amount

def new_value_portfolio(prices, portfolio):
     'Calculate new value of portfolio based on the new prices in prices.csv'
     new_value = 0
     for index, entry in enumerate(portfolio):
          new_value += entry['shares'] * prices[index][1]

     return new_value
def make_report(portfolio, prices)->list:
     'To create a visually appealing table, combining data from prices.csv and portfolio.csv'
     report = [] #list of tuples     
     for index, entry in enumerate(portfolio):
         tuple_line = (entry['name'], entry['shares'],  str(round(prices[index][1], 2)), entry['price'] - prices[index][1])
         report.append(tuple_line)

     return report

def print_report(report):
     '''Function for printing the report'''
     headers = ('Name', 'Shares', 'Price', 'Change')
     print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
     print(('-' * 10 + ' ') * len(headers))
     for name, shares, price, change in report:
          print(f'{name:>10s} {shares:>10d} {"$" + price:>10} {change:>10.2f}')

def handle_args()->str:
     '''Handle the args passed by executing of the script.'''
     if len(sys.argv) == 2:
          filename = sys.argv[1]
          filename_prices  = sys.argv[2]

     else:
          filename = ('Data/portfolio.csv')
          filename_prices = ('Data/prices.csv')
     
     return filename, filename_prices
def print_new_value_portfolio(current_value,new_value,difference):
     pprint(f'Value of current portfolio: {current_value}')
     pprint(f'New value of portfolio:{new_value} ')
     pprint(difference)

def portfolio_report(portfolio_filename, prices_filename):
     
     # filename, filename_prices = handle_args()
     portfolio = read_portfolio(portfolio_filename)
     prices = read_prices(prices_filename)


     # current_portfolio = calculate_current_portfolio( prices, portfolio)
     current_value = current_value_portfolio(portfolio=portfolio)
     new_value =  new_value_portfolio(prices, portfolio)
     difference  = round(current_value - new_value, 2)
     if new_value > current_value :
          difference = f'Gain of {difference}'
     else:
          difference = f'Loss of {difference}'
     report = make_report(portfolio, prices)
     print_new_value_portfolio(current_value,new_value,difference)
     print_report(report)

def main(argv):
    portfolio_report(argv[1], argv[2])
    
if __name__ == '__main__':
    import sys
    main(sys.argv)
# pprint(f' Value of current portfolio: {current_portfolio}')

# for r in report:
#      print('%10s %10d %10.2f %10.2f' % r)


# pprint(f'Portfolio list of dict {portfolio}')
# pprint(f'Prices dict {prices}')


# Exercise 2.16 done.