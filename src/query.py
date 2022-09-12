#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import glob
import numpy as np


# In[5]:


CSV_PATH="D:/SimGNNDATA/CSVFiles" #기존 CSV파일 Folder경로
CSV_LIST=glob.glob(CSV_PATH+'/*.csv') #CSV 파일 하나씩 경로 리스트화


# In[14]:


len(CSV_LIST)


# # 거실

# ### 1. 거실-식당

# In[12]:


#거실-식당이 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 1) & (df['Adj_Label']==20)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 2. 거실<->식당

# In[9]:


#거실<->식당이 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 1) & (df['Adj_Label']==20)]['ID_encode'].values
    if len(FIND)==0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 3. 거실-복도

# In[15]:


#거실-복도가 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 1) & (df['Adj_Label']==8)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 4. 거실-화장실

# In[18]:


#거실-화장실 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 1) & (df['Adj_Label']==4)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 5. 거실-방

# In[ ]:


#거실-방 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 1) & (df['Adj_Label']==2)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 6. 거실-계단

# In[ ]:


#거실-계단 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 1) & (df['Adj_Label']==7)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 7. 거실-주방

# In[ ]:


#거실-주방 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 1) & (df['Adj_Label']==3)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 8. 거실-현관

# In[ ]:


#거실-현관 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 1) & (df['Adj_Label']==0)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 9. 거실-차고지

# In[ ]:


#거실-차고지 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 1) & (df['Adj_Label']==19)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 10. 거실-다용도실

# In[ ]:


#거실-다용도실 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 1) & (df['Adj_Label']==6)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# # 주방

# ### 1. 식당 <-> 주방 - 거실

# In[6]:


#식당<->주방-거실이 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 3) & (df['Adj_Label']==1)]['ID_encode'].values
    FIND1=df.loc[(df['Label'] == 20) & (df['Adj_Label']==3)]['Adj_ID_encode'].values
    FIND2=df.loc[(df['Label'] == 20)]['Adj_ID_encode'].values
    BOOL_FIND=np.setdiff1d(FIND, FIND1)
    if (len(BOOL_FIND)!=0)&(len(FIND1)==0)&(len(FIND2)!=0):
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 2.주방<->식당

# In[ ]:


#주방<->식당이 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 3) & (df['Adj_Label']==20)]['ID_encode'].values
    if len(FIND)==0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 3.주방-펜트리실

# In[ ]:


#주방-펜트리실 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 3) & (df['Adj_Label']==9)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 4.주방-차고지

# In[ ]:


#주방-차고지 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 3) & (df['Adj_Label']==19)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 5.주방-복도

# In[ ]:


#주방-복도 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 3) & (df['Adj_Label']==8)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 6. 주방-붙박이실

# In[ ]:


#주방-붙박이실 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 3) & (df['Adj_Label']==11)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 7.주방-다용도실

# In[ ]:


#주방-다용도실 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 3) & (df['Adj_Label']==6)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 8.주방-포치

# In[ ]:


#주방-포치 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 3) & (df['Adj_Label']==18)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 9.주방-세탁실

# In[ ]:


#주방-세탁실 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 3) & (df['Adj_Label']==10)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 10.주방-화장실

# In[ ]:


#주방-화장실 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 3) & (df['Adj_Label']==4)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# # 식당

# ### 1.식당-복도

# In[ ]:


#식당-복도 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 20) & (df['Adj_Label']==8)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 2.식당-포치

# In[ ]:


#식당-포치 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 20) & (df['Adj_Label']==18)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 3.식당-주방

# In[ ]:


#식당-주방 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 20) & (df['Adj_Label']==3)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 4.식당-주방-복도

# In[ ]:


