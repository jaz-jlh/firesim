
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

def calculateTakeHome(work_income, deduction_insurances, contribution_401k, \
	contribution_hsa, total_tax):
	# TODO ignoring inflation
	return work_income - deduction_insurances - contribution_401k - \
		contribution_hsa - total_tax



print('Year Age Income 401k Taxable TotalTax TakeHome')

for year in range(start_year, end_year):
	# Time values
	age = start_age + year - start_year
	# Income
	work_income = calculateWorkIncome(age, year)
	# returns from investments
	# Pre-tax contributions
	account_retirement_401k = calculate401k(account_retirement_401k, age)
	# hsa
	# Taxes
	taxable_income = calculateTaxableIncome(age, work_income, year)
	fica_tax = tax.ficaTax(work_income, year)
	federal_income_tax = tax.federalIncomeTax(taxable_income, tax_bracket_2018)
	state_income_tax = tax.stateIncomeTax(work_income)
	local_income_tax = tax.localIncomeTax(work_income)
	total_tax = fica_tax + federal_income_tax + state_income_tax + local_income_tax
	# Now I get paid
	take_home = calculateTakeHome(work_income, deduction_insurances, \
		contribution_401k, contribution_hsa, total_tax)

	# 

	print("%5d %5d %8.f %8.f %8.f %8.f %8.f" % 
		(year, age, work_income, account_retirement_401k, taxable_income, total_tax, take_home))