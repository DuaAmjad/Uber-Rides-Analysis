#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np # linear algebra
import pandas as pd # data processing
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx

import os


# In[3]:


uber_df = pd.read_csv("My Uber Drives - 2016.csv")


# Data Exploration

# In[4]:


# First 5 records 
uber_df.head()


# In[5]:


# Last 5 records 
uber_df.tail()


# In[6]:


# The  shape and size of data 
print(uber_df.shape)
print (uber_df.size)


# In[7]:


# Columns names 
uber_df.columns


# In[8]:


# Data  type of the columns 
uber_df.dtypes


# In[9]:


#get more information about data
uber_df.info()


# Data Cleaning

# In[10]:


# Check the missing values 
uber_df.isnull().any()


# In[11]:


#Get the number of missing values in each column
uber_df.isnull().sum()


# In[12]:


uber_df[uber_df['END_DATE*'].isnull()]


# In[13]:


uber_df.drop(uber_df.index[1155],inplace=True)
#Duplicated Records needs to be removed 
uber_df[uber_df.duplicated()]


# In[14]:


# Dropping the duplicates values 
uber_df.drop_duplicates(inplace=True)

# Get the initial data with dropping the NA values
uber_df = uber_df.dropna()

#Get the shape of the dataframe after removing the null values
uber_df.shape


# In[15]:


#get the summary of data
uber_df.describe().T


# Calculate the total duration of the Uber ride

# In[16]:


uber_df['START_DATE*'] = pd.to_datetime(uber_df['START_DATE*'])
uber_df['END_DATE*'] = pd.to_datetime(uber_df['END_DATE*'])

(uber_df['END_DATE*']-uber_df['START_DATE*'])


# In[17]:


uber_df['Duration'] = (uber_df['END_DATE*']-uber_df['START_DATE*']).dt.total_seconds()/60
uber_df.head()


# To Calculate the time of a day

# In[18]:


def timeofdayfnc(hour):
    if 5 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 17:
        return 'Afternoon'
    elif 17 <= hour < 20:
        return 'Evening'
    else:
        return 'Night'
uber_df['time_of_day'] = uber_df['START_DATE*'].dt.hour.apply(timeofdayfnc)
uber_df.head(5)


# In[19]:


print(uber_df.info())


# In[21]:


print("Total number of unique categories in CATEGORY - {}".format(uber_df['CATEGORY*'].nunique()))
print("Total number of unique categories in PURPOSE - {}".format(uber_df['PURPOSE*'].nunique()))
print("Total number of unique location in START - {}".format(uber_df['START*'].nunique()))
print("Total number of unique location in STOP - {}".format(uber_df['STOP*'].nunique()))


# In[ ]:


# Assuming df is your cleaned DataFrame
uber_df.to_csv('cleaned_data.csv', index=False)


# In[ ]:




