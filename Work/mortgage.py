# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
init_payment = 2684.11
total_paid = 0.0
num_month = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    num_month = num_month + 1
    if num_month >= extra_payment_start_month and num_month <= extra_payment_end_month:
        payment = init_payment + extra_payment
    else:        
        payment = init_payment

    principal = principal * (1 + rate/12) - payment
    total_paid = total_paid + payment        
    #print(num_month, round(total_paid, ndigits=2), round(principal, ndigits=2))
    print(f'{num_month:5} {round(total_paid, ndigits=2):10.2f} {round(principal, ndigits=2):10.2f}')

print(f'Total paid: {round(total_paid + principal, ndigits=1):0.2f}')
print(f'    Months: {num_month}')
