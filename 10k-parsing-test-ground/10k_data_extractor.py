#!/usr/local/bin/python3.6

"""**************************************************
*                                                   *
*                       IMPORTS                     *
*                                                   *
**************************************************"""
from bs4 import BeautifulSoup
import requests
import re 
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
		self.request_count = 0
		self.link_base = "https://www.sec.gov"
		self._ticker = ticker	
		self.forms = []
		self.net_incomes = []
		self.f10k_links = []
		self.f10k_txt_links = []

	
	###################################
	## Private methods
	###################################

	def __EDGAR_get_next_page_url(self, current_soup):

	
		'''Navigate to the next page of EDGAR search results'''		

	
		# Find the html object that contains the link to the next page of SEC filings 
		next_page_buttons = current_soup.find_all(value = re.compile(r"Next \d+"))	
		
		# If we are on the last page of filings, return the empty string to caller	
		if (len(next_page_buttons) == 0):
			next_page_link = ""	
		else: # Else build link to the next page of filings	
			onclick_content = next_page_buttons[0]['onclick']	
			next_page_link = self.link_base + onclick_content.replace("parent.location=", "").replace("'", "")
	
		# Return link to caller	
		return next_page_link


	#def __compile_f10k_links(self):


	#	'''Puts links to the 10-K forms into a single list'''

	#	
	#	# Iterate in reverse, so net income data will be in chronological order
	#	for link in list(reversed(self.f10k_links)):
	#		soup = BeautifulSoup(requests.get(link).content, "html5lib")	
	#		
	#		table_cells = soup.findAll("td")
	#			
	#		next_td_contains_link = False			
	#
	#		for td in table_cells:
	#			if (td.text == "Complete submission text file"):
	#				next_td_contains_link = True

	#			if (next_td_contains_link):	
	#				f10k_txt_link = self.link_base + td.findNext("td").findChildren()[0]['href']	
	#				self.f10k_txt_links.append(f10k_txt_link)
	#				break
	#		time.sleep(1)

	def __compile_f10k_links(self):
	
	
		'''Creates a list of links to a company's 10-K forms'''

		
		url = "https://www.sec.gov/cgi-bin/browse-edgar?CIK=" + self._ticker + "&owner=exclude&action=getcompany&Find=Search"
		
		while(url != ""):
			
			# Ensure compliance with SEC access guidelines	
			if (self.request_count == 10):
				self.request_count = 0
				print("Sleeping...")
				time.sleep(1)	
			
			# Turn current SEC page into html soup
			page = requests.get(url).content			
			soup = BeautifulSoup(page, "lxml")

			self.request_count += 1
			
			f10k_elems = soup.find_all('td', text = re.compile(r"10-K\d*"))
			
			for e in f10k_elems:
				link = self.link_base + e.find_next('a')['href']
				self.f10k_links.append(link)
			
			# Get URL to next page of SEC filings
			url = self.__EDGAR_get_next_page_url(current_soup = soup)

			# Cleanup
			soup.decompose()
		
	def test(self):
		self.__compile_f10k_links()
		print(self.f10k_links)
		print(self.request_count)

	
	def __EDGAR_retrieve(self):

		'''Retrieves all 10k forms from the SEC's EDGAR database'''
		
#		self.__compile_f10k_links()	
#		self.__compile_f10k_txt_links()
#		
#		for link in self.f10k_txt_links:	
#
#			soup = BeautifulSoup(requests.get(link).content, "html5lib")
#			self.forms.append(soup)
		# ANK
		test = "https://www.sec.gov/Archives/edgar/data/1045810/000104581017000027/0001045810-17-000027.txt"
		webfile = requests.get(test).content
		pprint(webfile)
#		soup = BeautifulSoup(webfile, "html5lib")
#		
#		tds = soup.findAll("td")
#
#		for td in tds:
#			print(td)

#		self.forms.append(soup)


	def __compile_net_income_data(self):
		# Assume that the 10K forms were retrieved in reverse chronological order

		self.__EDGAR_retrieve()
		
#		# Regular expression for finding line with net income data on it
#		ni_regex = re.compile(r"(Net income((\$(\d+,*)+)(\s|\xa0)*)+\n)")
#		
#		# Iterate over all available 10-K forms and extract historical
#		# net income data
#		for f in self.forms:
#			
#			# Convert set of table rows from HTML to
#			# a long string
#			trs = f.findAll("tr")
#			trs_text = ""
#			for tr in trs:
#				trs_text += tr.text + "\n"
#
#			## Find net income data in current 10-K form (via regex)
#			matches = ni_regex.findall(trs_text)
#			
#			## Create (clean) list of historical net income values
#			## given in current 10-K form
#			ni_line = matches[0][0].replace("\xa0", " ") ## DATA CLEANING: replace &nbsp with regular space
#			ni_line = ni_line.replace("\n", "") ## DATA CLEANING: remove "\n"s from data
#			ni_data = ni_line.split("$") ## DATA CLEANING: create list of net incomes with no $ sign
#			ni_data.pop(0) ## DATA CLEANING: remove the word "Net income" from list
#			
#			for i, e in enumerate(ni_data): ## DATA CLEANING: remove commas and whitespace from net income values
#				if "," in e:
#					e = e.replace(",", "")
#				ni_data[i] = e.strip()	
#
#			for ni in ni_data:
#				self.net_incomes.append(ni)	
	
	def print_net_incomes(self):
		self.__compile_net_income_data()
		print(self.net_incomes)

		
F = Form10K_Data_Extractor("JNJ")
F.test()
