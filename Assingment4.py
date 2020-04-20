# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 10:30:04 2020

@author: M1030574
"""


import pandas as pd
import seaborn as sns
import scipy.stats
 
data = pd.read_csv('c:/users/greg/desktop/gapminder.csv', low_memory=False)

data['internetuserate'] = pd.to_numeric(data['internetuserate'], errors='coerce')
data['polityscore'] = pd.to_numeric(data['polityscore'], errors='coerce')
 
sub1 = data.copy()

sub3 = sub1[['internetuserate', 'polityscore']].dropna()
sub3['polityscore_binned'] = pd.cut(sub3.polityscore, 3, labels=['Low', 'Mid', 'High'])
sub3['internetuserate_binned'] = pd.cut(sub3.internetuserate, 2, labels=['Low', 'High'])

sub4 = sub3.copy()

ct1 = pd.crosstab(sub4['internetuserate_binned'], sub4['polityscore_binned'])
ct1

colsum=ct1.sum(axis=0)
colpct=ct1/colsum
colpct

cs1= scipy.stats.chi2_contingency(ct1)
cs1



sns.factorplot(x="polityscore_binned", y="internetuserate", data=sub4, kind="bar", ci=None)
plt.xlabel('Polity Score')
plt.ylabel('Internet Use Rate')
sns.plt.show()



recode1 = {'Low': 'Low', 'Mid': 'Mid'}
sub4['COMP-Low-v-Mid']= sub4['polityscore_binned'].map(recode1)


ct2=pd.crosstab(sub4['internetuserate_binned'], sub4['COMP-Low-v-Mid'])
ct2

colsum=ct2.sum(axis=0)
colpct=ct2/colsum
colpct

cs2= scipy.stats.chi2_contingency(ct2)
cs2

recode2 = {'Low': 'Low', 'High': 'High'}
sub4['COMP-Low-v-High']= sub4['polityscore_binned'].map(recode2)

ct3=pd.crosstab(sub4['internetuserate_binned'], sub4['COMP-Low-v-High'])
ct3

colsum=ct3.sum(axis=0)
colpct=ct3/colsum
colpct


cs3= scipy.stats.chi2_contingency(ct3)
cs3

recode3 = {'Mid': 'Mid', 'High': 'High'}
sub4['COMP-Mid-v-High']= sub4['polityscore_binned'].map(recode3)

ct4=pd.crosstab(sub4['internetuserate_binned'], sub4['COMP-Mid-v-High'])
ct4

colsum=ct4.sum(axis=0)
colpct=ct4/colsum
colpct

cs4= scipy.stats.chi2_contingency(ct4)
cs4
