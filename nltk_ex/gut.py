#!/usr/local/bin/python3.6
from nltk.tokenize import sent_tokenize, PunktSentenceTokenizer
from nltk.corpus import genesis

sample = genesis.raw("lolcat.txt")

tok = sent_tokenize(sample)

for x in range(10):
	print(tok[x])
