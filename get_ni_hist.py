#!/usr/local/bin/python3.6

'''IMPORTS'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

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
def plot_lin_reg(x, y, ax, n_pred):
	
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

'''DATA'''
## SKYWORKS SOLUTIONS, INC. annual net income data (in millions) 
swks_ani_raw = {2016 : 1010,
		2015 : 995,
		2014 : 798,
		2013 : 458,
		2012 : 278,
		2011 : 202,
		2010 : 227,
		2009 : 137,
		2008 : 95,
		2007 : 111,
		2006 : 40,
		2005 : -105,
		2004 : 26,
		2003 : 22,
		2002 : -451,
		2001 : -236,
		2000 : -319,
		1999 : -66,
		1998 : 10,
		1997 : -16,
		1996 : 4,
		1995 : 3,
		1994 : -11,
		1993 : -3,
		1992 : 0.1,
		1991 : 2}

## List of years we have income date for (ascending)
years = list(reversed(list(key for key in swks_ani_raw)))

## List of net incomes (earliest to latest)
net_incomes = list(reversed(list(swks_ani_raw[key] for key in swks_ani_raw)))


'''DATA VISUALIZATION'''
## Create a figure and set of axes for plotting data
FIG_WIDTH = 10
FIG_HEIGHT = 6
fig, ax = plt.subplots(figsize = (FIG_WIDTH, FIG_HEIGHT))

plot_lin_reg(years, net_incomes, ax, 10)

plt.show()
