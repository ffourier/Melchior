#!/usr/local/bin/python3.6

'''IMPORTS'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd
import sys
from pprint import pprint

'''FUNCTIONS'''
## Get the sample mean of a set of data
def get_mean(x):
	
	# Number of data points in x
	n = len(x)
	
	# Sum of data points (dp) in x
	sum_dp = 0
	for dp in x:
		sum_dp += dp
	
	# Calculate the mean
	m = (sum_dp * 1.0) / n
	
	# Return mean to caller	
	return m

## Get the sample standard deviation of a set of data
def get_sd(x):
	
	# Number of data points in x
	n = len(x)
	
	# Calculate the sample mean of data set x
	m = get_mean(x)
	
	# Sum of squared deviations from the mean	
	sum_sqr_dev = 0
	for dp in x:
		sum_sqr_dev += (dp - m) ** 2

	# Calculate sample variance 
	s_var = (sum_sqr_dev * 1.) / (n - 1)
	
	# Calculate sample standard deviation
	s_sd = s_var ** 0.5	

	# Return sample standard deviation to caller
	return s_sd

## Get sample correlation coefficient
def get_corr_coeff(x, y):
	
	# Number of data points	(x, y)
	n = len(x)
	
	# Sum of data points in x, sum of squared data points in x
	sum_x = 0
	sum_sqr_x = 0
	for dp in x:
		sum_x += dp
		sum_sqr_x += dp ** 2
	
	# Sum of data points in y, sum of squared data points in y
	sum_y = 0
	sum_sqr_y = 0
	for dp in y:
		sum_y += dp
		sum_sqr_y += dp ** 2

	# Calculate dot product of x and y
	dot_prod = 0
	for dp_x, dp_y in zip(x, y):
		dot_prod += dp_x * dp_y

	# Calculate sample correlation coefficient	
	r_num = (n * dot_prod) - (sum_x * sum_y)
	r_den = ((n * sum_sqr_x - sum_x ** 2) * (n * sum_sqr_y - sum_y ** 2)) ** 0.5
	r = r_num / r_den
	
	# Return sample correlation coefficient to caller
	return r
		
## Plot linear regression line for data
def plot_lin_reg(x, y, ax, n_pred, x_for_pred):
	
	# Calculate slope of regression line
	r = get_corr_coeff(x, y)	
	sd_x = get_sd(x)
	sd_y = get_sd(y)
	
	slope = r * (sd_y / sd_x)

	# Calculate y-intercept of regression line
	x_bar = get_mean(x)
	y_bar = get_mean(y)	
	y_intercept = y_bar - slope * x_bar

	# Plot regression line on ax (set of axes passed to function)
	X = np.linspace(x[0], x[-1] + n_pred + 1, 100)
	Y = y_intercept + slope * X
	ax.plot(X, Y, color = 'black', linestyle = 'solid')

	# Return list of predictions
	return list(y_intercept + slope * d for d in x_for_pred)

'''DATA'''
## Get path to csv file containing net income data and read file into dataframe
csv_file = sys.argv[2]
ni_df = pd.read_csv(csv_file).sort_values('year')

years = list(ni_df["year"])
net_incomes = list(ni_df["net_income"])


'''DATA VISUALIZATION'''
## Create a figure and set of axes for plotting data
FIG_WIDTH = 12
FIG_HEIGHT = 6
fig, ax = plt.subplots(figsize = (FIG_WIDTH, FIG_HEIGHT))

## Create bar plot of net income data
bars = ax.bar(years, net_incomes, color = 'green')

## Create bar plot for the predicted net incomes
extended_years = range(max(years) + 1, max(years) + 11)
pred_net_incomes = plot_lin_reg(years, net_incomes, ax, 10, extended_years)
extended_bars = ax.bar(extended_years, pred_net_incomes, color = 'gray') 

## Add net income amounts above bars in bar graph
for bar, ni in zip(bars + extended_bars, net_incomes + pred_net_incomes):
	bh = bar.get_height()
	if (bh < 0):
		bar.set_color('salmon') # Make bars corresponding to negative net incomes red
		text_height = bh - 80
	else:
		text_height = bh + 40

	ax.text(bar.get_x() + bar.get_width() / 2, text_height, '%d' % ni, ha = 'center', va = 'bottom',
		fontweight = 'bold', color = 'black', fontsize = 6)

## Add text to describe predicted net income growth
ax.text(extended_bars[0].get_x() + extended_bars[0].get_width() / 2, -150,
	'%.2f %% growth' % (100 * ((extended_bars[1].get_height() - extended_bars[0].get_height()) / extended_bars[0].get_height())),
	fontweight = 'bold', fontsize = 14)

## Create legend for plot
loss_rect = patches.Rectangle((0, 0), 1, 1, fc = 'salmon') # red rectangle
gain_rect = patches.Rectangle((0, 0), 1, 1, fc = 'green') # green rectangle
pred_rect = patches.Rectangle((0, 0), 1, 1, fc = 'gray') # gray rectangle
plt.legend([loss_rect, gain_rect, pred_rect], ["Net loss", "Net gain", "Predicted"])

## Add labels and title to plot
title = sys.argv[1] + " Annual Net Income " + "(%d - " % min(years) + "%d)" % max(years) 
ax.set_title(title)
ax.set_xlabel('Year')
ax.set_ylabel('Net Income (in millions)')

## Set the background color for the plot
ax.set_facecolor('wheat')

## Adjust y range of plot
#ax.set_ylim(min(net_incomes + pred_net_incomes) - 200, max(net_incomes + pred_net_incomes) + 200)
ax.margins(0.10)

## Make x-axis visible on plot
ax.axhline(0, color = 'black')

## Angle years on x-axis, and only include every other year
plt.xticks(np.arange(min(years), max(extended_years) + 1, 2.0))
fig.autofmt_xdate()

## Display the plot
plt.show()
