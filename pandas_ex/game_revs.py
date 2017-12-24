#!/usr/local/bin/python3.6

import pandas as pd
from pprint import pprint
import matplotlib.pyplot as plt

reviews = pd.read_csv("ign.csv")

# find xbox one games released in 2016 that got above average score
##filter_3 = (reviews["score"] > reviews["score"].mean()) & (reviews["platform"] == "Xbox One") & (reviews["release_year"] == 2016)
##filtered_reviews = reviews[filter_3]
##print(filtered_reviews.head())

# find all xbox one games rated as "Masterpiece"
#filter_4 = (reviews["platform"] == "Xbox One") & (reviews["score_phrase"] == "Masterpiece")
#filtered_reviews = reviews[filter_4]
#print(filtered_reviews)

# Plot histogram for Xbox One scores and histogram for PS4 scores
fig, (ax1, ax2) = plt.subplots(nrows = 2, ncols = 1)

ax1 = reviews[reviews["platform"] == "Xbox One"]["score"].plot(kind = "hist", edgecolor = 'black')

ax2 = reviews[reviews["platform"] == "PlayStation 4"]["score"].plot(kind = "hist", edgecolor = 'black')

plt.show()
