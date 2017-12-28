#!/usr/local/bin/python3.6

from finscraper import *
from finplotter import *
import sys

cmd_ticker = sys.argv[1]
F = Form10K_Data_Extractor(cmd_ticker)
F.print_net_incomes()

ni_df = F.get_net_income_df() 

print(ni_df)

NI_bar_plot(cmd_ticker, ni_df, w_regline = False, n_predyrs = 10)
