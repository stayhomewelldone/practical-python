# pcost.py
#
# Exercise 1.27
import csv
import sys
def portfolio_cost(filename):
    'Computes the total cost (shares*price) of a portfolio file'
    
    with open(filename, 'rt') as f:
     
        rows = csv.reader(f)
        headers = next(rows)
        total_cost = 0.0
        for rowno, row in enumerate(rows): 
            
                try:
                    nshares = int(row[1])
                    price = float(row[2])
                    total_cost += nshares * price
                except ValueError:
                     print(f' Row { rowno}: Bad row: {row}')
        return round(total_cost,2)
if len(sys.argv) == 2:
     filename = sys.argv[1]
else:
     filename = ('Data/portfolio.csv')
cost = portfolio_cost(filename)

print(f'Total cost {cost}')

#Exercise 1.29 done
#Exercise 1.30 done
#Exercise 1.31 done
#Exercise 1.32 done
#Exercise 1.33 done
#Exercise 2.15 done 

