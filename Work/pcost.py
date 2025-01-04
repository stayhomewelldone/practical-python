# pcost.py
#
# Exercise 1.27
import csv
import sys
def portfolio_cost(filename):
    
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        total_cost = 0
        for line in rows: 
            
                try: 
                    total_cost += (int(line[1]) * float(line[2]))
                except ValueError:
                     print("Couldn't parse", line)
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

