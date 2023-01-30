import numpy as np
import pandas as pd

# specify which variables should be preserved in new financial info file
var_list = ['sa_finance1_cocode', 'sa_finance1_year', 'sa_ann_rep_months','sa_total_assets', 'sa_export_earnings', 'sa_bd_return_on_ast', 'sa_net_ppe', 'sa_op_cash_flow_before_wkcap_cha', 'sa_debt', 'sa_borrowings']


# read in prowess financial report information csv, preserving only variables of interest, write out to intermediate file

print('loading in financial info...')
df = pd.read_csv(r'/new_data/eloise_testing/fin_data_cleaning/prowess_financial.csv', usecols = var_list)
df.to_csv(r'/new_data/eloise_testing/fin_data_cleaning/prowess_financial_intermed2.csv')
print('financial data loaded into intermediate file')


# read in df with only vars of interest
print('intermediate file loaded')
df2 = pd.read_csv(r'/new_data/eloise_testing/fin_data_cleaning/prowess_financial_intermed2.csv')


# generate new variable year from sa_finance1_year
df2['year'] = df2.sa_finance1_year.str.slice(0,4)
 

# write out final file which contains only the necessary information

df2.to_csv(r'/new_data/eloise_testing/fin_data_cleaning/prowess_financial_clean.csv')
