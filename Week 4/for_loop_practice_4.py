#!/usr/bin/env python
# coding: utf-8

# In[9]:


numbers_1 = list(map(int, input().split()))
numbers_2 = list(map(int, input().split()))
intersection = tuple(set(numbers_1) & set(numbers_2))
print(intersection)


# In[ ]:




