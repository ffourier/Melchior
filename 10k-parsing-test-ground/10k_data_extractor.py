#!/usr/local/bin/python3.6

"""**************************************************
*                                                   *
*                       IMPORTS                     *
*                                                   *
**************************************************"""
from bs4 import BeautifulSoup
import requests
import re ## Regular expressions
import pandas as pd


class Form10K_Data_Extractor:
	
	'''Class for extracting financial data from a company's annual report (i.e., Form 10K)'''
	
	###################################
	## Constructor
	###################################

	def __init__(self, ticker):
		self._ticker = ticker	
		self.forms = []
		self.net_incomes = []
	
	###################################
	## Private methods
	###################################

	def __EDGAR_retrieve(self):

		'''Retrieves all 10k forms from the SEC's EDGAR database'''

		webpage = "https://www.sec.gov/Archives/edgar/data/1045810/000104581017000027/nvda-2017x10k.htm"		
		soup = BeautifulSoup(requests.get(webpage).content, "html5lib")
		self.forms.append(soup)


	def __compile_net_income_data(self):
		## Assume that the 10K forms were retrieved in reverse chronological order

		self.__EDGAR_retrieve()
		
		## Regular expression for finding line with net income data on it
		ni_regex = re.compile(r"(Net income((\$(\d+,*)+)(\s|\xa0)*)+\n)")
		
		for f in self.forms:
			trs = f.findAll("tr")

			trs_text = ""
			for tr in trs:
				trs_text += tr.text + "\n"

			matches = ni_regex.findall(trs_text)
	
			ni_line = matches[0][0].replace("\xa0", " ").replace("\n", "")
			ni_data = ni_line.split("$")
			ni_data.pop(0)
			
			for i, e in enumerate(ni_data):
				if "," in e:
					e = e.replace(",", "")
				ni_data[i] = e.strip()	

			for ni in ni_data:
				self.net_incomes.append(ni)	
	
	def print_net_incomes(self):
		self.__compile_net_income_data()
		print(self.net_incomes)	

		

F = Form10K_Data_Extractor("NVDA")
F.print_net_incomes()
'''
webpage = open("nvda_2017_10k.html").read()
soup = BeautifulSoup(webpage, "html5lib")

trs = soup.findAll("tr")

trs_text = ""

for tr in trs:
	trs_text += tr.text + "\n"

ni_regex = re.compile(r"(Net income((\$(\d+,*)+)(\s|\xa0)*)+\n)")

text = open("doc.txt").read()

matches = ni_regex.findall(trs_text)

# For now, assume the correct match is the first one

ni_line = matches[0][0].replace("\xa0", " ").replace("\n", "")

ni_data = ni_line.split("$")
ni_data.pop(0)

for i, e in enumerate(ni_data):
	if "," in e:
		e = e.replace(",", "")
	ni_data[i] = e.strip()	

print(ni_data)
'''
