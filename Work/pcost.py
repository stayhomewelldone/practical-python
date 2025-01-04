# pcost.py
#
# Exercise 1.27

def portfolio_cost(filename):
    
    with open(filename, 'rt') as f:
        headers = next(f)
        total_cost = 0
        for line in f: 
            
                row = line.split(',')
                try: 
                    total_cost += (int(row[1]) * float(row[2]))
                except ValueError:
                     print("Couldn't parse", line)
        return round(total_cost,2)

cost = portfolio_cost('Data/portfolio.csv')

print(f'Total cost {cost}')

#Exercise 1.29 done
#Exercise 1.30 done
#Exercise 1.31 done

