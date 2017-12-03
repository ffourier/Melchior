#!/usr/local/bin/python3.6

import sys
from termcolor import colored
import requests
from bs4 import BeautifulSoup
import re
from json import loads
from pprint import pprint

print("\n")

if (len(sys.argv) < 2):
	print("Please supply the name of the tool you would like to use. \n")
	exit()

if (sys.argv[1] == "profcalc"):
	
	comm_fee = float(input("What is the commission fee? " + colored("$ ", 'green', attrs = ['bold', 'blink'])))
	shares_bought = int(input("How many shares are you going to buy? " +
	                colored("No. of Shares: ", 'blue', attrs = ['bold', 'blink'])))	
	stock_price_bought = float(input("What is the current stock price? " +
			     colored("$ ", 'green', attrs = ['bold', 'blink'])))
	stock_price_sold = float(input("At what price are you going to sell? " +
			   colored("$ ", 'green', attrs = ['bold', 'blink'])))
	shares_sold = int(input("How many shares are you going to sell? " +
		      colored("No. of Shares: ", 'blue', attrs = ['bold', 'blink'])))

	realized_profit = (shares_sold * stock_price_sold) - (shares_sold * stock_price_bought) - 2 * comm_fee
	
	if (realized_profit < 0):
		print("Your realized profit is $ " + colored("%.2f." % realized_profit, 'red', attrs = ['bold']))
	else:
		print("Your realized profit is $ " + colored("%.2f." % realized_profit, 'green', attrs = ['bold']))

	exit()

elif (sys.argv[1] == "divincalc"):
	
	ticker = input("What is the ticker symbol of the stock you are interested in? ")	
	webpage_div = "https://finance.yahoo.com/quote/" + ticker + "/key-statistics?p=" + ticker

	soup = BeautifulSoup(requests.get(webpage_div).content, "html5lib")
	script = soup.find("script", text = re.compile("root.App.main")).text
	data = loads(re.search("root.App.main\s+=\s+(\{.*\})", script).group(1))

	stats = data["context"]["dispatcher"]["stores"]["QuoteSummaryStore"]
	share_price = stats["financialData"]["currentPrice"]["raw"]
	div_yield = stats["summaryDetail"]["dividendYield"]["raw"]

	print("The dividend yield for " + ticker + " is " + str(div_yield) + ".")
	shares = int(input("How many shares do you own? "))
	qrtly_div_inc = shares * share_price * (div_yield / 4)
	yrly_div_inc = 4 * qrtly_div_inc
	print("Your dividend income for one year will be $" + colored("%.2f" % yrly_div_inc, 'green', attrs = ['bold']) + ".")

	exit()

print("\n")
