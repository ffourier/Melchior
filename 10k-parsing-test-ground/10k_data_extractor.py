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
import sys


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
		self.f10k_file_links = []

	def print_f10k_links(self):

		for link in self.f10k_file_links:
			print(link)

	
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


	def __compile_f10k_links_p1(self):
	
	
		'''Phase one of finding the links to the 10-K forms: 
		   Gets all of the form 10-K links in the company's filings table on EDGAR'''

		print("Phase one in progress...")

		url_base = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK="
		url = url_base + self._ticker + "&type=&dateb=&owner=exclude&count=100"	
			
		# While there is still another page of SEC filings to be checked ...
		while(url != ""):
			
			# Ensure compliance with SEC access guidelines	
			if (self.request_count >= 10):
				self.request_count = 0
				print("Sleeping to comply with SEC request guidelines...")
				time.sleep(1)	
			
			# Turn current SEC page into html soup
			page = requests.get(url).content			
			soup = BeautifulSoup(page, "lxml")

			self.request_count += 1
			
			# Get all table elements that have the text "10-K" or "10-K405" in them	
			f10k_elems = soup.find_all('td', text = re.compile(r"10-K\d*$"))
			
			# For each table element in f10k_elems,
			# the next table element contains the link needed
			for e in f10k_elems:
				link = self.link_base + e.find_next('a')['href']
				self.f10k_links.append(link)
			
			# Get URL to next page of SEC filings
			url = self.__EDGAR_get_next_page_url(current_soup = soup)

			# Cleanup
			soup.decompose()
		
		print("Phase one complete.")


	def __compile_f10k_links_p2(self):


		'''Phase two of finding the links to the 10-K forms:
		   Visits every link compiled in phase one, and gets the 10-K form in either
		   .html format (preferred, but not always available) or .txt format (if necessary)'''
		
		
		print("Phase two in progress...")	
		
		# Visit links compiled in phase one; then get link to
		# actual form 10-K document	
		for link in self.f10k_links:
			
			# Ensure compliance with SEC access guidelines
			if (self.request_count >= 10):
				self.request_count = 0
				print("Sleeping to comply with SEC request guidelines...")
				time.sleep(1)
			
			# Turn current page into HTML soup	
			file_list_page = requests.get(link).content	
			soup = BeautifulSoup(file_list_page, "lxml")
			
			# Increment number of SEC requests performed by 1
			self.request_count += 1
				
			# Search for the 10-K form in html format
			doc_table = soup.find("table", summary = "Document Format Files")
			rows = doc_table.find_all("tr")
			link_end = rows[1].find('a')['href']
			
			# If html-formatted 10-K form doesn't exist,
			# find the txt-formatted 10-K form (mostly for very old filings)
			if "." not in link_end:
				link_end = rows[-1].find('a')['href']
			
			# Add link to 10-K form to list for later usage
			link = self.link_base + link_end
			self.f10k_file_links.append(link)
		
		print("Phase two complete.")
	

	def __compile_net_income_data(self):

		self.__compile_f10k_links_p1()
		self.__compile_f10k_links_p2()

		raw_year_extractions = []
		raw_income_data_extractions = []
		
		years_txt_regex = re.compile(r"\s*(((19|20)\d{2})\s+){2,}")
		ni_txt_regex = re.compile(r"\s*Net (income|loss)+\s*(\(loss\))*\.*\s*(\${0,1}\s*\(*\d+,\d+\)*\s*)+")

		for link in self.f10k_file_links:
			
			# Ensure compliance with SEC access guidelines			
			if (self.request_count >= 10):
				self.request_count = 0
				time.sleep(1)

			f10k_file = requests.get(link)
			self.request_count += 1
			
			years_captured = False
			incomes_captured = False
			
			if "txt" in link: # If dealing with txt files, use regex only
				for item in f10k_file.text.split("\n"):
					if (years_captured and incomes_captured):
						break
					if not years_captured and re.match(years_txt_regex, item):
						print(item)
						years_captured = True
					if not incomes_captured and re.match(ni_txt_regex, item):
						print(item)	
						incomes_captured = True
			else: # For html files, use BeautifulSoup and regex
				print("")


	def print_net_incomes(self):
		self.__compile_net_income_data()
		print(self.net_incomes)

cmd_ticker = sys.argv[1]		
F = Form10K_Data_Extractor(cmd_ticker)
F.print_net_incomes()
