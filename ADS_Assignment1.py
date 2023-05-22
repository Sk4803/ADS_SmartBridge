#!/usr/bin/env python
# coding: utf-8

# ## 1. Assign your Name to variable name and Age to variable age. Make a Python program that prints your name and age.

# In[1]:


name = "Suryakant Patwardhan"
age = 19
print("Name: ", name)
print("Age: ", age)


# ## 2. X="Datascience is used to extract meaningful insights." Split the string.

# In[2]:


X="Datascience is used to extract meaningful insights."
print(X.split(" "))


# ## 3. Make a function that gives multiplication of two numbers.

# In[3]:


def multiply(a, b):
    return a*b
print(multiply(2, 3))


# ## 4. Create a Dictionary of 5 States with their capitals. also print the keys and values.

# In[8]:


dict = {"Madhya Pradesh": "Bhopal", "Rajasthan" : "Jaipur", "Gujarat" : "Gandhinagar", "Uttar Pradesh" : "Lucknow", "Maharashtra" : "Mumbai"}
for a in dict:
    print(a, ":", dict[a])


# ## 5. Create a list of 1000 numbers using range function.

# In[10]:


list1 = []
for i in range(1, 1001):
    list1.append(i)
print(list1)


# ## 6. Create an identity matrix of dimension 4 by 4.

# In[11]:


import numpy as np
matrix = np.identity(4, dtype = int)
print(matrix)


# ## 7. Create a 3x3 matrix with values ranging from 1 to 9.

# In[13]:


np.arange(1, 10).reshape(3, 3)


# ## 8. Create 2 similar dimensional array and perform sum on them.

# In[14]:


arr1 = np.arange(1, 10).reshape(3, 3)
arr2 = np.arange(11, 20).reshape(3, 3)
np.add(arr1, arr2)


# ## 9. Generate the series of dates from 1st Feb, 2023 to 1st March, 2023 (both inclusive).

# In[17]:


import datetime
start = datetime.date(2023,2,1)
k = 29
res = []
for day in range(k):
    date = (start + datetime.timedelta(days = day)).isoformat()
    res.append(date)
print(str(res))


# ## 10. Given a dictionary, convert it into corresponding dataframe and display it. dictionary = {'Brand': ['Maruti', 'Renault', 'Hyndai'], 'Sales' : [250, 200, 240]}.

# In[21]:


import pandas as pd
dictionary = {'Brand': ['Maruti', 'Renault', 'Hyndai'], 'Sales' : [250, 200, 240]}
dataframe = pd.DataFrame.from_dict(dictionary)
print(dataframe)


# In[ ]:




