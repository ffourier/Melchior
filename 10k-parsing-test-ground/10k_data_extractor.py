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
import time
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
		self.f10k_txt_links = []
	
	###################################
	## Private methods
	###################################

	def __EDGAR_get_next_page(self, current_page):
	
		'''See the next 100 results of EDGAR'''		
		
		# Number of SEC filings to show per page on EDGAR	
		count = 100
		
		# Number of first SEC filing on current page
		start = 0
		
		soup = BeautifulSoup(requests.get(current_page).content, "html5lib")	
	
		buttons = soup.findAll("input")
			
		link_base = "https://www.sec.gov"		

		next_page_link = ""
		
		for b in buttons:
			if (b['value'] == "Next 100"):
				next_page_link = b['onclick'].replace("parent.location=", "")
				next_page_link = link_base + next_page_link.replace("'", "")
				break
		
		return next_page_link
	

	def __compile_f10k_txt_links(self):
		
		## Maybe iterate in reverse, so net income data will be in chronological order?	
		
		link_base = "https://www.sec.gov"
			
		for link in self.f10k_links:
			soup = BeautifulSoup(requests.get(link).content, "html5lib")	
			
			table_cells = soup.findAll("td")
				
			next_td_contains_link = False			
	
			for td in table_cells:
				if (td.text == "Complete submission text file"):
					next_td_contains_link = True

				if (next_td_contains_link):	
					f10k_txt_link = link_base + td.findNext("td").findChildren()[0]['href']	
					self.f10k_txt_links.append(f10k_txt_link)
					break

	def __compile_f10k_links(self):
		
		'''Creates a list of links to a company's 10K forms'''
		
		link_base = "https://www.sec.gov"	
		webpage = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001045810&type=&dateb=&owner=exclude&start=0&count=100"
		
		while(webpage != ""):
			
			soup = BeautifulSoup(requests.get(webpage).content, "html5lib")

			table_rows = soup.findAll("tr")

			for tr in table_rows:
				tr_children = tr.findChildren()
				for c in tr_children:
					if c.text == "10-K":
						link = link_base + c.findNext("td").findChildren()[0]['href']
						self.f10k_links.append(link)
			
			webpage = self.__EDGAR_get_next_page(webpage)
			time.sleep(1)
		
	def test(self):
		self.__compile_f10k_links()
#		self.__compile_f10k_txt_links()
		print(self.f10k_links)

	
	def __EDGAR_retrieve(self):

		'''Retrieves all 10k forms from the SEC's EDGAR database'''
		
		self.__compile_f10k_links()	
		self.__compile_f10k_txt_links()
		
		for link in self.f10k_txt_links:	

			soup = BeautifulSoup(requests.get(link).content, "html5lib")
			self.forms.append(soup)


	def __compile_net_income_data(self):
		# Assume that the 10K forms were retrieved in reverse chronological order

		self.__EDGAR_retrieve()
		
		# Regular expression for finding line with net income data on it
		ni_regex = re.compile(r"(Net income((\$(\d+,*)+)(\s|\xa0)*)+\n)")
		
		# Iterate over all available 10-K forms and extract historical
		# net income data
		for f in self.forms:
			
			# Convert set of table rows from HTML to
			# a long string
			trs = f.findAll("tr")
			trs_text = ""
			for tr in trs:
				trs_text += tr.text + "\n"

			# Find net income data in current 10-K form (via regex)
			matches = ni_regex.findall(trs_text)
			
			# Create (clean) list of historical net income values
			# given in current 10-K form
			ni_line = matches[0][0].replace("\xa0", " ") ## DATA CLEANING: replace &nbsp with regular space
			ni_line = ni_line.replace("\n", "") ## DATA CLEANING: remove "\n"s from data
			ni_data = ni_line.split("$") ## DATA CLEANING: create list of net incomes with no $ sign
			ni_data.pop(0) ## DATA CLEANING: remove the word "Net income" from list
			
			for i, e in enumerate(ni_data): ## DATA CLEANING: remove commas and whitespace from net income values
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
