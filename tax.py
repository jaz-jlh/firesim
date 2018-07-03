from params import *

def federalIncomeTax(taxable_income, tax_bracket):
	tax_burden = 0
	for index in range(len(tax_bracket)):
		bracket = tax_bracket[index]
		if taxable_income > bracket[0]:
			tax_burden += (bracket[0] - tax_bracket[index - 1][0])* bracket[1]
		else:
			tax_burden += (taxable_income - tax_bracket[index - 1][0]) * bracket[1]
			break
	return tax_burden

def capitalGainsTax(year, taxable_income, short_term_gains, 
	long_term_gains, capital_gains_tax_bracket):
	short_term_burden = 0
	long_term_burden = 0
	# TODO currently ignoring the net investment income tax (applies to income over 200k for single)
	total_income = taxable_income + short_term_gains + long_term_gains
	# this for loop is reversed so that we only have to compare 1 income value
	for tax_bracket in reversed(capital_gains_tax_bracket):
		if total_income > tax_bracket[0]:
			short_term_burden = short_term_gains * tax_bracket[1]
			long_term_burden = long_term_gains * tax_bracket[2]
			return short_term_burden, long_term_burden

def ficaTax(total_income, year):
	# for now we'll just say the fica tax is a flat 7.65% because that's typically the case
	return total_income * 0.0765 
	#TODO implement this properly
	# fica does not apply to HSA contributions - https://www.investopedia.com/articles/personal-finance/091615/how-use-your-hsa-retirement.asp
	# 
	# Social Security tax responsibility: 6.2% each for you and employer up to $127,200 in wages.
	# Medicare tax responsibility: 1.45% each for you and your employer (with no income limit).
	# Medicare surcharge tax: 0.9% just for the employee on wages over $200,000.
	# from https://www.fool.com/retirement/2017/01/28/what-is-the-fica-tax-and-why-do-i-have-to-pay-it.aspx

def stateIncomeTax(total_income):
	return total_income * tax_rate_state

def localIncomeTax(total_income):
	return total_income * tax_rate_local

def effectiveTaxRate(total_income, tax_burden):
	return (tax_burden / total_income) * 100.0