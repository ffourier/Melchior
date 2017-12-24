#!/usr/local/bin/python3.6

from nltk.tokenize import sent_tokenize, word_tokenize

EXAMPLE = """"Hello Mr. Smith, how are you doing today?  The weather is great, and Python is awesome.  The sky is
	   pinkish-blue.  You shouldn't eat cardboard."""

print(word_tokenize(EXAMPLE))
print(sent_tokenize(EXAMPLE))
