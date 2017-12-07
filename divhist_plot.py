#!/usr/local/bin/python3.6
from bs4 import BeautifulSoup
import requests
import sys
import re
from pprint import pprint
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

## Get ticker from command line
ticker = sys.argv[1].lower()

## Webpage to get data from

wp = "http://www.nasdaq.com/symbol/" + ticker + "/dividend-history"
soup = BeautifulSoup(requests.get(wp).content, "html5lib")

table = soup.find('table', id = 'quotes_content_left_dividendhistoryGrid')

pd_spans = table.findAll('span', {"id" : re.compile('(.+)PayDate(.+)')})
camt_spans = table.findAll('span', {"id" : re.compile('(.+)CashAmount(.+)')})

div_dict = {}

for pd_elem, camt_elem in zip(pd_spans, camt_spans):
	div_dict[pd_elem.text] = float(camt_elem.text)

div_df = pd.DataFrame(list(div_dict.items()))

div_df.columns = ['Date', 'Dividend Amount']

div_df['Date'] = pd.to_datetime(div_df['Date'])

div_df = div_df.sort_values(by = 'Date', ascending = True)

div_df.plot(x = 'Date', y = 'Dividend Amount', style = 'o')

plt.show()
