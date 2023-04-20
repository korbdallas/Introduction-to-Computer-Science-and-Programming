#Problem Set 1
#Handed out: Lecture 2.
#Due: 11:59pm, Lecture 4.
#Name: Michael Colombo
#
#Introduction
#This problem set will introduce you to using control flow in Python and formulating a
#computational solution to a problem. You will design and write three simple Python programs,
#test them, and hand them in. Be sure to read this problem set thoroughly.
#Paying Off Credit Card Debt
#Each month, a credit card statement will come with the option for you to pay a minimum amount
#of your charge, usually 2% of the balance due. However, the credit card company earns money
#by charging interest on the balance that you don’t pay. So even if you pay credit card payments
#on time, interest is still accruing on the outstanding balance.
#Say you’ve made a $5,000 purchase on a credit card with 18% annual interest rate and 2%
#minimum monthly payment rate. After a year, how much is the remaining balance? Use the
#following equations.
#
#Minimum monthly payment = Minimum monthly payment rate x Balance
#(Minimum monthly payment gets split into interest paid and principal paid)
#Interest Paid = Annual interest rate / 12 months x Balance
#Principal paid = Minimum monthly payment – Interest paid
#Remaining balance = Balance – Principal paid
#
#For month 1, we can compute the minimum monthly payment by taking 2% of the balance:
#
#Minimum monthly payment = .02 x $5000.0 = $100.0
#
#We can’t simply deduct this from the balance because there is compounding interest. Of this
#$100 monthly payment, compute how much will go to paying off interest and how much will go
#to paying off the principal. Remember that it’s the annual interest rate that is given, so we need
#to divide it by 12 to get the monthly interest rate.
#
#Interest paid = .18/12.0 x $5000.0 = $75.0
#Principal paid = $100.0 – $75.0 = $25
#
#The remaining balance at the end of the first month will be the principal paid this month
#subtracted from the balance at the start of the month.
#
#Remaining balance = $5000.0 – $25.0 = $4975.0
#
#For month 2, we repeat the same steps:
#
#Minimum monthly payment = .02 x $4975.0 = $99.50
#Interest Paid = .18/12.0 x $4975.0 = $74.63
#Principal Paid = $99.50 – $74.63 = $24.87
#Remaining Balance = $4975.0 – $24.87 = $4950.13
#After 12 months, the total amount paid is $1167.55, leaving an outstanding balance of $4708.10.
#Pretty depressing!
#
#Paying the Minimum
#Problem 1
#Write a program to calculate the credit card balance after one year if a person only pays the
#minimum monthly payment required by the credit card company each month.
#Use raw_input() to ask for the following three floating point numbers:
#1. the outstanding balance on the credit card
#2. annual interest rate
#3. minimum monthly payment rate
#For each month, print the minimum monthly payment, remaining balance, principle paid in the
#format shown in the test cases below. All numbers should be rounded to the nearest penny.
#Finally, print the result, which should include the total amount paid that year and the remaining
#balance.
#
#Hints
#Use the round function.
#To help you get started, here is a rough outline of the stages you should probably follow in
#writing your code:
#• Retrieve user input.
#• Initialize some state variables. Remember to find the monthly interest rate from the
#annual interest rate taken in as input.
#• For each month:
#o Compute the new balance. This requires computing the minimum monthly
#payment and figuring out how much will be paid to interest and how much will be
#paid to the principal.
#o Update the outstanding balance according to how much principal was paid off.
#o Output the minimum monthly payment and the remaining balance.
#o Keep track of the total amount of paid over all the past months so far.
#• Print out the result statement with the total amount paid and the remaining balance.
#Use these ideas to guide the creation of your code
#
#!/usr/bin/env python

# questions for user input 
principle=float(input("current outstanding balance: "))
interest=float(input("Annual interest rate (as a decimal): "))
minimum=float(input("minimum monthly payment (as a deimal): "))

#needed variables 
total_paid=float(0)
month=1

while(month <= 12):

   print("\nmonth", month)
   month += 1

   min_payment=(minimum*principle)
   print("Minimum monthly payment: $",round(min_payment, 2))
   total_paid += min_payment

   int_paid=((interest/12)*principle)

   principle_paid=(min_payment-int_paid)
   print("Principle paid: $",round(principle_paid, 2))

   remaining_balance=(principle-principle_paid)
   print("Remaining Balance: $",round(remaining_balance, 2))
   principle=remaining_balance
   

print("\nRESULT")
print("Total amount paid: $",round(total_paid, 2)) 
print("Remaining Balance: $",round(remaining_balance, 2))
