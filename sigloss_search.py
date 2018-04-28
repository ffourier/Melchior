################################################
## FILENAME: sigloss_search.py	 	       #
## PURPOSE: Search for stocks that have lost   #
##          significant value over a specified #
##          period of time.	               #
## AUTHOR: nolanHg                             #
## DATE: 04/27/2018			       #
################################################

## IMPORTS ##
from termcolor import colored
import sys
import requests
from bs4 import BeautifulSoup
import re
from json import loads
from pprint import pprint
import datetime

## FUNCTIONS ##
def page_to_soup(url):
	return BeautifulSoup(requests.get(url).content, "html5lib")

def soup_to_json(soup):
	script = soup.find("script",text=re.compile("root.App.main")).text
	data = loads(re.search("root.App.main\s+=\s+(\{.*\})", script).group(1))
	return data

def get_nasdaq_tickers():
	tickers = []
	
	for j in range(0, 26):
		print("Downloading tickers starting with the letter " + chr(65 + j) + "...")
		data_src_page = "http://eoddata.com/stocklist/NASDAQ/" + chr(65 + j) + ".htm"
		soup = page_to_soup(data_src_page)		
		qtab = soup.find("table", {"class" : "quotes"})
		qtab_rows = qtab.find_all("tr")
		
		for k in range(1, len(qtab_rows)):
			tickers.append(qtab_rows[k].find('a').text)
		
	return tickers

def display_LG(tlist, date, pct_thresh, mode):
	for ticker in tlist:
		quote_src_page = "https://finance.yahoo.com/quote/" + ticker + "?p=" + ticker
		soup = page_to_soup(quote_src_page)
		try:
			data = soup_to_json(soup)

			try:
				hist_quote = get_historical_quote(ticker, date)
				quote = data["context"]["dispatcher"]["stores"]["QuoteSummaryStore"]["price"]["regularMarketPrice"]["raw"]
				
				if (hist_quote is None):
					print(ticker + ":")
					print("Price on " + date + ": No data available")
					print("Current price: " + str(quote))
					print("\n")
				else:	
					if (mode == "loss"):	
						if (hist_quote > quote):
							pct_loss = -100 * ((1.0 * abs(quote - hist_quote)) / hist_quote)
							if abs(pct_loss) > threshold:
								print(ticker + ":")
								print("Price on " + date + ": " + str(hist_quote))
								print("Current price: " + str(quote))
								print("Percentage loss: " + colored("%.2f" % pct_loss, 'red', attrs = ['bold']))
								print("\n")
					else:
						if (hist_quote < quote):
							pct_gain = 100 * ((1.0 * abs(quote - hist_quote)) / hist_quote)
							if abs(pct_gain) > threshold:
								print(ticker + ":")
								print("Price on " + date + ": " + str(hist_quote))
								print("Current price: " + str(quote))
								print("Percentage gain: " + colored("%.2f" % pct_gain, 'green', attrs = ['bold']))
								print("\n")

			except KeyError:
				print("Key Error: " + ticker)

		except AttributeError:
			print("Download Error: " + ticker)	

def get_historical_quote(ticker, date):
	date_list = date.split("/")
	month = int(date_list[0])
	day = int(date_list[1])
	year = int(date_list[2])
	
	unix_timestamp = int(datetime.datetime(year, month, day, 0, 0, 0).timestamp())
	hist_quote_src_page = "https://finance.yahoo.com/quote/" + ticker + \
			      "/history?period1=" + str(unix_timestamp) + "&period2=" + str(unix_timestamp) + \
			      "&interval=1d&filter=history&frequency=1d"

	soup = page_to_soup(hist_quote_src_page)
	qtab = soup.find("table")
	rows = qtab.find_all("tr")
	tds = rows[1].find_all("td")
	try:
		hist_quote = float(tds[4].text.replace(',', ''))

	except IndexError:
		return None
	
	return hist_quote 

if (len(sys.argv) != 4):
	print("USAGE: python3 sigloss_search <date> <pct threshold> <mode>")
	exit()

historical_date = sys.argv[1]	
threshold = float(sys.argv[2])
mode = sys.argv[3]
tickers = get_nasdaq_tickers()
display_LG(tickers, historical_date, threshold, mode)
