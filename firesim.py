
# my stuff
import tax
from params import *

print_level = 'debug'

# initialize account values

account_savings              = initial_value_savings
account_retirement_401k      = initial_value_retirement_401k
account_retirement_taxable   = initial_value_retirement_taxable
account_roth                 = initial_value_roth
account_hsa                  = initial_value_hsa


# calculate intermediate values inside loop, publish values after each iteration

def inflation(initial_value, year):
	return ((1 + inflation_rate) ** (year - start_year))* initial_value

def calculateTaxableIncome(age, income, year):
	if age < fire_age:
		deductions = deduction_insurances + deduction_standard + \
		contribution_401k + contribution_hsa
		deductions = inflation(deductions, year)
		return income - deductions
	else:
		return 0

def calculateTakeHome(work_income, deduction_insurances, contribution_401k, \
	contribution_hsa, total_tax):
	# TODO ignoring inflation
	return work_income - deduction_insurances - contribution_401k - \
		contribution_hsa - total_tax

print('Year Age ', end='')
if print_level == 'debug':
	print('WorkIncome Taxable TotalTax TakeHome LivingExp Saveable', end='')
# elif print_level == 'intermediates':
# 	print('not implemented yet')
print(' Roth HSA Savings 401k Taxable')

for year in range(start_year, end_year):
	# Time values
	age = start_age + year - start_year

	# Growth rates happen regardless
	account_retirement_401k 	*= (1 + growth_rate_retirement_401k)
	account_retirement_taxable 	*= (1 + growth_rate_retirement_taxable)
	account_roth 				*= (1 + growth_rate_roth)
	account_hsa 				*= (1 + growth_rate_hsa)
	account_savings 			*= (1 + growth_rate_savings)

	living_expenses = inflation(initial_value_living_expenses, year)

	# the work regime
	if age < fire_age:
		# Income from working, adjusted for inflation
		work_income = inflation(initial_value_work_income, year)
		# returns from investments
		#

		# TODO 
		# Pre-tax contributions
		account_retirement_401k = account_retirement_401k + contribution_401k # add inflation
		# hsa
		account_hsa = account_hsa + contribution_hsa # add inflation

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
		# living expenses calculated above		
		saveable = take_home - living_expenses

		# Contributions
		account_savings += inflation(contribution_savings, year)




	# post-work regime
	else:
		work_income = 0
		# Retirement account distributions are not subject to the FICA tax - https://finance.zacks.com/ira-withdrawals-subject-fica-5179.html


	# TODO make this less repetitive because they are subsets
	print("%5d %5d" % (year, age), end='')
	if print_level == 'debug':
		print("%8.f %8.f %8.f %8.f %8.f %8.f" % 
			(work_income, taxable_income, total_tax, 
				take_home, living_expenses, saveable), end='')
	# elif print_level == 'intermediates':
	# 	print('not implemented yet')
	print("%8.f %8.f %8.f %8.f %8.f" % 
		(account_roth, account_hsa, account_savings, \
			account_retirement_401k, account_retirement_taxable))