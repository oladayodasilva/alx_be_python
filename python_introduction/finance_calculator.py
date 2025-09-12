monthly_income = int(input("enter your monthly income:"))
monthly_expenses = int(input("enter your total monthly expenses:"))

#calculation of monthly savings by subtracting monthly expenses from income
monthly_savings = monthly_income - monthly_expenses

#project annual savings
simple_annual_interest_rate = 0.05

#Projected savings after 1 year
#Formula: (Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05))

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")
