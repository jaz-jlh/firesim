
# my stuff
import tax
from params import *

# account_savings = 
# account_retirement_401k = 
# account_retirement_taxable = 
# account_roth = 
# account_hsa = 

# initialize account values

account_savings              = initial_value_savings
account_retirement_401k      = initial_value_retirement_401k
account_retirement_taxable   = initial_value_retirement_taxable
account_roth                 = initial_value_roth
account_hsa                  = initial_value_hsa


# calculate intermediate values inside loop, publish values after each iteration

def inflation(initial_value, year):
	return ((1 + inflation_rate) ** (year - start_year))* initial_value

def calculateWorkIncome(age, year):
	income = 0
	if age < fire_age:
		# income comes from work here
		income = inflation(initial_value_work_income, year)
	return income


def calculateTaxableIncome(age, income, year):
	if age < fire_age:
		deductions = deduction_insurances + deduction_standard + \
		contribution_401k + contribution_hsa
		deductions = inflation(deductions, year)
		return income - deductions
	else:
		return 0

def calculate401k(current_value, age):
	if age < fire_age:
		return current_value + contribution_401k
	else: 
		return current_value



print('Year Age Income Taxable 401k')

for year in range(start_year, end_year):
	age = start_age + year - start_year
	work_income = calculateWorkIncome(age, year)
	taxable_income = calculateTaxableIncome(age, work_income, year)
	account_retirement_401k = calculate401k(account_retirement_401k, age)

	print("%5d %5d %8.f %8.f %8.f" % 
		(year, age, work_income, taxable_income, account_retirement_401k))