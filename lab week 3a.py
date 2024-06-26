#NAMES
#As always, attempt your lab without searching for solutions online unless otherwise noted

#1: This code does not run!  Try it and examine the errors, then figure out what needs to
#be changed to make it work.  Do not create any, global variables, delete any existing
#code, or cut and paste existing code to new locations.

a = 10

def first_func(b=20):
    c = 30
    value = second_func()
    return value

def second_func(d=40):
    e = 50
    return a + b + c + d + e

result = first_func()

def my_func(a=10, b=20, c=30,d=40,e=50):
    new_func = a + b + c + d + e
    return new_func
print(my_func())

#2: Take this code from last week's lab and write functions so that the final
#execution looks like:
#answer = {key_func(k):val_func(v) for k, v in start_dict.items()}

import datetime
start_dict = {'noah': '2/23/1999',
              'sarah':'9/1/2001',
              'zach': '8/8/2005'}
#turn it into {'Noah': datetime.datetime(1999, 2, 23),
#              'Sarah': datetime.datetime(2001, 9, 1),
#              'Zach': datetime.datetime(2005, 8, 8)}


def key_func(k):
    k = k.capitalize()
    return k

def val_func(v):
    v = datetime.strptime(v, "%m/%d/%Y")
    return v

new_dates = {key_func(k):val_func(v) for k, v in start_dict.items()}

#3: A zscore is one term to describe data transformed to have mean zero and
#standard deviation one, given by: x - x_mean / x_std
#Write a function that takes any list-like object as a positional argument,
#then returns an object of the same dimensions with the zscores for the series.
#Use these two imported functions, and test your results on several lists of
#values
from numpy import mean, std
x = (1, 2, 3)


def zscore(num, average=mean(x), standard=std(x)):
    y = ((num-average))/standard
    return y

w = (4, 5, 6)

w_zscore = zscore(w, average=mean(w), standard=std(w))
x_zscore = zscore(x)
f = (200, 45, 72)
f_zscore = zscore(f, average=mean(f),standard=std(f))
#4: A modified zscore uses the "median absolute deviation" to better handle
#outliers in the data, where the MAD is calculated by:
#  1. x - the median of the series
#  2. the absolute values of the results from 1
#  3. the median of the results from 2
#and finally, replace the standard deviation in the formula for the zscore from
#question 3 with the results from this process: x - x_mean / MAD
#
#Copy the function you created in 3 and create an optional key word argument that
#lets you override the default zscore calculation to instead use the modified
#version. This function should work in both question 3 and 4 without needing to
#change how you call it in part 3, because of its default behavior
from numpy import median, absolute
x_median = median(x)
x_1 = x

def mad (num):
    step_1 = num - median(num)
    step_2 = absolute(step_1)
    step_3 = median(step_2)
    return step_3
x_mad = mad(x)
def zscore(num, standard=std(x)):
    average = num - mean(num)
    y = average/standard
    return y
x_zscore = zscore(x)
x_mad_zscore = zscore(x, standard=mad(x))
w_mad_zscore = zscore(w, standard=mad(w))
f_mad_score = zscore(f, standard=mad(f))
