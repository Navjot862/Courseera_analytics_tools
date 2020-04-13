# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 16:57:15 2020

@author: M1030574
"""

import numpy
import pandas
import statsmodels.formula.api as smf
import statsmodels.stats.multicomp as multi

data = pandas.read_csv(‘nesarc_pds.csv’, low_memory=False)

#subset data
sub1=data[['ETHRACE2A’,'S3BQ3’]]
#rename column headings
sub1.rename(columns={'ETHRACE2A’:'RACE’,
                     'S3BQ3’:'NO_JOINTS’} ,
           inplace=True)

#set numeric
sub1['RACE’] = pandas.to_numeric(sub1['RACE’], errors='coerce’)
sub1['NO_JOINTS’] = pandas.to_numeric(sub1['NO_JOINTS’], errors='coerce’)

#SETTING MISSING DATA
sub1['NO_JOINTS’]=sub1['NO_JOINTS’].replace(99, numpy.nan)

#Drop rows with missing values
sub2 = sub1[['RACE’, 'NO_JOINTS’]].dropna()

#set variable race as categorical
sub2['RACE’] = sub2['RACE’].astype('category’)
#recode from numbers to ethnic groups for easier interpretation
recode1 = {1:'White’, 2:'Black’, 3:'American Indian/Alaska Native’, 4:'Asian’, 5:'Hispanic/Latino’}
sub2['RACE’]= sub2['RACE’].map(recode1)

#ANOVA analysis
mc1 = multi.MultiComparison(sub2['NO_JOINTS’],sub2['RACE’])
res1 = mc1.tukeyhsd()
print(res1.summary())

The results outputted are as follows:

group1          group2     meandiff p-adj   lower   upper  reject
———————————————————————-
         Asian           Black   1.0361 0.2352  -0.333  2.4051  False
         Asian Hispanic/Latino   0.4915 0.8523  -0.886   1.869  False
         Asian          Native   1.2146 0.2948  -0.492  2.9212  False
         Asian           White  -0.0249    0.9 -1.3407  1.2908  False
         Black Hispanic/Latino  -0.5446 0.1589 -1.2028  0.1136  False
         Black          Native   0.1785    0.9 -1.0249  1.3819  False
         Black           White   -1.061  0.001 -1.5777 -0.5443   True
Hispanic/Latino          Native   0.7231 0.4803 -0.4899  1.9361  False
Hispanic/Latino           White  -0.5165 0.0677 -1.0551  0.0222  False
        Native           White  -1.2395 0.0257 -2.3819 -0.0971   True

We can see from the results above that there are two cases where we can reject the null hypothesis of identical means. We can see that people from the black ethnic group smoke significantly more joints per day than the people from the white ethnic group. We also see native people also smoke significantly more joints per day than white people. 

