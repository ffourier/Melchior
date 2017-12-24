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
from pprint import pprint


"""**************************************************
*                                                   *
*                       CLASSES                     *
*                                                   *
**************************************************"""
class Form10K_Data_Extractor:
	
	'''Class for extracting financial data from a company's annual report (i.e., Form 10K)'''
	
	###################################
	## Constructor
	###################################

	def __init__(self, ticker):
		self._ticker = ticker	
		self.forms = []
		self.net_incomes = []
		self.f10k_links = []
	
	###################################
	## Private methods
	###################################

	def __compile_f10k_links(self):
		
		'''Creates a list of links to a company's 10K forms'''

		webpage = "https://www.sec.gov/cgi-bin/browse-edgar?CIK=NVDA&owner=exclude&action=getcompany"
		soup = BeautifulSoup(requests.get(webpage).content, "html5lib")

		table_rows = soup.findAll("tr")

		link_base = "https://www.sec.gov"

		for tr in table_rows:
			tr_children = tr.findChildren()
			for c in tr_children:
				if c.text == "10-K":
					link = link_base + c.findNext("td").findChildren()[0]['href']
					self.f10k_links.append(link)
	
	def test(self):
		self.__compile_f10k_links()
		print(self.f10k_links)

	
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
F.test()
