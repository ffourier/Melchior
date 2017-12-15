#!/usr/local/bin/python3.6
from bs4 import BeautifulSoup
import requests
import sys
import re
import matplotlib.pyplot as plt

def plot_div_hist(ticker):
	
	##--- WEB CRAWLING ---##	
	wp = "http://www.nasdaq.com/symbol/" + ticker + "/dividend-history" # webpage to get data from
	soup = BeautifulSoup(requests.get(wp).content, "html5lib") # get webpage data
	table = soup.find('table', id = 'quotes_content_left_dividendhistoryGrid') # extract dividend table
	pd_spans = table.findAll('span', {"id" : re.compile('(.+)PayDate(.+)')}) # extract div paydates
	camt_spans = table.findAll('span', {"id" : re.compile('(.+)CashAmount(.+)')}) # extract cash amts

	##--- DATA ORGANIZATION ---##	
	paydates = [] # container for dividend paydates
	divamts = [] # container for dividend amounts
	for pd_elem, camt_elem in zip(reversed(pd_spans), reversed(camt_spans)):
		paydates.append(pd_elem.text)
		divamts.append(float(camt_elem.text))
	
	index = range(0, len(divamts))	
	
	##--- DATA VISUALIZATION ---##
	fig, ax = plt.subplots(figsize = (10, 6))
	bars = ax.bar(index, divamts, color = 'green', edgecolor = 'black', linewidth = 1.5, ls = 'solid')
	
	# Replace ticks on x-axis with paydates	
	plt.xticks(index, paydates)
		
	# Make dates on x-axis slanted	
	fig.autofmt_xdate()	

	# Add dividend amounts above the bars in the bar graph	
	for bar, div in zip(bars, divamts):
		height = bar.get_height()
		ax.text(bar.get_x() + bar.get_width() / 2, height, '%.2f' % div, ha = 'center', va = 'bottom', 
			fontweight = 'bold', color = 'black')
	
	title = 'Dividend History for ' + ticker.upper()
	plt.title(title)
	plt.xlabel('Payment Dates')
	plt.ylabel('Dividend Amounts')
	plt.show()

##--- FROM COMMAND LINE ---##
ticker = sys.argv[1].lower()

##--- CALL GRAPHING FUNCTION ---##
plot_div_hist(ticker)
