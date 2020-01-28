#!/usr/bin/env python
# coding: utf-8

# In[7]:


import requests
import pandas as pd
import numpy as np
from datetime import datetime


# In[8]:


r = requests.get('https://view.inews.qq.com/g2/getOnsInfo?name=wuwei_ww_area_counts&callback=&_=')


# In[9]:


tx = r.text
tx = tx.replace('\\n','')
tx = tx.replace('\\','')
tx = tx.replace(' ','')


# In[10]:


tx = tx.split('[')[1]
tx = tx.split(']')[0]
df = pd.read_json('['+tx+']')


# In[11]:


cn = df[df.country == '中国']


# In[13]:


now = datetime.now()
current_time = now.strftime("%Y%m%d_%H%M")
df.to_excel('virus/'+current_time+'.xlsx')