#식당-주방-복도이 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 20) & (df['Adj_Label']==3)]['Adj_ID_encode'].values
    FIND1=df.loc[(df['Label'] == 3) & (df['Adj_Label']==8)]['ID_encode'].values
    BOOL_FIND=np.intersect1d(FIND, FIND1)
    if len(BOOL_FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 5.식당-주방-거실

# In[ ]:


#식당-주방-거실이 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 20) & (df['Adj_Label']==3)]['Adj_ID_encode'].values
    FIND1=df.loc[(df['Label'] == 3) & (df['Adj_Label']==1)]['ID_encode'].values
    BOOL_FIND=np.intersect1d(FIND, FIND1)
    if len(BOOL_FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 6.복도-식당-주방-거실

# In[34]:


#복도-식당-주방-거실이 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 8) & (df['Adj_Label']==20)]['Adj_ID_encode'].values #복도-식당
    FIND1=df.loc[(df['Label'] == 20) & (df['Adj_Label']==3)]['ID_encode'].values #식당-주방
    
    FIND2=df.loc[(df['Label'] == 20) & (df['Adj_Label']==3)]['Adj_ID_encode'].values #식당-주방
    FIND3=df.loc[(df['Label'] == 3) & (df['Adj_Label']==1)]['ID_encode'].values #주방-거실
    
    BOOL_FIND=np.intersect1d(FIND, FIND1)
    BOOL_FIND1=np.intersect1d(FIND2, FIND3)
    if (len(BOOL_FIND)!=0)&(len(BOOL_FIND1)!=0):
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 7.차고지-식당-주방-거실

# In[37]:


#차고지-식당-주방-거실이 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 19) & (df['Adj_Label']==20)]['Adj_ID_encode'].values #차고지-식당
    FIND1=df.loc[(df['Label'] == 20) & (df['Adj_Label']==3)]['ID_encode'].values #식당-주방
    
    FIND2=df.loc[(df['Label'] == 20) & (df['Adj_Label']==3)]['Adj_ID_encode'].values #식당-주방
    FIND3=df.loc[(df['Label'] == 3) & (df['Adj_Label']==1)]['ID_encode'].values #주방-거실
    
    BOOL_FIND=np.intersect1d(FIND, FIND1)
    BOOL_FIND1=np.intersect1d(FIND2, FIND3)
    if (len(BOOL_FIND)!=0)&(len(BOOL_FIND1)!=0):
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 8.식당-계단실

# In[ ]:


#식당-계단실 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 20) & (df['Adj_Label']==7)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 9.식당-펜트리실

# In[ ]:


#식당-팬트리실 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 20) & (df['Adj_Label']==9)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 10.식당-주방-팬트리실

# In[ ]:


#식당-주방-팬트리실 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 20) & (df['Adj_Label']==3)]['Adj_ID_encode'].values
    FIND1=df.loc[(df['Label'] == 3) & (df['Adj_Label']==9)]['ID_encode'].values
    BOOL_FIND=np.intersect1d(FIND, FIND1)
    if len(BOOL_FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# # 방

# ### 1. 방-드레스룸

# In[ ]:


#방-드레스룸 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 2) & (df['Adj_Label']==5)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 2. 방-드레스룸, 방-화장실

# In[ ]:


#방-드레스룸,방-화장실 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 2) & (df['Adj_Label']==5)]['ID_encode'].values
    FIND1=df.loc[(df['Label'] == 2) & (df['Adj_Label']==4)]['ID_encode'].values
    if (len(FIND1)!=0)&(len(FIND)!=0):
            Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 3. 거실-방-드레스룸

# In[20]:


#거실-방-드레스룸이 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 8) & (df['Adj_Label']==2)]['Adj_ID_encode'].values
    FIND1=df.loc[(df['Label'] == 2) & (df['Adj_Label']==5)]['ID_encode'].values
    BOOL_FIND=np.intersect1d(FIND, FIND1)
    if len(BOOL_FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 4. 거실-방-화장실

# In[15]:


#거실-방-화장실 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 1) & (df['Adj_Label']==2)]['Adj_ID_encode'].values
    FIND1=df.loc[(df['Label'] == 2) & (df['Adj_Label']==4)]['ID_encode'].values
    BOOL_FIND=np.intersect1d(FIND, FIND1)
    if len(BOOL_FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 5. 거실-방-붙박이장

# In[25]:


Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 1) & (df['Adj_Label']==2)]['ID_encode'].values
    FIND1=df.loc[(df['Label'] == 2) & (df['Adj_Label']==11)]['Adj_ID_encode'].values
    BOOL_FIND=np.intersect1d(FIND, FIND1)
    if len(BOOL_FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 6. 방-다용도실

# In[ ]:


#방-다용도실 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 2) & (df['Adj_Label']==6)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 7. 방-계단

# In[ ]:


#방-계단 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 2) & (df['Adj_Label']==7)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 8. 방-화장실, 방-붙박이장

# In[ ]:


#방-붙박이장,방-화장실 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 2) & (df['Adj_Label']==11)]['ID_encode'].values
    FIND1=df.loc[(df['Label'] == 2) & (df['Adj_Label']==4)]['ID_encode'].values
    if (len(FIND1)!=0)&(len(FIND)!=0):
            Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 9. 방-드레스룸, 방-화장실, 방-복도

# In[ ]:


#방-드레스룸,방-화장실,방-복도 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 2) & (df['Adj_Label']==5)]['ID_encode'].values
    FIND1=df.loc[(df['Label'] == 2) & (df['Adj_Label']==4)]['ID_encode'].values
    FIND2=df.loc[(df['Label'] == 2) & (df['Adj_Label']==8)]['ID_encode'].values
    if (len(FIND1)!=0)&(len(FIND)!=0)&(len(FIND2)!=0):
            Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 10. 방-붙박이장

# In[ ]:


#방-붙박이장 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 2) & (df['Adj_Label']==11)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# # 화장실

# ### 1.화장실-복도

# In[ ]:


#화장실-복도 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 4) & (df['Adj_Label']==8)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 2.화장실-방

# In[ ]:


#화장실-방 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 4) & (df['Adj_Label']==2)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 3.화장실-다용도실

# In[ ]:


#화장실-다용도실 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 4) & (df['Adj_Label']==6)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 4.화장실-드레스룸

# In[ ]:


#화장실-드레스룸 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 4) & (df['Adj_Label']==5)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 7.방-화장실-드레스룸

# In[ ]:


#방-화장실-드레스룸 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 2) & (df['Adj_Label']==4)]['Adj_ID_encode'].values
    FIND1=df.loc[(df['Label'] == 4) & (df['Adj_Label']==5)]['ID_encode'].values
    BOOL_FIND=np.intersect1d(FIND, FIND1)
    if len(BOOL_FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 8.복도-방-화장실

# In[ ]:


#복도-방-화장실 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 8) & (df['Adj_Label']==2)]['Adj_ID_encode'].values
    FIND1=df.loc[(df['Label'] == 2) & (df['Adj_Label']==4)]['ID_encode'].values
    BOOL_FIND=np.intersect1d(FIND, FIND1)
    if len(BOOL_FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 9.거실-화장실-복도

# In[ ]:


#거실-화장실-복도 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 1) & (df['Adj_Label']==4)]['Adj_ID_encode'].values
    FIND1=df.loc[(df['Label'] == 4) & (df['Adj_Label']==8)]['ID_encode'].values
    BOOL_FIND=np.intersect1d(FIND, FIND1)
    if len(BOOL_FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 10.차고지-화장실

# In[ ]:


#차고지-화장실 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 19) & (df['Adj_Label']==4)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# # 복도

# ### 1.복도-방

# In[43]:


#복도-방 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 8) & (df['Adj_Label']==2)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 2.복도-붙박이장

# In[ ]:


#복도-붙박이장 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 8) & (df['Adj_Label']==11)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 3.복도-방-붙박이장

# In[ ]:


#복도-방-붙박이장 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 8) & (df['Adj_Label']==2)]['Adj_ID_encode'].values
    FIND1=df.loc[(df['Label'] == 2) & (df['Adj_Label']==11)]['ID_encode'].values
    BOOL_FIND=np.intersect1d(FIND, FIND1)
    if len(BOOL_FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 4.거실-복도-차고지

# In[ ]:


#거실-복도-차고지 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 1) & (df['Adj_Label']==8)]['Adj_ID_encode'].values
    FIND1=df.loc[(df['Label'] == 8) & (df['Adj_Label']==19)]['ID_encode'].values
    BOOL_FIND=np.intersect1d(FIND, FIND1)
    if len(BOOL_FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 5.복도-계단

# In[ ]:


#복도-계단 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 8) & (df['Adj_Label']==7)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 6.복도-다용도실

# In[ ]:


#복도-다용도실 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 8) & (df['Adj_Label']==6)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 7.복도-현관

# In[ ]:


#복도-현관 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 8) & (df['Adj_Label']==0)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 8.복도-복도

# In[ ]:


#복도-복도 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 8) & (df['Adj_Label']==8)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 9.복도-방-드레스룸

# In[ ]:


#복도-방-드레스룸 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 8) & (df['Adj_Label']==2)]['Adj_ID_encode'].values
    FIND1=df.loc[(df['Label'] == 2) & (df['Adj_Label']==5)]['ID_encode'].values
    BOOL_FIND=np.intersect1d(FIND, FIND1)
    if len(BOOL_FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 10.복도-세탁실

# In[ ]:


#복도-세탁실 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 8) & (df['Adj_Label']==10)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# # 현관

# ### 1.현관-방

# In[ ]:


#현관-방 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 0) & (df['Adj_Label']==2)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 2.현관-붙박이장

# In[ ]:


#현관-붙박이장 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 0) & (df['Adj_Label']==11)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 3.현관-복도-거실

# In[ ]:


#현관-복도-거실 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 0) & (df['Adj_Label']==8)]['Adj_ID_encode'].values
    FIND1=df.loc[(df['Label'] == 8) & (df['Adj_Label']==1)]['ID_encode'].values
    BOOL_FIND=np.intersect1d(FIND, FIND1)
    if len(BOOL_FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 4.현관-포치

# In[ ]:


#현관-방 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 0) & (df['Adj_Label']==18)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 5.현관-차고지

# In[ ]:


#현관-방 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 0) & (df['Adj_Label']==19)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 6.포치-복도-현관

# In[ ]:


#포치-복도-현관 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 18) & (df['Adj_Label']==8)]['Adj_ID_encode'].values
    FIND1=df.loc[(df['Label'] == 8) & (df['Adj_Label']==0)]['ID_encode'].values
    BOOL_FIND=np.intersect1d(FIND, FIND1)
    if len(BOOL_FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 7.현관-방-붙박이장

# In[ ]:


#현관-방-붙박이장 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 0) & (df['Adj_Label']==2)]['Adj_ID_encode'].values
    FIND1=df.loc[(df['Label'] == 2) & (df['Adj_Label']==11)]['ID_encode'].values
    BOOL_FIND=np.intersect1d(FIND, FIND1)
    if len(BOOL_FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 8.현관-방-드레스룸

# In[ ]:


#현관-방-드레스룸 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 0) & (df['Adj_Label']==8)]['Adj_ID_encode'].values
    FIND1=df.loc[(df['Label'] == 8) & (df['Adj_Label']==5)]['ID_encode'].values
    BOOL_FIND=np.intersect1d(FIND, FIND1)
    if len(BOOL_FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 9.현관-방-화장실-드레스룸

# In[ ]:


#현관-방-화장실-드레스룸이 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 0) & (df['Adj_Label']==2)]['Adj_ID_encode'].values #현관-방
    FIND1=df.loc[(df['Label'] == 2) & (df['Adj_Label']==4)]['ID_encode'].values #방-화장실
    
    FIND2=df.loc[(df['Label'] == 2) & (df['Adj_Label']==4)]['Adj_ID_encode'].values #방-화장실
    FIND3=df.loc[(df['Label'] == 4) & (df['Adj_Label']==5)]['ID_encode'].values #화장실-드레스룸
    
    BOOL_FIND=np.intersect1d(FIND, FIND1)
    BOOL_FIND1=np.intersect1d(FIND2, FIND3)
    if (len(BOOL_FIND)!=0)&(len(BOOL_FIND1)!=0):
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 10.현관-복도-주방

# In[ ]:


#현관-복도-주방 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 0) & (df['Adj_Label']==8)]['Adj_ID_encode'].values
    FIND1=df.loc[(df['Label'] == 8) & (df['Adj_Label']==3)]['ID_encode'].values
    BOOL_FIND=np.intersect1d(FIND, FIND1)
    if len(BOOL_FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# # 계단

# ### 1.계단-현관

# In[ ]:


#계단-현관 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 7) & (df['Adj_Label']==0)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 2.계단-식당

# In[ ]:


#계단-식당 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 7) & (df['Adj_Label']==20)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 3.계단-주방

# In[ ]:


#계단-주방 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 7) & (df['Adj_Label']==3)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 4.계단-다용도실

# In[ ]:


#계단-다용도실 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 7) & (df['Adj_Label']==6)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 5.계단-화장실

# In[ ]:


#계단-화장실 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 7) & (df['Adj_Label']==4)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 6.계단-현관-포치

# In[ ]:


#계딴-현관-포치 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 7) & (df['Adj_Label']==0)]['Adj_ID_encode'].values
    FIND1=df.loc[(df['Label'] == 0) & (df['Adj_Label']==18)]['ID_encode'].values
    BOOL_FIND=np.intersect1d(FIND, FIND1)
    if len(BOOL_FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 7.계단-방-붙박이장

# In[ ]:


#계단-방-붙박이장 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 7) & (df['Adj_Label']==2)]['Adj_ID_encode'].values
    FIND1=df.loc[(df['Label'] == 2) & (df['Adj_Label']==11)]['ID_encode'].values
    BOOL_FIND=np.intersect1d(FIND, FIND1)
    if len(BOOL_FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 8.계단-방-화장실

# In[ ]:


#계단-방-화장실 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 7) & (df['Adj_Label']==2)]['Adj_ID_encode'].values
    FIND1=df.loc[(df['Label'] == 2) & (df['Adj_Label']==4)]['ID_encode'].values
    BOOL_FIND=np.intersect1d(FIND, FIND1)
    if len(BOOL_FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 9.계단-방-드레스룸

# In[ ]:


#계단-방-드레스룸 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 7) & (df['Adj_Label']==2)]['Adj_ID_encode'].values
    FIND1=df.loc[(df['Label'] == 2) & (df['Adj_Label']==5)]['ID_encode'].values
    BOOL_FIND=np.intersect1d(FIND, FIND1)
    if len(BOOL_FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 10.계단-방-화장실-드레스룸

# In[ ]:


#계단-방-화장실-드레스룸이 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 7) & (df['Adj_Label']==2)]['Adj_ID_encode'].values #계단-방
    FIND1=df.loc[(df['Label'] == 2) & (df['Adj_Label']==4)]['ID_encode'].values #방-화장실
    
    FIND2=df.loc[(df['Label'] == 2) & (df['Adj_Label']==4)]['Adj_ID_encode'].values #방-화장실
    FIND3=df.loc[(df['Label'] == 4) & (df['Adj_Label']==5)]['ID_encode'].values #화장실-드레스룸
    
    BOOL_FIND=np.intersect1d(FIND, FIND1)
    BOOL_FIND1=np.intersect1d(FIND2, FIND3)
    if (len(BOOL_FIND)!=0)&(len(BOOL_FIND1)!=0):
        Test.append(CSV.split('\\')[-1].split('.')[0])


# # 차고지

# ### 1.차고지-다용도실

# In[ ]:


#차고지-다용도실 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 19) & (df['Adj_Label']==6)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 2.차고지-다용도실-거실

# In[ ]:


#차고지-다용도실-거실 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 19) & (df['Adj_Label']==6)]['Adj_ID_encode'].values
    FIND1=df.loc[(df['Label'] == 6) & (df['Adj_Label']==1)]['ID_encode'].values
    BOOL_FIND=np.intersect1d(FIND, FIND1)
    if len(BOOL_FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 3.차고지-다용도실-주방-거실

# In[ ]:


#차고지-다용도실-주방-거실이 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 19) & (df['Adj_Label']==6)]['Adj_ID_encode'].values #차고지-다용도
    FIND1=df.loc[(df['Label'] == 6) & (df['Adj_Label']==3)]['ID_encode'].values #다용도-주방
    
    FIND2=df.loc[(df['Label'] == 6) & (df['Adj_Label']==3)]['Adj_ID_encode'].values #다용도-주방
    FIND3=df.loc[(df['Label'] == 3) & (df['Adj_Label']==1)]['ID_encode'].values #주방-거실
    
    BOOL_FIND=np.intersect1d(FIND, FIND1)
    BOOL_FIND1=np.intersect1d(FIND2, FIND3)
    if (len(BOOL_FIND)!=0)&(len(BOOL_FIND1)!=0):
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 4.차고지-복도-방

# In[ ]:


#차고지-복도-방 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 19) & (df['Adj_Label']==8)]['Adj_ID_encode'].values
    FIND1=df.loc[(df['Label'] == 8) & (df['Adj_Label']==2)]['ID_encode'].values
    BOOL_FIND=np.intersect1d(FIND, FIND1)
    if len(BOOL_FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 5.차고지-세탁실

# In[ ]:


#차고지-다용도실 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 19) & (df['Adj_Label']==6)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 6.차고지-식당-거실

# In[ ]:


#차고지-식당-거실 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 19) & (df['Adj_Label']==20)]['Adj_ID_encode'].values
    FIND1=df.loc[(df['Label'] == 20) & (df['Adj_Label']==1)]['ID_encode'].values
    BOOL_FIND=np.intersect1d(FIND, FIND1)
    if len(BOOL_FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 7.차고지-다용도실-주방-식당

# In[ ]:


#차고지-다용도실-주방-식당이 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 19) & (df['Adj_Label']==6)]['Adj_ID_encode'].values #차고지-다용도
    FIND1=df.loc[(df['Label'] == 6) & (df['Adj_Label']==3)]['ID_encode'].values #다용도-주방
    
    FIND2=df.loc[(df['Label'] == 6) & (df['Adj_Label']==3)]['Adj_ID_encode'].values #다용도-주방
    FIND3=df.loc[(df['Label'] == 3) & (df['Adj_Label']==20)]['ID_encode'].values #주방-식당
    
    BOOL_FIND=np.intersect1d(FIND, FIND1)
    BOOL_FIND1=np.intersect1d(FIND2, FIND3)
    if (len(BOOL_FIND)!=0)&(len(BOOL_FIND1)!=0):
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 8.차고지-계단

# In[ ]:


#차고지-계단 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 19) & (df['Adj_Label']==7)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 9.차고지-포치

# In[ ]:


#차고지-포치 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 19) & (df['Adj_Label']==18)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 10.차고지-복도

# In[ ]:


#차고지-복도 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 19) & (df['Adj_Label']==8)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# # 세탁실

# ### 1.복도-세탁실-욕실

# In[ ]:


#복도-세탁실-욕실 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 8) & (df['Adj_Label']==10)]['Adj_ID_encode'].values
    FIND1=df.loc[(df['Label'] == 10) & (df['Adj_Label']==4)]['ID_encode'].values
    BOOL_FIND=np.intersect1d(FIND, FIND1)
    if len(BOOL_FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 2. 세탁실-붙박이장

# In[ ]:


#세탁실-붙박이장 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 10) & (df['Adj_Label']==11)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 3.세탁실-복도-붙박이장

# In[ ]:


#세탁실-복도-붙박이장 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 10) & (df['Adj_Label']==8)]['Adj_ID_encode'].values
    FIND1=df.loc[(df['Label'] == 8) & (df['Adj_Label']==11)]['ID_encode'].values
    BOOL_FIND=np.intersect1d(FIND, FIND1)
    if len(BOOL_FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 4.세탁실-복도-다용도실

# In[ ]:


#세탁실-복도-다용도실 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 10) & (df['Adj_Label']==8)]['Adj_ID_encode'].values
    FIND1=df.loc[(df['Label'] == 8) & (df['Adj_Label']==6)]['ID_encode'].values
    BOOL_FIND=np.intersect1d(FIND, FIND1)
    if len(BOOL_FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 5.세탁실-복도-방

# In[ ]:


#세탁실-복도-방 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 10) & (df['Adj_Label']==8)]['Adj_ID_encode'].values
    FIND1=df.loc[(df['Label'] == 8) & (df['Adj_Label']==2)]['ID_encode'].values
    BOOL_FIND=np.intersect1d(FIND, FIND1)
    if len(BOOL_FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 6.복도-세탁실-차고지

# In[ ]:


#복도-세탁실-차고지 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 8) & (df['Adj_Label']==10)]['Adj_ID_encode'].values
    FIND1=df.loc[(df['Label'] == 10) & (df['Adj_Label']==19)]['ID_encode'].values
    BOOL_FIND=np.intersect1d(FIND, FIND1)
    if len(BOOL_FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 7.차고지-세탁실-현관

# In[ ]:


#차고지-세탁실-현관 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 19) & (df['Adj_Label']==10)]['Adj_ID_encode'].values
    FIND1=df.loc[(df['Label'] == 10) & (df['Adj_Label']==0)]['ID_encode'].values
    BOOL_FIND=np.intersect1d(FIND, FIND1)
    if len(BOOL_FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 8.세탁실-복도-화장실

# In[ ]:


#세탁실-복도-화장실 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 10) & (df['Adj_Label']==8)]['Adj_ID_encode'].values
    FIND1=df.loc[(df['Label'] == 8) & (df['Adj_Label']==4)]['ID_encode'].values
    BOOL_FIND=np.intersect1d(FIND, FIND1)
    if len(BOOL_FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 9.세탁실-복도-주방

# In[ ]:


#세탁실-복도-주방 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 10) & (df['Adj_Label']==8)]['Adj_ID_encode'].values
    FIND1=df.loc[(df['Label'] == 8) & (df['Adj_Label']==3)]['ID_encode'].values
    BOOL_FIND=np.intersect1d(FIND, FIND1)
    if len(BOOL_FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 10.세탁실-복도-거실

# In[ ]:


#세탁실-복도-거실 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 10) & (df['Adj_Label']==8)]['Adj_ID_encode'].values
    FIND1=df.loc[(df['Label'] == 8) & (df['Adj_Label']==1)]['ID_encode'].values
    BOOL_FIND=np.intersect1d(FIND, FIND1)
    if len(BOOL_FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# # 드레스룸

# ### 1. 화장실-붙박이장-드레스룸

# In[ ]:


#화장실-붙박이장-드레스룸 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 4) & (df['Adj_Label']==11)]['Adj_ID_encode'].values
    FIND1=df.loc[(df['Label'] == 11) & (df['Adj_Label']==5)]['ID_encode'].values
    BOOL_FIND=np.intersect1d(FIND, FIND1)
    if len(BOOL_FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 2. 복도-방-화장실-드레스룸

# In[ ]:


#복도-방-화장실-드레스룸이 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 8) & (df['Adj_Label']==2)]['Adj_ID_encode'].values #거실-방
    FIND1=df.loc[(df['Label'] == 2) & (df['Adj_Label']==4)]['ID_encode'].values #방-화장실
    
    FIND2=df.loc[(df['Label'] == 2) & (df['Adj_Label']==4)]['Adj_ID_encode'].values #방-화장실
    FIND3=df.loc[(df['Label'] == 4) & (df['Adj_Label']==5)]['ID_encode'].values #화장실-드레스룸
    
    BOOL_FIND=np.intersect1d(FIND, FIND1)
    BOOL_FIND1=np.intersect1d(FIND2, FIND3)
    if (len(BOOL_FIND)!=0)&(len(BOOL_FIND1)!=0):
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 3. 방-화장실, 방-붙박이장,방-드레스룸

# In[ ]:


#방-드레스룸,방-화장실,방-붙박이장 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 2) & (df['Adj_Label']==5)]['ID_encode'].values
    FIND1=df.loc[(df['Label'] == 2) & (df['Adj_Label']==4)]['ID_encode'].values
    FIND2=df.loc[(df['Label'] == 2) & (df['Adj_Label']==11)]['ID_encode'].values
    if (len(FIND1)!=0)&(len(FIND)!=0)&(len(FIND2)!=0):
            Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 4. 거실-방-화장실-드레스룸

# In[ ]:


#거실-방-화장실-드레스룸이 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 1) & (df['Adj_Label']==2)]['Adj_ID_encode'].values #거실-방
    FIND1=df.loc[(df['Label'] == 2) & (df['Adj_Label']==4)]['ID_encode'].values #방-화장실
    
    FIND2=df.loc[(df['Label'] == 2) & (df['Adj_Label']==4)]['Adj_ID_encode'].values #방-화장실
    FIND3=df.loc[(df['Label'] == 4) & (df['Adj_Label']==5)]['ID_encode'].values #화장실-드레스룸
    
    BOOL_FIND=np.intersect1d(FIND, FIND1)
    BOOL_FIND1=np.intersect1d(FIND2, FIND3)
    if (len(BOOL_FIND)!=0)&(len(BOOL_FIND1)!=0):
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 5. 드레스룸-세탁실

# In[ ]:


#드레스룸-세탁실 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 5) & (df['Adj_Label']==10)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# # 붙박이장

# ### 1.계단실-붙박이장

# In[ ]:


#계단-붙박이장 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 7) & (df['Adj_Label']==11)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 2.거실-붙박이장

# In[ ]:


#거실-붙박이장 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 1) & (df['Adj_Label']==11)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 3.화장실-붙박이장

# In[ ]:


#화장실-붙박이장 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 4) & (df['Adj_Label']==11)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 4.방-붙박이장

# In[ ]:


#방-붙박이장 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 2) & (df['Adj_Label']==11)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 5. 방-화장실, 방-붙박이장,방-복도

# In[ ]:


#방-복도,방-화장실,방-붙박이장 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 2) & (df['Adj_Label']==8)]['ID_encode'].values
    FIND1=df.loc[(df['Label'] == 2) & (df['Adj_Label']==4)]['ID_encode'].values
    FIND2=df.loc[(df['Label'] == 2) & (df['Adj_Label']==11)]['ID_encode'].values
    if (len(FIND1)!=0)&(len(FIND)!=0)&(len(FIND2)!=0):
            Test.append(CSV.split('\\')[-1].split('.')[0])


# # 다용도실

# ### 1.다용도실-붙박이장 

# In[ ]:


#다용도실-붙박이장 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 6) & (df['Adj_Label']==11)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 2. 세탁실-다용도실

# In[ ]:


#세탁실-다용도실 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 10) & (df['Adj_Label']==6)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 3. 복도-다용도실-차고지

# In[ ]:


#복도-다용도실-차고지 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 8) & (df['Adj_Label']==6)]['Adj_ID_encode'].values
    FIND1=df.loc[(df['Label'] == 6) & (df['Adj_Label']==19)]['ID_encode'].values
    BOOL_FIND=np.intersect1d(FIND, FIND1)
    if len(BOOL_FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 4. 주방-다용도실

# In[ ]:


#주방-다용도실 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 3) & (df['Adj_Label']==6)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 5. 주방-다용도실-차고지

# In[ ]:


#주방-다용도-차고지 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 3) & (df['Adj_Label']==6)]['Adj_ID_encode'].values
    FIND1=df.loc[(df['Label'] == 6) & (df['Adj_Label']==19)]['ID_encode'].values
    BOOL_FIND=np.intersect1d(FIND, FIND1)
    if len(BOOL_FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# # 펜트리실

# ### 1. 거실-펜트리실

# In[ ]:


#거실-펜트리실 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 1) & (df['Adj_Label']==9)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 2. 복도-펜트리실

# In[ ]:


#복도-펜트리실 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 8) & (df['Adj_Label']==9)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 3. 거실-주방-펜트리실

# In[ ]:


#거실-주방-펜트리실 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 1) & (df['Adj_Label']==3)]['Adj_ID_encode'].values
    FIND1=df.loc[(df['Label'] == 3) & (df['Adj_Label']==9)]['ID_encode'].values
    BOOL_FIND=np.intersect1d(FIND, FIND1)
    if len(BOOL_FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 4. 다용도실-펜트리실

# In[ ]:


#다용도실-펜트리실 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 6) & (df['Adj_Label']==9)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])


# ### 5. 현관-펜트리실

# In[ ]:


#현관-펜트리실 연결된 관계
Test=[]
for CSV in CSV_LIST:
    df = pd.read_csv(CSV,index_col=None,usecols=[1,3,4,5])
    FIND=df.loc[(df['Label'] == 0) & (df['Adj_Label']==9)]['ID_encode'].values
    if len(FIND)!=0:
        Test.append(CSV.split('\\')[-1].split('.')[0])

