# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
total_months = 0 
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    if principal < 2684.11:
        payment = principal
        break

    if total_months >= extra_payment_start_month and total_months <= extra_payment_end_month:
        principal  = principal - extra_payment
        total_paid  = total_paid + extra_payment
    
    principal = principal * (1+rate/12) - payment 

    total_months = total_months + 1
    total_paid = total_paid + payment

    print(f'{total_months} {round(total_paid, 2)} {round(principal, 2)}')
    
print(f'Total paid ${round(total_paid,2)}')
print(f'Months {total_months}')
#Exercise 1.12: A Mystery
# It returns true because it evaluates that there is an value between the parentheses. 

# Exercise 1.13 done
# Exercise 1.14 done
# symbols.replace('GOOG', ',GOOG')
# symbols =  'HPQ,' + symbols
# Exercise 1.15
# >>> 'CAT' in symbols
# False
# Why did the check for 'AA' return True?
# Because 'AA" occurs in the string. 
#Exercise 1.16 done
#Exercise 1.17 done
#Exercise 1.22 done
#symlist.append('RHT')
#symlist.insert(1, 'AA')
#symlist.remove('MSFT')
#symlist.append('YHOO')
#symlist.index('YHOO')
#Exercise 1.23 done

#Exercise 1.24 done
#Exercise 1.25
#