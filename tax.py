
def incomeTax(taxable_income, tax_bracket):
	tax_burden = 0
	for index in range(len(tax_bracket)):
		bracket = tax_bracket[index]
		if taxable_income > bracket[0]:
			tax_burden += (bracket[0] - tax_bracket[index - 1][0])* bracket[1]
		else:
			tax_burden += (taxable_income - tax_bracket[index - 1][0]) * bracket[1]
			break
	return tax_burden

def effectiveTaxRate(taxable_income, tax_burden):
	return (tax_burden / taxable_income) * 100.0