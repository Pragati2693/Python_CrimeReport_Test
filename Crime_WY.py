#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
from collections import Counter
import matplotlib
matplotlib.style.use('ggplot')
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


data1 = pd.read_csv(r"D:\R Studio\RStudio\CrimeD\2022-09\Crime_WY.csv")
data1.head()


# In[3]:


data1.drop("Context",axis = 1, inplace = True)


# In[4]:


Crime_sum = data1["Crime type"].value_counts()


# In[5]:


Crime_sum = Crime_sum.to_frame().reset_index().rename(columns = {'index':'CrimeType','Crime type':'Count'})


# In[6]:


Crime_sum = Crime_sum.set_index('CrimeType')


# In[69]:


Crime_sum.plot(kind = 'pie',y = 'Count', autopct='%1.0f%%', figsize = (10,10)) #41% of crime is on voilence ans sexual offence


# In[8]:


data1[data1.Location == 'No Location'] #497 does not have any location


# In[9]:


CrimeLSOA = data1["LSOA name"].value_counts().head(13)


# In[ ]:





# In[10]:


CLSOA = CrimeLSOA.to_frame().reset_index().rename(columns = {'index':'LSOA name', 'LSOA name': 'count'})


# In[11]:


CLSOA.plot.bar(x = 'LSOA name',y = 'count') # Area with more than 100 crimes in month of sep


# In[12]:


data1["new LSOA"] = data1["LSOA name"].str.split(expand = True)[0]
dataA = data1['new LSOA'].value_counts().to_frame()
dataA = dataA.rename(columns = {"new LSOA": "count"})


# In[13]:


dataA.plot.pie(y = 'count', figsize = (8,10),autopct='%1.0f%%') # Most of the crime is in Leeds  and almost no crime in barnsley,Selby,Harrogate


# In[14]:


DataLC = data1.groupby(["new LSOA","Crime type"])


# In[15]:


data_LC = DataLC["Crime ID"].count().to_frame()


# In[16]:


data_LC.rename(columns = {"Crime ID": "Count"}, inplace = True)


# In[17]:


data_LC.head()


# In[18]:


pivot = pd.pivot_table(data=data_LC, index=['new LSOA'], columns=['Crime type'], values='Count')


# In[19]:


pivot.fillna(0, inplace = True)


# In[20]:


pivot.plot.bar(stacked = True, figsize = (12,7), color =['lightseagreen', 'tomato','pink','blue','olive','yellow','indigo','white','grey','red','purple','brown','black','coral'])


# In[21]:


data2 = pd.read_csv(r"D:\R Studio\RStudio\CrimeD\2022-09\2022-09-west-yorkshire-outcomes.csv")


# In[22]:


data2O = data2["Outcome type"].value_counts().to_frame()
data2O = data2O.reset_index()


# In[23]:


data2O = data2O.rename(columns = {"index":"Outcome","Outcome type":"Count2"})
data2O.head()


# In[24]:


dataLast = data1["Last outcome category"].value_counts().to_frame().reset_index()


# In[25]:


data1O = dataLast.rename(columns = {"index":"Outcome","Last outcome category":"Count1"})


# In[26]:


data1O.head()


# In[27]:


merged_df1 = pd.merge(data1O,data2O,how='outer',on=['Outcome'])


# In[28]:


merged_df1[['Count1','Count2']] = merged_df1[['Count1','Count2']].fillna(0)
merged_df1.head()
merged_df1.plot(kind = 'bar', x = 'Outcome', y = ['Count1','Count2']) #count1 is before EOM and count2 is after EOM


# In[29]:


data2.info()#data1 has 28446 entries and data2 has 27731 entries, which means that 715 entries are not addresed
data1.info()


# In[30]:


data12 = pd.merge(data1, data2, how = 'left', on = 'Crime ID')
data12.columns


# In[31]:


data12.drop(['Month_y','Reported by_y','Falls within_y','Longitude_y','Latitude_y','Location_y','LSOA code_y','LSOA name_y'], axis = 1, inplace = True)


# In[32]:


data12.drop(['Reported by_x', 'Falls within_x', 'Longitude_x', 'Latitude_x', 'Location_x', 'LSOA code_x'], axis = 1, inplace = True)


# In[33]:


data12.info()


# In[34]:


sns.heatmap(data12.isnull()) # shows that there are null values in crime id, last outcome category and most in Outcome type


