#Problem 2
#Now write a program that calculates the minimum fixed monthly payment needed in order pay
#off a credit card balance within 12 months. We will not be dealing with a minimum monthly
#payment rate.
#Take as raw_input() the following floating point numbers:
#1. the outstanding balance on the credit card
#2. annual interest rate as a decimal
#Print out the fixed minimum monthly payment, number of months (at most 12 and possibly less
#than 12) it takes to pay off the debt, and the balance (likely to be a negative number).
#Assume that the interest is compounded monthly according to the balance at the start of the
#month (before the payment for that month is made). The monthly payment must be a multiple of
#$10 and is the same for all months. Notice that it is possible for the balance to become negative
#using this payment scheme. In short:
#Monthly interest rate = Annual interest rate / 12.0
#Updated balance each month = Previous balance * (1 + Monthly interest rate) – Minimum monthly payment

#!/usr/bin/env python

# questions for user input 
principal=float(input("current outstanding balance: "))
interest=float(input("Annual interest rate (as a decimal): "))

#needed variables
monthly_int_rate=(interest/12.0)
monthly_payment=0
new_balance=principal


while new_balance > 0:

    monthly_payment += 10
    new_balance=principal
    month=0
    

   
    while month < 12 and new_balance > 0:
        
            
        month += 1

        # Interest for the month
        interest = (monthly_int_rate * new_balance)
        
        # Subtract monthly payment from outstanding balance
        new_balance -= monthly_payment

        # Add interest
        new_balance += interest

# Round final balance to 2 decimal places
new_balance = round(new_balance,2)


print("\nRESULT")
print("Monthly payment to pay off debt in 1 year: $", round(monthly_payment, 2))
print("Number of months needed: ", month)
print("Balance: $",round(new_balance, 2))
