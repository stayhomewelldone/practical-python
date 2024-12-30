# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
total_months = 0 
extra_payment = 1000

while principal > 0:
    if total_months < 12:
        principal  = principal - extra_payment
        total_paid  = total_paid + extra_payment
    principal = principal * (1+rate/12) - payment 

    total_months = total_months + 1
    total_paid = total_paid + payment

print('Total paid', round(total_paid,2))
print("Total months", total_months)