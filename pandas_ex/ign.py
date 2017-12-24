#!/usr/local/bin/python3.6

import pandas as pd
from pprint import pprint

reviews = pd.read_csv("ign.csv")

print(reviews.head())

print(reviews.shape)

print(reviews.iloc[0:5, 0:3])

# Print first 5 rows and all columns of the dataframe
print(reviews.iloc[:5, :])

# Print the entire dateframe
print(reviews.iloc[:,:])

# Print rows from position 5 onwards, and columns from position 5 onwards
print(reviews.iloc[5:, 5:])

# print the first column, and all of the rows for the column
print(reviews.iloc[:, 0])

# print the 10th row, and all of the columns for that row
print(reviews.iloc[9, :])

# Remove the first column from the df

reviews = reviews.iloc[:, 1:]

pprint(reviews.head())

# Display the row indexes for reviews df
print(reviews.index)

# Get row 10 to row 20 of reviews, and assign the result to some_reviews
some_reviews = reviews.iloc[10:20, :]
print(some_reviews.head())

# Error testing
print(some_reviews.loc[8:21, :])

# retrieving column by label
print(reviews.loc[:5, "score"])

# retrieving multiple columns by label
print(reviews.loc[:5, ["score", "release_year"]])

# retrieving column the easy way
print(reviews["score"])

# retrieving multiple columns the easy way
print(reviews[["score", "release_year"]])

# Get type of single column of df
print(type(reviews["score"]))

# Get type of two columns of df
print(type(reviews[["score", "release_year"]]))

# creating a series
s1 = pd.Series([1, 2])
print(s1)

# create another series
s2 = pd.Series(["Boris Yeltsin", "Mikhail Gorbachev"])
print(s2)

# create a new data frame with the above series
df = pd.DataFrame([s1, s2])
print(df)

# create a new dataframe another way
df2 = pd.DataFrame(
	[
		[1, 2],
		["Boris Yeltsin", "Mikhail Gorbachev"],
	],
	index = ["row1", "row2"],
	columns = ["column1", "column2"]
		  )

print(df2.loc["row1":"row2", "column1"])

# create df yet another way
df3 = pd.DataFrame(
	{
		"column1" : [1, "Boris Yeltsin"],
		"column2" : [2, "Mikhail Gorbachev"]
	}
)

print(df3)

# get first 5 entries of series "title"
print(reviews["title"].head())

# find the mean score
print(reviews["score"].mean())

# Print correlation matrix
print(reviews.corr())

# divide score by 2
print(reviews["score"] / 2)

# find games that got above average score
score_filter = reviews["score"] > reviews["score"].mean()
filtered_reviews = reviews[score_filter]
print(filtered_reviews.head())

# find xbox one games that got above average score
xbox_one_filter = (reviews["score"] > reviews["score"].mean()) & (reviews["platform"] == "Xbox One")
filtered_reviews = reviews[xbox_one_filter]
print(filtered_reviews.head())

# find xbox one games released in 2016 that got above average score
filter_3 = (reviews["score"] > reviews["score"].mean()) & (reviews["platform"] == "Xbox One") & (reviews["release_year"] == 2016)
filtered_reviews = reviews[filter_3]
print(filtered_reviews.head())
