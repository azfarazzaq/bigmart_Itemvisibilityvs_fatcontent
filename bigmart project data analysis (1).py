#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os


# In[4]:


os.chdir("C:/Users/Azfa Razzaq/Videos/Captures")


# In[6]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[7]:


data= pd.read_csv("big_mart.csv")


# In[8]:


data


# In[10]:


data["Item_Fat_Content"].unique()


# In[15]:


data["Item_Fat_Content"]=data["Item_Fat_Content"].str.replace(('low fat|LF'),'Low Fat')
data["Item_Fat_Content"]=data["Item_Fat_Content"].str.replace('reg','Regular')


# In[16]:


data["Item_Fat_Content"].unique()


# In[19]:


data.columns


# In[21]:


data.info()


# In[28]:


low_fat_data=data[data['Item_Fat_Content']=="Low Fat"]
Regular_fat_data=  data[data['Item_Fat_Content']=="Regular"]  


# In[69]:


#plotting the data set

fig,axes= plt.subplots(nrows=1,ncols=2,figsize=(15,5))
(ax1,ax2)=axes
ax1.hist(low_fat_data['Item_Visibility'],bins=10,alpha=0.5,label = "low fat")
ax1.hist(Regular_fat_data['Item_Visibility'],bins=10,alpha=0.3,label = "low fat")
ax1.legend()
ax1.set_title("Item Visibily vs. Fat content Histogram")
ax1.set_xlabel("Item Visibility")
ax1.set_ylabel("Item count")

ax2plot=sns.ecdfplot(data=data, x="Item_Visibility",ax=ax2,hue='Item_Fat_Content')

lowfat_median=low_fat_data["Item_Visibility"].median()
Regfat_median=Regular_fat_data["Item_Visibility"].median()


#grid lines
ax2plot.axvline(x=lowfat_median,ymax=0.5,ls="--",color="black",alpha=0.5)
ax2plot.axvline(x=Regfat_median,ymax=0.5,ls="--",color="black",alpha=0.5)
ax2plot.axhline(y=0.5,ls="--",color="black",alpha=0.5)

#annotations
arrow_props= dict(arrowstyle="->",connectionstyle="angle,angleA=0,angleB=90,rad=10")
ax2plot.annotate("$Median_{low}=%.4f$"%lowfat_median,xytext=(0.11,0.6), xy=(lowfat_median,0.5) ,arrowprops=arrow_props)
ax2plot.annotate("$Median_{Reg}=%.4f$"%Regfat_median,xytext=(0.11,0.7), xy=(Regfat_median,0.5),arrowprops=arrow_props)

plt.show()
plt.savefig("Item visibity vs fat content")


# In[72]:


data["Outlet_Type"].unique()


# In[76]:


data["Outlet_Type"].value_counts()


# In[83]:


data["Item_Type"].unique()


# In[ ]:





# In[ ]:












