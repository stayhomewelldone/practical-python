# report.py
#
# Exercise 2.4
import sys
from pprint import pprint
from fileparse import parse_csv
import stock
import tableformat

def read_portfolio(filename)->list:
     '''Read the contents of a portfolio'''
     with open(filename) as lines:
         portdicts = parse_csv(lines)
         portfolio = [ stock.Stock(d['name'], d['shares'], d['price']) for d in portdicts]
         return portfolio

def read_prices(filename)->dict:
    '''Read the contents of prices, and returns a dict'''
    prices = parse_csv(filename, types=[str, float], has_headers=False)
    return dict(prices)
    
def calculate_current_portfolio(prices, portfolio)->list:
     '''Calculates and returns the current portfolio value'''
     current_portfolio = []
     for row in portfolio:
               row['gain/loss'] = round(prices[row.name] - row.price ,2)
               row['price'] = prices[row.name]
               current_portfolio.append(row)
     return current_portfolio        
               
def current_value_portfolio( portfolio):
     '''Calculate the current value of the portfolio''' 
     current_amount = 0
     for entry in portfolio:
          current_amount += entry.shares * entry.price
     return current_amount

def new_value_portfolio(prices, portfolio):
     '''Calculate new value of portfolio based on the new prices in prices.csv'''
     new_value = 0
     for index, entry in enumerate(portfolio):
          new_value += entry.shares * prices[entry.name]

     return new_value
def make_report(portfolio, prices)->list:
     '''To create a visually appealing table, combining data from prices.csv and portfolio.csv'''
     report = [] #list of tuples     
     for index, entry in enumerate(portfolio):
         tuple_line = (entry.name, entry.shares,  round(prices[entry.name], 2), entry.price- prices[entry.name])
         report.append(tuple_line)

     return report

def print_report(report, formatter):
     '''Function for printing the report'''
     formatter.headings(['Name', 'Shares', 'Price', 'Change'])
     for name, shares, price, change in report:
          rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
          formatter.row(rowdata)

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

def portfolio_report(portfolio_filename, prices_filename, fmt='txt'):
     
     portfolio = read_portfolio(portfolio_filename)
     prices = read_prices(prices_filename)
     current_value = current_value_portfolio(portfolio)
     new_value =  new_value_portfolio(prices, portfolio)
     difference  = round(current_value - new_value, 2)
     if new_value > current_value :
          difference = f'Gain of {difference}'
     else:
          difference = f'Loss of {difference}'
     report = make_report(portfolio, prices)
     print_new_value_portfolio(current_value,new_value,difference)
     formatter = tableformat.create_formatter(fmt)
     print_report(report, formatter)

def main(argv):
    if len(argv) != 4:
        raise SystemExit(f'Usage: report.py ' 'portfile pricefile formatter')
    portfolio_report(argv[1], argv[2], argv[3])

if __name__ == '__main__':    
    import sys
    main(sys.argv)
