#!/usr/bin/env python
# coding: utf-8

# In[2]:


numbers_1 = list(map(int, input().split()))
numbers_2 = list(map(int, input().split()))
result = tuple(set(numbers_1) & set(numbers_2))
print(*result, sep=" ")


# In[ ]:




