#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd 

df = pd.read_csv('https://raw.githubusercontent.com/KeithGalli/pandas/master/pokemon_data.csv')

print(df)


# In[50]:


## Read Headers
#print(df.columns)

## Read each Column
#print(df[['Name', 'Type 1', 'HP']])

##Read Each Row
#print(df.iloc[0:4])
#for index, row in df.iterrows():
   # print(index, row['Name'])
df.loc[df['Type 1'] == "Fire"]

## Read a specific Location (R,C)
#print(df.iloc[2,1])


# In[53]:


df.describe()
df.sort_values('Name', ascending=False)


# In[59]:


df.sort_values(['Type 1', 'HP'], ascending=False)


# In[60]:


df.head(5)


# In[69]:


#df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']

#df = df.drop(columns=['Total'])

df['Total'] = df.iloc[:, 4:9].sum(axis=1)

cols = list(df.columns.values)
df = df[cols[0:4] + [cols[-1]]+cols[4:12]]

df.head(5)


# In[65]:


45+49+49+65+65+45


# In[79]:


#df.to_csv('modified.cvs', index=False)

df.to_excel('modified.xlsx', index=False)


# In[81]:


new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]

#new_df.to_csv('filtered.csv')

new_df.reset_index(drop=True, inplace=True)

new_df


# In[90]:


#new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]
import re 

df.loc[~df['Type 1'].str.contains('fire|grass', regex=True)]


# In[98]:


df.loc[df['Total'] > 500, ['Generation', 'Legendary']] = ['Test 1', 'Test 2']

df


# In[102]:


df['count'] = 1

df

df.groupby(['Type 1', 'Type 2']).count()['count']


# In[107]:


for df in (chunksize==5):
    print("CHUNK DF")
    print(df)


# In[ ]:




