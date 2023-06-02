#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[9]:


#Import the dataset
nikeSet = pd.read_csv('nike_shoes_sales.csv')
nikeSet.head(20)
#Already looking at the set we can get rid of unneccessary columns


# In[38]:


#Cleaning the Dataframe
#Dropping unneeded columns
nikeCleaned = nikeSet.drop(['description','images','discount'], axis=1)

#converting prices into decimals
nikeCleaned['listing_price'] = nikeCleaned['listing_price'] / 100
nikeCleaned['sale_price'] = nikeCleaned['sale_price'] / 100

#Only want to look at shoes with active ratings/reviews
nike = nikeCleaned[nikeCleaned['reviews'] != 0]

#update the new index
nikeClean = nike.reset_index(drop=True)

nikeClean.head()


# In[39]:


#Start looking for patterns
nikeClean.describe()

