#!/usr/local/bin/python3.6

##################################################################
#								 #
# Filename:  get_quote.py					 #
#								 #
# Purpose:  Get the current price of a stock			 #
#								 #
# Author:  Nolan R. H. Gagnon					 #
#								 #
# Date: Dec. 03, 2017                                            #
#								 #
##################################################################

## IMPORTS -----------------------------------------------------##
from termcolor import colored
import sys
import  requests
from bs4 import BeautifulSoup
import re
from json import loads
from pprint import pprint

def str_to_int(string):
	t = string.replace(',', '')
	return int(t)

## Check for proper usage of script
if len(sys.argv) > 2:
	print("Please supply only the ticker symbol.  Example usage: ./get_quote NVDA")
	exit()

## Build URL for requested stock's page on Yahoo Finance
webpage = "https://finance.yahoo.com/quote/" + sys.argv[1] + "?p=" + sys.argv[1]

## Get JSON data from webpage
soup = BeautifulSoup(requests.get(webpage).content, "html5lib")
script = soup.find("script",text=re.compile("root.App.main")).text
data = loads(re.search("root.App.main\s+=\s+(\{.*\})", script).group(1))

quote = data["context"]["dispatcher"]["stores"]["QuoteSummaryStore"]["financialData"]["currentPrice"]["raw"]

## Get company health metrics
bs_page = "https://finance.yahoo.com/quote/" + sys.argv[1] + "/balance-sheet?p=" + sys.argv[1]
soup = BeautifulSoup(requests.get(bs_page).content, "html5lib")
script = soup.find("script", text = re.compile("root.App.main")).text
bs_data = loads(re.search("root.App.main\s+=\s+(\{.*\})", script).group(1))

bs = bs_data["context"]["dispatcher"]["stores"]["QuoteSummaryStore"]["balanceSheetHistoryQuarterly"]["balanceSheetStatements"]

## Calculate the company's current ratio (measure of ability to handle short-term debt)
tot_curr_assets = str_to_int(bs[0]['totalCurrentAssets']['longFmt'])
tot_curr_liabs = str_to_int(bs[0]['totalCurrentLiabilities']['longFmt'])

current_ratio = (tot_curr_assets * 1.0) / tot_curr_liabs

## Calculate the company's debt-to-equity ratio (how much leverage is the company using?)
tot_liab = bs[0]['totalLiab']['raw']  # total liabilities (mrq)
equity = bs[0]['totalStockholderEquity']['raw']

de_ratio = (tot_liab * 1.0) / equity


print("\n\n")
print(40*"-" + " |" + colored(sys.argv[1], attrs = ['bold']) + "| " + 40*"-" + "\n")
print("Current Price: " + colored(quote, 'green', attrs=['bold']))
print("\n")

print(colored("Debt Metrics", attrs = ['bold']))

if (de_ratio < 1.00):
	print("Debt-to-equity Ratio: " + colored("%.2f" % de_ratio, 'green', attrs = ['bold']))
else:
	print("Debt-to-equity Ratio: " + colored("%.2f" % de_ratio, 'red', attrs = ['bold']))	

if current_ratio > 1.00:
	print("Current Ratio: " + colored("%.2f" % current_ratio, 'green', attrs = ['bold']))
else:
	print("Current Ratio: " + colored("%.2f" % current_ratio, 'red', attrs = ['bold']))

print("\n\n")
