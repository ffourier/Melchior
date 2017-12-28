#!/usr/local/bin/python3.6

from finscraper import *
import sys

cmd_ticker = sys.argv[1]
F = Form10K_Data_Extractor(cmd_ticker)
F.print_net_incomes()
