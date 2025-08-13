# Level 1: Basic Input and Salary Calculation
# Objective: Capture employee details and calculate the gross salary.
# Tasks:
# • Accept the following inputs for an employee:
# o Name
# o EmpID
# o Basic Monthly Salary
# o Special Allowances (Monthly)
# o Bonus Percentage (Annual Bonus as % of Gross Salary)
# • Calculate:
# o Gross Monthly Salary = Basic Salary + Special Allowances
# o Annual Gross Salary = (Gross Monthly Salary × 12) + Bonus
# • Output:
# o Display the employee details, gross monthly salary, and annual gross salary


print('Tax calculation')

name = input('Enter your name: ')
emp_id = int(input('Enter your employee ID: '))
basic_month_salary = int(input('Enter your basic monthly salary: '))
special_allowance = int(input('Enter your special allowance: '))
bonus_percentage = float(input('Enter your bonus percentage: '))
gross_monthly_salary = basic_month_salary +  special_allowance
annual_gross_salary = ((gross_monthly_salary * 12) + bonus_percentage)
print(f'Gross salary = {gross_monthly_salary}')
print(f'Annual gross salary = {annual_gross_salary}')