# In[35]:


data12["Outcome type"].value_counts()


# In[36]:


dtemp1 = data12.groupby(["Crime type","Outcome type"])


# In[37]:


dtemp = dtemp1['Crime ID'].count().to_frame().reset_index()


# In[38]:


dtemp.rename(columns = {"Crime ID": "Count"}, inplace = True)


# In[39]:


dtemp = dtemp.sort_values(by = "Count", ascending = False)


# In[40]:


pivot2 = pd.pivot_table(data=dtemp, index=['Outcome type'], columns=['Crime type'], values='Count')


# In[41]:


pivot2.fillna(0, inplace = True)
pivot2.plot.bar(stacked = True, figsize = (12,7), color =['maroon','cyan','blue','yellow','indigo','red','purple','brown','coral','pink','darkorchid','slateblue','teal'])
# graph shows that most of the crimes outcome is investigation complete with no suspect identified and police is unable to prosecute suspect for most of thevoice case


# In[42]:


data12 = data12.dropna(subset = ['Crime ID']) # dropping all the rows for which Crime ID is null


# In[43]:


data12["Outcome type"].isna().sum()


# In[44]:


OutcomeN = data12[data12["Outcome type"].isna()] # stroring data for which outcome is null and 12647 cases has no outcome


# In[45]:


OutcomeN.groupby("Crime type")["Last outcome category"].count().plot.bar() #shows that more than half of those cases for which no justification provided involved 'voilence n sexual offence cases'


# In[46]:


data12.head()


# In[47]:


#plot = df.plot.pie(subplots=True, figsize=(6, 4))
#df = pd.DataFrame({'mass': [2.87, 5.97, 6.00],
                  #'radius': [6051.8, 6378.1, 71492]},
                  #index=['Venus', 'Earth', 'Jupiter'])
#plot = df.plot.pie(y='mass', figsize=(5, 5))


# In[48]:


data12['Outcome type'].fillna(0,inplace = True)
dataLOC = data12.groupby(['new LSOA','Outcome type'])


# In[49]:


dataLOC = dataLOC['Crime ID'].count().to_frame()


# In[50]:


dataLOC.rename(columns = {"Crime ID":"Count"}, inplace = True)


# In[51]:


pivot3 = pd.pivot_table(data=dataLOC, index=['new LSOA'], columns=['Outcome type'], values='Count')


# In[52]:


pivot3.fillna(0, inplace = True)


# In[53]:


pivot3.plot.bar(stacked = True, figsize = (12,7), color =['maroon','cyan','blue','yellow','indigo','red','purple','brown','coral','pink','darkorchid','slateblue','teal'])


# In[54]:


data1[data1["Crime ID"].isna()]["new LSOA"].value_counts() #most of the null value of crime id is from Leeds but proportion of leeds n Bradford  n Wakefield which is 8%


# In[55]:


data1["new LSOA"].value_counts() #crimid null for Kirklees is 9%,8% Calderdale, 4% for Harrogate n 0% for selby n bernsley


# In[56]:


dataSimi = data12[data12["Last outcome category"] == data12["Outcome type"]]


# In[57]:


dataSimi["Outcome type"].value_counts()


# In[58]:


data1['Last outcome category'].value_counts() # shows that there is no chnage in value of 'last outcome cat' n 'outcome type' for
                                              #Investigation complete; no suspect identified,Unable to prosecute suspect,
                                             #Further investigation is not in the public interest,Action to be taken by another organisation 
                                            #Formal action is not in the public interest,Offender given a caution


# In[59]:


dataCourtA = data12[data12["Last outcome category"] =="Awaiting court outcome"]


# In[60]:


dataCourtA["Outcome type"].value_counts() #shows that the last outcome with "awaiting cout outcome" chnage to "Suspect charged"


# In[61]:


dataNSimi = data12[data12["Last outcome category"] != data12["Outcome type"]] # not similar data


# In[62]:


dataNSimi["Last outcome category"].value_counts() # shows that almost all "under investigation" outcome is chnaged


# In[63]:


data_U_I = dataNSimi[dataNSimi["Last outcome category"] == "Under investigation"]


# In[64]:


data_U_I["Outcome type"].value_counts() # shows that all the "Under investigation" outcome before month end has no value/0/null in "Outcome type"
                                        # and there are 12647 crimes with no outcome in the end of the month

