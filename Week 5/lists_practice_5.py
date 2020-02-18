#!/usr/bin/env python
# coding: utf-8

# In[4]:


string1 = input()
string2 = input()
numbers1 = list(map(int, string1.split()))
numbers2 = list(map(int, string2.split()))
result = list(set(numbers1) & set(numbers2))
for e in result:
    print(e, end=" ")


# In[ ]:




