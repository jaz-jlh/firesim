

import tax, params



# initialize account values
account_savings              = params.initial_value_savings
account_retirement_401k      = params.initial_value_retirement_401k
account_retirement_taxable   = params.initial_value_retirement_taxable
account_roth                 = params.initial_value_roth
account_hsa                  = params.initial_value_hsa

# calculate intermediate values inside loop, publish values after each iteration






for year in range(params.start_year, params.end_year):
	print(year)