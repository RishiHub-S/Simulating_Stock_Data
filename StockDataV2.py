#!/usr/bin/env python
# coding: utf-8

# In[1]:


import scipy as sp
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


#DATA CREATION

#Generates DataFrame with Stock Name, Day, and Price.

#stock_name = [1,2]
#Generates stock_name list.
stock_name = []
for i in range(1,101): #range(start#, END# +1)
  stock_name.append(i)

#day = [1, 2, 3]
#Generates day list.
day = []
for i in range(1,31): #range(start#, END# +1)
  day.append(i)


stock_day_price = []

for z in stock_name:
    for x in day:
        for y in sp.random.uniform(low = sp.random.uniform(low = 10, high = 50, size = 1), high = sp.random.uniform(low = 51, high = 100, size = 1), size = 1):
            stock_day_price.append((z, x, y))
            stock_day_price_df = pd.DataFrame(stock_day_price, columns = ("Stock_Name", "Day", "Price"))


# In[3]:


stock_day_price_df


# In[4]:


#Generates DataFrame with Stock Name, Entry Day, and Exit Day.
#stock = [1, 2]
#entry_day = [1, 2, 3]
#exit_day = [1, 2, 3]

edxd = []

for z in stock_name:
    for x in day:
        for y in day:
            if x < y:  
                edxd.append((z, x, y))
                edxd_df = pd.DataFrame(edxd, columns = ("Stock_Name", "Entry_Day", "Exit_Day"))


# In[5]:


edxd_df


# In[6]:


#Combining Dataframes.
edxd_sdp_df1 = pd.merge(edxd_df, stock_day_price_df,  how='left', left_on=["Stock_Name", "Entry_Day"], right_on = ["Stock_Name", "Day"])
edxd_sdp_df1


# In[7]:


#Renamed Column
edxd_sdp_df1.rename(columns = {'Price': 'Entry_Price', 'Day':'ED'}, inplace = True)
edxd_sdp_df1


# In[8]:


edxd_sdp_df2 = pd.merge(edxd_sdp_df1, stock_day_price_df,  how='left', left_on=["Stock_Name", "Exit_Day"], right_on = ["Stock_Name", "Day"])

#Rename Column
edxd_sdp_df2.rename(columns = {'Price':'Exit_Price', 'Day':'XD'}, inplace = True)

#Delete ED & XD Columns
#edxd_sdp_df2.drop([['ED', 'XD']], 1, inplace=True)
edxd_sdp_df2.drop(edxd_sdp_df2.columns[[3, 5]], 1, inplace=True)
edxd_sdp_df2


# In[9]:


#####################################-----------MAIN DATA TABLE---------##############################################

#Creating Profit Column
edxd_sdp_df2['Profit'] = edxd_sdp_df2['Exit_Price'] - edxd_sdp_df2['Entry_Price']
edxd_sdp_df2


# In[10]:


#ANALYSIS


# In[11]:



#Takes the minimum price of the column 'Entry_Price' and lists both it's corresponding 'Stock_Name' and the minimum entry price.
minprice_bygroup = edxd_sdp_df2.groupby(['Stock_Name'])['Entry_Price'].min().reset_index()
minprice_bygroup.rename(columns = {'Entry_Price':'Min_Entry_Price'}, inplace = True)

minprice_withday = pd.merge(minprice_bygroup, edxd_sdp_df2,  how='left', left_on=["Stock_Name", "Min_Entry_Price"], right_on = ["Stock_Name", "Entry_Price"])

minprice_withday


# In[12]:


#Takes the minimum price of the column 'Exit_Price' and lists both it's corresponding 'Stock_Name' and the maximum entry price.
maxprice_bygroup = minprice_withday.groupby(['Stock_Name'])['Exit_Price'].max().reset_index()
maxprice_bygroup.rename(columns = {'Exit_Price':'Max_Exit_Price'}, inplace = True)
maxprice_bygroup

min_entry_max_exit = pd.merge(minprice_withday, maxprice_bygroup,  how='left', left_on=["Stock_Name", "Exit_Price"], right_on = ["Stock_Name", "Max_Exit_Price"])

min_entry_max_exit = min_entry_max_exit.dropna()

min_entry_max_exit = min_entry_max_exit.reindex(columns= ['Stock_Name', 'Min_Entry_Price','Max_Exit_Price','Entry_Day','Exit_Day', 'Profit'])
min_entry_max_exit


# In[13]:


min_entry_day_g= min_entry_max_exit['Entry_Day']
# Generate histogram/distribution plot
sns.displot(min_entry_day_g)
plt.show()


# In[14]:


max_exity_day_g = min_entry_max_exit['Exit_Day']
# Generate histogram/distribution plot
sns.displot(max_exity_day_g)
plt.show()


# In[15]:


sns.scatterplot(data=min_entry_max_exit, x="Entry_Day", y="Exit_Day")


# In[ ]:


#####################################---START OF PRICE REVERSION & MOMENTUM DATA CREATION & ANALYSIS---###################################

#For Reference
stock_day_price_df

meanprice_bygroup = stock_day_price_df.groupby(['Stock_Name'])['Price'].mean().reset_index()
meanprice_bygroup.rename(columns = {'Price':'Mean_Price'}, inplace = True)
meanprice_bygroup


# In[ ]:


#Shows the mean price of a single stock based on the prices on different days.
#Combines stockdaypricedf and meanpricebygroup
stock_pricereversion = pd.merge(stock_day_price_df, meanprice_bygroup,  how='left', left_on=["Stock_Name"], right_on = ["Stock_Name"])
stock_pricereversion


# In[ ]:


#Stocks, Day, Price with Price Reversion Data

stock_pricereversion['Price_Reversion'] = stock_pricereversion['Price'] - stock_pricereversion['Mean_Price']
stock_pricereversion


# In[ ]:


#Calculating Lag Price and Momentum
stock_pricereversion['Lag1_Price'] = stock_pricereversion['Price'].shift(-1) 
stock_pricereversion['Momentum'] = (stock_pricereversion['Price'].shift(-1) - stock_pricereversion['Price']) /  stock_pricereversion['Price']
stock_pricereversion


# In[ ]:


#Rearranges columns for clarity
SPM =stock_pricereversion.reindex(columns= ['Stock_Name', 'Day', 'Price','Lag1_Price', 'Mean_Price', 'Price_Reversion', 'Momentum'])
SPM

